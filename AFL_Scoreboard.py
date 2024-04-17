import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("AFL_Scoreboard")

currentScore1 = 0
currentScore2 = 0

def increaseScore1():
    global currentScore1
    currentScore1 = currentScore1 + 6
    Score1.configure(text = currentScore1)
    
def behindScore1():
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
    currentScore2 = currentScore2 + 6
    Score2.configure(text = currentScore2)

def behindScore2():
    global currentScore2
    currentScore2 = currentScore2 + 1
    Score2.configure(text = currentScore2)

def decreaseScore2():
    global currentScore2
    currentScore2 = currentScore2 - 1
    if currentScore2 < 0:
        messagebox.showerror("Error", "The score can only be positive")
        currentScore2 = 0
        Score2.configure(text = currentScore2)
    else:
        Score2.configure(text = currentScore2)

goalScoreButton1 = tk.Button(root, text="GOAL JOHNS", command=increaseScore1)
goalScoreButton1.grid(row=1, column=1, pady=20, padx=20)

goalScoreButton1 = tk.Button(root, text="BEHIND JOHNS", command=behindScore1)
goalScoreButton1.grid(row=2, column=1, pady=20, padx=20)

decreaseScoreButton1 = tk.Button(root, text="DECREASE JOHNS", command=decreaseScore1)
decreaseScoreButton1.grid(row=3, column=1, pady=20, padx=20)

increaseScoreButton2 = tk.Button(root, text="GOAL ETHANS", command=increaseScore2)
increaseScoreButton2.grid(row=1, column=10, pady=20, padx=20)

goalScoreButton2 = tk.Button(root, text="GOAL JOHNS", command=behindScore2)
goalScoreButton2.grid(row=2, column=10, pady=20, padx=20)

decreaseScoreButton2 = tk.Button(root, text="DECREASE ETHANS", command=decreaseScore2)
decreaseScoreButton2.grid(row=3, column=10, pady=20, padx=20)

Score1 = tk.Label(root)
Score1.grid(row=0, column=1, pady=20, padx=20)


Score2 = tk.Label(root)
Score2.grid(row=0, column=10, pady=20, padx=20)

exitButton = tk.Button(root, text="Exit", command=root.destroy)
exitButton.grid(sticky="se", column=10)

root.geometry("300x300")

root.mainloop()