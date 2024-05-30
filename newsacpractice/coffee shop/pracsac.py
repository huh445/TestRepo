import tkinter as tk

class Books:
    def __init__(self):
        self.root = tk.Tk()
        
        self.title = tk.Label(self.root, text="Register points")

        self.first_name_label = tk.Label(self.root, text="First Name:")
        self.first_name = tk.Entry(self.root)
        self.last_name_label = tk.Label(self.root, text="Last Name:")
        self.last_name = tk.Entry(self.root)
        self.email_label = tk.Label(self.root, text="Email:")
        self.email = tk.Entry(self.root)
        self.qty_label = tk.Label(self.root, text="Amount of books")
        self.qty = tk.Entry(self.root)

        self.error_message = tk.Label(self.root)

        self.button = tk.Button(self.root, text="Register", command=self.validate)

        self.pack()

    def validate(self):
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        email = self.email.get()
        qty = self.qty.get()
        error_message = ""

        if not first_name and not last_name and not email and not qty:
            error_message = "Do not leave text empty"
        
        if int(qty) < 1:
            error_message = "Order can not be less than 1"
        elif int(qty) == 12:
            error_message = "Please speak to the counter for free coffee"
        
        self.error_message.config(text=error_message)

    
    def pack(self):
        self.root.geometry("640x480")

        self.title.pack()
        self.first_name_label.pack()
        self.first_name.pack()
        self.last_name_label.pack()
        self.last_name.pack()
        self.email_label.pack()
        self.email.pack()
        self.qty_label.pack()
        self.qty.pack()
        self.error_message.pack()

        self.button.pack()

        self.error_message.configure(fg="red", font=("arial", 16))

        self.root.mainloop()

if __name__ == "__main__":
    john = Books()