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
        xml_root = self.xml.getroot()
        users = xml_root.findall("user")
        # print("0")
        if len(username) == 5:
            # print("1")
            # print("1.5")
            for user in users:
                # print("2")
                username_element = user.find("username")
                username_text = username_element.text
                if username_text == username:
                    print("yarp")
        else:
            print("username needs to be 5 characters or more")
    def pack(self):
        self.root.geometry("640x480")
        self.username.pack()
        self.password.pack()
        self.login_button.pack()