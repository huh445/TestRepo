import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class tkinterStuff:
    def __init__(self, master):
        self.master = master
        self.master.title("John"s image playlist")
        self.master.geometry("640x480")

        self.image = tk.Label(self.master)
        self.image.pack()

        self.imageButton = tk.Button(self.master, text="Upload Image", command=self.uploadImage)
        self.imageButton.pack()

        self.ifImage = None

    def uploadImage(self):
        filePath = filedialog.askopenfilename()
        if filePath:
            self.ifImage = Image.open(filePath)
            self.displayImage()
    
    def displayImage(self):
        if self.image:
            self.photo = ImageTk.PhotoImage(self.ifImage)
            self.image.config(image=self.photo)

def main():
    root = tk.Tk()
    app = tkinterStuff(root)
    root.mainloop()


if __name__ == "__main__":
    main()