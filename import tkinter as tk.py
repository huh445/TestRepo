import tkinter as tk

root = tk.Tk()

currentScore1 = 0
currentScore2 = 0

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



Score1 = tk.Label(root)
Score1.pack()

increaseScore1Button = tk.Button(root, text="Increase Score 1 By 1", command=increaseScore1)
increaseScore1Button.pack()

decreaseScore1Button = tk.Button(root, text="Decrease Score 1 By 1", command=decreaseScore1)
decreaseScore1Button.pack()

def increaseScore2():
    global currentScore2
    currentScore2 =+ 1
    Score2.configure(text = currentScore2)
def decreaseScore2():
    global currentScore2
    currentScore2 = currentScore2 - 1
    if currentScore2 < 0:
        print("The score can only be positive.")
        currentScore2 = 0
        Score2.configure(text = currentScore2)
    else:
        Score2.configure(text = currentScore2)



Score2 = tk.Label(root)
Score2.pack()

increaseScore2Button = tk.Button(root, text="Increase Score 2 By 1", command=increaseScore2)
increaseScore2Button.pack()

decreaseScore2Button = tk.Button(root, text="Decrease Score 2 By 1", command=decreaseScore2)
decreaseScore2Button.pack()


root.geometry("640x480")
root.mainloop()
