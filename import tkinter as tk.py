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

increaseScore1Button = tk.Button(root, text="Increase Score 1 By 1", command=increaseScore1)
increaseScore1Button.pack()

decreaseScore1Button = tk.Button(root, text="Decrease Score 1 By 1", command=decreaseScore1)
decreaseScore1Button.pack()

resetScore1 = tk.Button(root, text="Reset", command=resetScore)
resetScore1.pack()

root.geometry("640x480")
root.mainloop()
