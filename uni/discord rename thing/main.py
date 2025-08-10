from json.decoder import JSONDecodeError
from typing import Any, Union

from datetime import datetime as date
from sys import stdout
from os import path

import requests
import json
import os


# the settings (mostly locations to files)
account_data   = 'account/user.json'
messages_dir   = 'messages'
reporting_files = (
  'activity/reporting/events-2021-00000-of-00001.json',
  'activity/tns/events-2021-00000-of-00001.json'
)

# first param is the token, the following is True if it's a bot token, False for a user token
fetch_token = ( '', True )

# show the top X messaged people
top_x = 10

# mostly for demo purposes if you don't want to leak info
censor_user_ids      = False
hide_discord_discrim = True

ascii_art   = [ 
  ':F$MMM       $MM$F', 
  'MNNNNNNNNNNNNNNNNNNNM:', 
  'MMNNNNNNNNNNNNNNNNNNNMM*', 
  'MMNNNMMMMMNNNNNMMMMMNNNMM', 
  '$NNNNMF    $MNN$    *MNNNN$', 
  'MNNNNM     *MNNF     MNNNNM', 
  'MNNNNM$   *MMNNM*   VMNNNNM*', 
  ':MNNNNMMMMMMNNNNNMMMMMMNNNNM*', 
  '*$MMNM**:**FVVVF**:**MNMM$*', 
  '*V$             $V*' 
]
ascii_width = 34


class VerboseLogger:
  outstanding = False


  def start(self, message: Any) -> None:
    # a line break if there's an outstanding one
    if self.outstanding:
      print()
    
    # print the message without a line break
    print(message, end='')
    self.outstanding = True

    stdout.flush()


  def complete(self, done_message: str = None) -> None:
    if self.outstanding and done_message:
      print()

    self.outstanding = False
    print(f'{done_message if done_message else ""} ... done')


class User:
  def __init__(self, id: str) -> None:
    self.id = id

    self.username = 'Unknown'
    self.discrim  = 0

    # a map of ids to display names
    self.relations = {}


  def fetch(self) -> bool:
    if not fetch_token[0]:
      return
    
    response = requests.get(f'https://discord.com/api/v8/users/{self.id}', headers={ 'Authorization': f'{"Bot " if fetch_token[1] else ""}{fetch_token[0]}' })
    
    # make sure we didn't get any other code than 200s
    if not response.ok:
      return False

    # convert to a json object then parse both the username and discrim
    response = response.json()

    self.username = response.get('username')
    self.discrim  = response.get('discriminator')

    return True


  def find_user(self, id: str) -> Any:
    return self.relations.get(id)


  def __str__(self):
    # don't show the discriminator if requested
    if hide_discord_discrim:
      return self.username

    return f'{self.username}#{self.discrim:0>4}'


class MessageFolder:
  channel_data = 'channel.json'
  channel_type = -1

  recipient: User = None
  recp_id: str = 0
  
  __message_count_cache = -1


  def __init__(self, folder: str, profile: Union[User, None]) -> None:
    self.__full_path = path.join(messages_dir, folder)

    # this is important to keep so we can figure out who the recipient is
    self.owner = profile

    # figure out the channel type
    self.__parse_channel_data()


  def is_dm_channel(self) -> bool:
    return self.channel_type == 1


  def __str__(self) -> str:
    return f'MessageFolder [ {self.recipient=}, {self.recp_id=} ]'


  def message_count(self) -> int:
    # just use the cache to avoid a lot of load time
    if self.__message_count_cache != -1:
      return self.__message_count_cache

    count = 0
    
    # the full path to the messages csv file
    messages = path.join(self.__full_path, 'messages.csv')

    # open the messages file and read the occurences of \n in it
    with open(messages, 'rb') as messages_file:
      # read one character until the file is over
      while True:
        ch = messages_file.read(1)
        
        if not ch:
          break  # the file is over, EOF

        # check for a \n, if it's there then add one to the count
        if ch == b'\n':
          count += 1

    self.__message_count_cache = count

    return count


  def __parse_channel_data(self) -> None:
    # get the full path to the channel.json file
    channel_path = path.join(self.__full_path, self.channel_data)

    # parse the channel path as json for reading later
    data = {}
    with open(channel_path, 'r', encoding='utf-8') as channel_file:
      data = json.load(channel_file)
    
    # get the channel type and check if it's a dm channel
    self.channel_type = data.get('type', -1)
    
    if not self.is_dm_channel():
      return

    # remove the owner id from the list
    recipients: list = data.get('recipients', [])
    recipients.remove(self.owner.id)

    # only if there's one recipient left then we set the field with a mapped relation user
    if len(recipients) == 1:
      self.recp_id   = recipients[0]
      self.recipient = self.owner.find_user(self.recp_id)


