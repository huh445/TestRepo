import xml.etree.ElementTree as ET

class Validate:
    def __init__(self):
        xml = ET.parse("passwords.xml")
        xml_root = xml.getroot()
        self.users = xml_root.findall("user")
    
    def login(self, username, password):
        if len(username) == 5 and len(password) == 5:
            for users in self.users:
                username_element = users.find("username").text
                password_element = users.find("password").text
                staff_element = users.find("staff").text
                id = users.find("id").text
                if staff_element is not None:
                    staff = True
                else:
                    staff = False
                if username_element == username and password_element == password:
                    return True, staff, id
        else:
            print("Error, username and password has to be 5 characters")
    
    def change_password(self, password, id):
        for users in self.users:
            id_element = users.find("id").text
            if id == id_element:
                password_element = users.find("password")
                password_element.text = password
                self.xml.write("passwords.xml")