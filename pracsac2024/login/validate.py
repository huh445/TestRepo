import xml.etree.ElementTree as ET

class Validate:
    def __init__(self):
        self.xml = ET.parse("passwords.xml")
        xml_root = self.xml.getroot()
        self.users = xml_root.findall("user")
    def login(self, username, password):
        if len(username) == 5 and len(password) == 5:
            for user in self.users:
                staff_element = user.find("staff")
                username_element = user.find("username")
                user_id = user.find("id").text
                if staff_element is not None:
                    staff = True
                else:
                    staff = False
                if username_element.text == username:
                    password_element = user.find("password")
                    if password_element.text == password:
                        return True, staff, user_id
        else:
            print(f"username needs to be 5 characters or more,\nusername is {len(username)} and password is {len(password)} characters long")
        return False, False
    def change_password(self, id, password):
        for user in self.users:
            user_id = user.find("id")
            if id == user_id.text:
                password_element = user.find("password")
                password_element.text = password
                self.xml.write("passwords.xml")