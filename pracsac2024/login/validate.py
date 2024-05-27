import xml.etree.ElementTree as ET

class Validate:
    def __init__(self):
        self.xml = ET.parse("passwords.xml")
    def login(self, username, password):
        xml_root = self.xml.getroot()
        users = xml_root.findall("user")
        if len(username) == 5 and len(password) == 5:
            for user in users:
                username_element = user.find("username")
                if username_element.text == username:
                    password_element = user.find("password")
                    if password_element.text == password:
                        return True
        else:
            print(f"username needs to be 5 characters or more,\nusername is {len(username)} and password is {len(password)} characters long")
        return False