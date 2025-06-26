import tkinter as tk
from login.login import Login

if __name__ == "__main__":
    root = tk.Tk()
    login = Login(root)
    root.mainloop()