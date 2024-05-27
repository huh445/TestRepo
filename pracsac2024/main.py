import tkinter as tk
import xml.etree.ElementTree as ET
from login import Login

if __name__ == "__main__":
    root = tk.Tk()
    xml = ET.parse("passwords.xml")
    login = Login(root, xml)
    root.mainloop()