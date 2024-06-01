import tkinter as tk
from tkinter import messagebox
import xml.etree.ElementTree as ET

class ImportXML:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple XML Viewer")

        self.text_area = tk.Text(self.root, wrap="word", width=50, height=15)
        self.text_area.pack(pady=10)

        load_button = tk.Button(self.root, text="Load XML", command=self.load_xml)
        load_button.pack()

        self.root.mainloop()
    def load_xml(self):
        try:
            tree = ET.parse("xmlpractice/data.xml")
            root = tree.getroot()

            self.text_area.delete("1.0", tk.END)

            for contact  in root.findall("contact"):
                name = contact.find("name").text
                email = contact.find("email").text
                self.text_area.insert(tk.END, f"Name: {name}\nEmail: {email}\n\n")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load XML file: {e}")
            
if __name__ == "__main__":
    john = ImportXML()