import tkinter as tk

credentials = {"john": "b edwards", "sexual": "harrassment", "fortnite": "balls"}

class appLogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("640x480")

        self.loginAttempts = 0

        self.usernameEntry = tk.Entry(root)
        self.usernameEntry.pack()

        self.passwordEntry = tk.Entry(root, show="*")
        self.passwordEntry.pack()

        self.loginButton = tk.Button(root, text="Login", command=self.login)
        self.loginButton.pack()

        self.label = tk.Label(root)
        self.label.pack()
    
    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if username in credentials and credentials[username] == password and self.loginAttempts < 2:
            self.label.config(text="Successful Login.")
            self.loginAttemps = 0
        elif self.loginAttempts < 2:
            self.loginAttempts += 1
            self.label.config(text=f"Username or Password incorrect, {3 - self.loginAttempts} attempts left.")
        else:
            self.label.config(text="No More Attempts Left.")
            self.loginButton.pack_forget()
            self.usernameEntry.pack_forget()
            self.passwordEntry.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = appLogin(root)
    root.mainloop()