class Activity:
  __ips  = set()

  __ip_n = 0
  messages_n = 0

  first_activity = None


  def add_ip(self, ip: Union[str, None]) -> None:
    # if there's no ip then it's ok
    if not ip:
      return

    # add the ip and increment the count
    self.__ips.add(ip)
    self.__ip_n += 1


  def ip_count(self) -> int:
    return self.__ip_n


  def is_before_first(self, compare: date) -> bool:
    if not self.first_activity:
      return True

    return compare.timestamp() < self.first_activity.timestamp()


class LogLine:
  def __init__(self, key: str, data: Union[str, int] = '', key_width: int = 0) -> None:
    self.key  = key
    self.line = data

    # the width the key will be
    self.fixed = key_width


  def __str__(self) -> str:
    parsed = self.line

    # parse the number with a comma
    if type(self.line) is int:
      parsed = f'{self.line:,}'

    return f'{self.key:<{self.fixed}}: {parsed}'


class LogBreak(LogLine):
  def __init__(self) -> None:
    super().__init__(None, None)


  def __str__(self) -> str:
    return ''


int_len = lambda n: len(str(n))


def main() -> int:
  logger = VerboseLogger()

  # the lines to print with the art at the end
  lines: list[LogLine] = []

  # get the user's profile
  logger.start('parsing user file')
  profile = get_self(account_data)
  logger.complete()

  logger.start('fetching all message channels')
  channels = parse_message_channels(profile)

  # do a quick filter by checking if the recipient is there
  logger.start('filtering and sorting only dms')
  top_dms = filter_sort(channels)

  logger.complete()
  logger.complete('message channels fetched')

  # do a nice little visual on finding each user
  display_user_finding(top_dms)

  logger.start('parsing activity file')
  activity = parse_activity()

  # make sure the file doesn't fuck itself
  # if not activity:
    # print(f'no such file, check the name {reporting_files!r}')
    # return -1

  logger.complete()

  # add a bunch of line details
  lines.append(LogLine('Package sum', profile))
  lines.append(LogBreak())

  lines.append(LogLine(f'Top messages of a total {activity.messages_n:,} sent'))
  # add all the top dms
  for n, dm in enumerate(top_dms):
    count   = dm.message_count()
    percent = count / activity.messages_n * 100

    lines.append(LogLine(f'  #{n + 1:<{int_len(top_x)}} {dm.recipient}', f'{count:<{int_len(activity.messages_n) + 1},} ({percent:.2f}%)', 24))

  lines.append(LogBreak())

  lines.append(LogLine('First activity', f'{activity.first_activity:%B %Y}'))
  lines.append(LogLine('Total unique IP count', activity.ip_count()))

  print_ascii(lines)

  return 0


def print_ascii(lines: list[LogLine]) -> None:
  global ascii_art, ascii_width

  print()  # extra \n

  padding = 0

  # go through the lines and print each
  ascii_n = len(ascii_art)
  line_n  = len(lines)

  # whichever one is bigger then we will use that one
  count = max(ascii_n, line_n)

  # what column to start printing the ascii art
  start = 0

  if count != ascii_n:
    start = line_n // 2 - ascii_n // 2

  for n in range(count):
    # print the piece of the ascii art dependent on the starting position
    y = n - start

    piece = ascii_art[y] if y < ascii_n and n >= start else ''
    print(f'{piece:^{ascii_width}}', end='')

    i = n - padding

    # only print lines after the padding
    if i >= line_n or n < padding:
      print()  # add a \n
      continue
    
    # print the line next to the ascii line
    print(lines[i])

  print()  # extra \n


