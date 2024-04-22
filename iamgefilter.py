import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter

class ImageEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Convoluted Image Editor")

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

        self.load_button = tk.Button(self.master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.filter_var = tk.StringVar()
        self.filter_var.set("BLUR")
        self.filter_menu = tk.OptionMenu(self.master, self.filter_var, "BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EMBOSS", "SHARPEN")
        self.filter_menu.pack()

        self.apply_filter_button = tk.Button(self.master, text="Apply Filter", command=self.apply_filter)
        self.apply_filter_button.pack()

        self.save_button = tk.Button(self.master, text="Save Image", command=self.save_image)
        self.save_button.pack()

        self.image = None

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def display_image(self):
        if self.image:
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.photo)

    def apply_filter(self):
        if self.image:
            filter_type = self.filter_var.get()
            if filter_type == "BLUR":
                self.image = self.image.filter(ImageFilter.BLUR)
            elif filter_type == "CONTOUR":
                self.image = self.image.filter(ImageFilter.CONTOUR)
            elif filter_type == "DETAIL":
                self.image = self.image.filter(ImageFilter.DETAIL)
            elif filter_type == "EDGE_ENHANCE":
                self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter_type == "EMBOSS":
                self.image = self.image.filter(ImageFilter.EMBOSS)
            elif filter_type == "SHARPEN":
                self.image = self.image.filter(ImageFilter.SHARPEN)
            self.display_image()

    def save_image(self):
        if self.image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            if save_path:
                self.image.save(save_path)
                messagebox.showinfo("Save Image", "Image saved successfully!")

def main():
    root = tk.Tk()
    app = ImageEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
