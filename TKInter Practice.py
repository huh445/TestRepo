import tkinter as tk

root = tk.Tk()

currentScore1 = 0

root.title("Scoreboard")

def increaseScore1():
    global currentScore1
    currentScore1 = currentScore1 + 1
    Score1.configure(text = currentScore1)

def decreaseScore1():
    global currentScore1
    currentScore1 = currentScore1 - 1
    if currentScore1 < 0:
        print("The score can only be positive.")
        currentScore1 = 0
        Score1.configure(text = currentScore1)
    else:
        Score1.configure(text = currentScore1)

def resetScore():
    global currentScore1
    currentScore1 = 0
    Score1.configure(text=currentScore1)



Score1 = tk.Label(root)
Score1.pack()

increaseScoreButton = tk.Button(root, text="+", command=increaseScore1)
increaseScoreButton.pack()

decreaseScoreButton = tk.Button(root, text="-", command=decreaseScore1)
decreaseScoreButton.pack()

resetScoreButton = tk.Button(root, text="Reset Counter", command=resetScore)
resetScoreButton.pack()

increaseScoreButton.configure(width=5, height=2)
increaseScoreButton.config(bg="#000000",fg="#ffffff",font=("Arial",50))

decreaseScoreButton.configure(width=5, height=2)
decreaseScoreButton.config(bg="#000000",fg="#ffffff",font=("Arial",50))

resetScoreButton.config(bg="#000000",fg="#ffffff",font=("Arial",18))


root.geometry("640x480")
root.mainloop()
