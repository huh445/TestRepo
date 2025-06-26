import tkinter as tk
from tkinter import messagebox
from get_vid import GetVid
import webbrowser

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.get_vid = GetVid()
        
        self.button = tk.Button(self.root, text="Skibidi Toilet", command=self.skib)

        self.run()

    def skib(self):
        try:
            response = self.get_vid.get_vid()
            if response:
                webbrowser.open(response)
        except Exception as e:
            messagebox.showerror("Error", f"An error occured: {e}")
    
    def run(self):
        self.button.pack()
        self.root.title("Skibidi Toilet")
        self.root.geometry("640x480")
        self.root.mainloop()