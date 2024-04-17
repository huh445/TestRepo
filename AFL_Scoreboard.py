import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("AFL_Scoreboard")

currentScore1 = 0
currentscore2 = 0

def increaseScore1():
    global currentScore1
    currentScore1 = currentScore1 + 1
    Score1.configure(text = currentScore1)

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
    currentscore2 = 0
    Score1.configure(text=currentScore1)
    Score2.configure(text=currentScore2)

def increaseScore2():
    global currentScore2
    currentScore2 = currentScore2 + 1
    Score1.configure(text = currentScore2)


def decreaseScore2():
    global currentScore2
    currentScore2 = currentScore2 - 1
    if currentScore2 < 0:
        messagebox.showerror("Error", "The score can only be positive")
        currentScore2 = 0
        Score2.configure(text = currentScore2)
    else:
        Score2.configure(text = currentScore2)

increaseScoreButton1 = tk.Button(root, text="Increase The Johns by One", command=increaseScore1)
increaseScoreButton1.pack()

decreaseScoreButton1 = tk.Button(root, text="Decrease The Johns by One", command=decreaseScore1)
decreaseScoreButton1.pack()

increaseScoreButton2 = tk.Button(root, text="Increase The Ethans by One", command=increaseScore2)
increaseScoreButton2.pack()

decreaseScoreButton2 = tk.Button(root, text="Decrease The Ethans by One", command=decreaseScore2)
decreaseScoreButton2.pack()

Score1 = tk.Label(root)
Score1.pack()

Score2 = tk.Label(root)
Score2.pack()


root.geometry("800x800")

root.mainloop()