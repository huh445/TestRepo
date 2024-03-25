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


increaseScoreButton = tk.Button(root, text="+", command=increaseScore1)
increaseScoreButton.pack()

Score1 = tk.Label(root)
Score1.pack()

decreaseScoreButton = tk.Button(root, text="-", command=decreaseScore1)
decreaseScoreButton.pack()

resetScoreButton = tk.Button(root, text="RESET COUNTER", command=resetScore)
resetScoreButton.pack()

increaseScoreButton.configure(width=5, height=2)
increaseScoreButton.config(bg="#000000",fg="#ffffff",font=("Arial",50))

decreaseScoreButton.configure(width=5, height=2)
decreaseScoreButton.config(bg="#000000",fg="#ffffff",font=("Arial",50))

resetScoreButton.config(bg="#000000",fg="#ffffff",font=("Arial",18))

Score1.config(fg="#000000",font=("Arial",50), borderwidth=1, relief="solid")

increaseScoreButton.place(x=300, y=100)
decreaseScoreButton.place(x=750, y=100)

root.geometry("1280x720")
root.mainloop()
