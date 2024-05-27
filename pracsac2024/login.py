import tkinter as tk

class Login:
    def __init__(self, root, xml):
        self.root = root
        self.xml = xml

        self.username = tk.Entry(self.root)
        self.password = tk.Entry(self.root)

        self.login_button = tk.Button(self.root, text="Login", command=self.username_validate)

        self.pack()
    def username_validate(self):
        username = self.username.get()
        password = self.password.get()
        xml_root = self.xml.getroot()
        users = xml_root.findall("user")
        if len(username) == 5 and len(password) == 5:
            for user in users:
                username_element = user.find("username")
                username_text = username_element.text
                if username_text == username:
                    currid = user.find("id")
                    self.password_validate(currid.text, users, password)

        else:
            print(f"username needs to be 5 characters or more,\nusername is {len(username)} and password is {len(password)} characters long")
    def password_validate(self, id, users, password):
        for user in users:
            id_element = user.find("id")
            password_element = user.find("password")
            if id_element.text == id and password_element.text == password:
                print("success")
    def pack(self):
        self.root.geometry("640x480")
        self.username.pack()
        self.password.pack()
        self.login_button.pack()