def display_user_finding(top_channels: list[MessageFolder]) -> None:
  if not fetch_token:
    print('skipping due to a lack of a token')
    return

  print()  # a little padding on the messages following
  
  # print the headings
  print(f'{"User ID":<20}{"Status":>10}    Result')

  # go through each user and make an attempt to find their real 
  for channel in top_channels:
    user_id    = channel.recp_id
    is_present = bool(channel.recipient)

    if censor_user_ids:  # replace all characters with astrix
      user_id = '*' * len(user_id)

    status = 'FETCHING'  # PRESENT or FETCHING
    if is_present:
      status = 'PRESENT'

    print(f'{user_id:<20}{status:>10} -> ', end='')

    # just give the normal result and return
    if not is_present:
      # make the new user, fetch it, and update it
      user = User(channel.recp_id)
      if not user.fetch():
        print('FAILED')
        continue

      channel.recipient = user
    
    print(channel.recipient)

  print()


def parse_time(timestamp: str) -> Union[date, None]:
  # the formats that will get used to test
  date_formats = ( '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%dT%H:%M:%S.%fZ' )
  
  time: date = None
  n = 0

  # run until there's no date_formats left
  while not time and n < len(date_formats):
    current = date_formats[n]

    try:
      # parse the date using the current format
      time = date.strptime(timestamp, current)
    except ValueError:
      n += 1  # if it fails to parse then go to the next date

  return time


def get_self(user_profile: str) -> User:
  # no fiLE
  if not path.exists(user_profile):
    return None

  # open the file and parse completely as json
  json_data: dict = {}

  with open(user_profile, 'r', encoding='utf-8') as user_file:
    json_data = json.load(user_file)
  
  # make a user of the ID
  user = User(json_data.get('id'))

  user.username = json_data.get('username', 'Unknown')
  user.discrim  = int(json_data.get('discriminator', 0))  # parse as int

  # parse the relationships to avoid fetching for user's, default to an empty list
  for relation in json_data.get('relationships', []):
    # create a friend user with their id
    friend = User(relation.get('id', 0))

    user_data = relation.get('user', {})
    
    friend.username = user_data.get('username', 'Unknown friend')
    friend.discrim  = user_data.get('discriminator', 0)

    # add the friend to the relations mapping
    user.relations[friend.id] = friend

  # send the user back with all the proper information
  return user


def parse_message_channels(profile: User) -> list[MessageFolder]:
  folders = []

  # go through each directory in the messages folder and add it to the list
  for channel_folder in os.listdir(messages_dir):
    full_path = path.join(messages_dir, channel_folder)

    # make sure no files get indexed into
    if not path.isdir(full_path):
      continue

    folders.append(MessageFolder(channel_folder, profile))

  return folders


def filter_sort(channels: list[MessageFolder]) -> list[MessageFolder]:
  top_messages = channels[:]  # the top messages is a copy of the channels

  # filter the channels by testing if the recipient exists
  top_messages = list(filter(lambda channel: channel.is_dm_channel(), top_messages))

  # sort by the message count and reverse the order
  top_messages = sorted(top_messages, key=lambda channel: channel.message_count(), reverse=True)

  # return the list from 0 to the top x
  return top_messages[0:top_x]


def parse_activity() -> Activity:
  activity = Activity()

  for file_name in reporting_files:
    # make sure the file exists
    if not path.exists(file_name):
      continue

    # open the activity file
    handle = open(file_name, 'r', encoding='utf-8')

    # go through each line and parse it as json
    for line in handle:
      if line == None:
        break

      # make sure we can actually parse the line
      try:
        obj: dict = json.loads(line)
      except JSONDecodeError:
        continue

      # remove the quotes surrounding the timestamp field
      time = parse_time(obj.get('timestamp').strip('"'))

      if obj.get('event_type', '') == 'send_message':
        activity.messages_n += 1

      # update the first activity date
      if activity.is_before_first(time):
        activity.first_activity = time

      # add the IP from the object
      activity.add_ip(obj.get('ip'))

    # close the file and return the activity
    handle.close()
  
  return activity


if __name__ == '__main__':
  try:
    exit(main())
  except KeyboardInterrupt:
    print('\nexiting...')
    exit()
