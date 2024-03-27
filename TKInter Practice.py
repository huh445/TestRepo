import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

currentScore1 = 0

root.title("...and be counted app")

def increaseScore1():
    global currentScore1
    currentScore1 = currentScore1 + 1
    Score1.configure(text = currentScore1)
    if currentScore1 > 200:
        capacityLabel.config(text="At capacity")
        messagebox.showerror("Error", "At capacity")
        currentScore1 = 201
        Score1.configure(text = currentScore1)
    else:
        capacityLabel.config(text="Not at capacity")

def decreaseScore1():
    global currentScore1
    currentScore1 = currentScore1 - 1
    if currentScore1 < 0:
        messagebox.showerror("Error", "The score can only be positive")
        currentScore1 = 0
        Score1.configure(text = currentScore1)
    else:
        Score1.configure(text = currentScore1)

def resetScore():
    global currentScore1
    currentScore1 = 0
    Score1.configure(text=currentScore1)

def cheatScore():
    global currentScore1
    currentScore1 = 199
    Score1.configure(text = currentScore1)


increaseScoreButton = tk.Button(root, text="+", command=increaseScore1)
increaseScoreButton.pack()

Score1 = tk.Label(root)
Score1.pack()

decreaseScoreButton = tk.Button(root, text="-", command=decreaseScore1)
decreaseScoreButton.pack()

resetScoreButton = tk.Button(root, text="RESET COUNTER", command=resetScore)
resetScoreButton.pack()

NWAlignedLabel = tk.Label(root, text="...and be counted app")
NWAlignedLabel.pack(anchor="nw")

exitButton = tk.Button(root, text="Exit", command=root.destroy)
exitButton.pack(anchor="se", side="bottom")

headingLabel = tk.Label(root, text="...and be counted app")
headingLabel.pack(anchor="center")

subHeadingLabel = tk.Label(root, text="App that counts the number of poeple entering the stand")
subHeadingLabel.pack(anchor="center")

capacityLabel = tk.Label(root, text="Not at capacity")
capacityLabel.pack(anchor="center")

cheatButton = tk.Button(root, text="YEP CUM", command=currentScore1)
cheatButton.pack()


increaseScoreButton.configure(width=5, height=2)
increaseScoreButton.config(bg="#000000",fg="#ffffff",font=("Arial",50))

decreaseScoreButton.configure(width=5, height=2)
decreaseScoreButton.config(bg="#000000",fg="#ffffff",font=("Arial",50))

resetScoreButton.config(bg="#000000",fg="#ffffff",font=("Arial",18))

Score1.configure(width=7, height=2)
Score1.config(fg="#000000",font=("Arial",50), borderwidth=1, relief="solid")

exitButton.config(bg="#000000", fg="#ffffff", font=("Arial"))

NWAlignedLabel.config(fg="#000000",font=("Arial",10))

headingLabel.config(font=("Arial",18))

subHeadingLabel.config(font=("Arial", 10))

capacityLabel.config(font=("Arial", 18), anchor="center")

increaseScoreButton.place(x=850, y=200)
decreaseScoreButton.place(x=200, y=200)
Score1.place(x=500, y=200)
resetScoreButton.place(x=525, y=425)
capacityLabel.place(x=550,y=150)

root.geometry("1280x720")
root.mainloop()
