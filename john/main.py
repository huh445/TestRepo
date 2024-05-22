import tkinter as tk
import tkinter.ttk as ttk
from scoring import Scoring

class ScoringApp:
    def __init__(self, root, scoring):
        self.root = root
        style = ttk.Style()
        self.scoring = scoring

        style.theme_use("alt")

        style.configure("TButton", background="#587b7f", foreground="#D3D0CB", font="Abel", relief="flat")
        style.map("TButton", background=[("active", "#E2C044")])

        style.configure("TLabel", background="#393e41", foreground="#D3D0CB", font="Abel 12")

        self.p1ScoresLabel = ttk.Label(self.root, style="TLabel")
        self.p2ScoresLabel = ttk.Label(self.root, style="TLabel")
        
        self.p1ScoreIncrease = ttk.Button(self.root, style="TButton", text="Increase Player 1 Points by 1", command=lambda: self.scoring.p1Scores())
        self.p1ScoreDecrease = ttk.Button(self.root, style="TButton", text="Decrease Player 1 Points by 1", command=lambda: self.scoring.p1Decrease())

        self.p2ScoreIncrease = ttk.Button(self.root, style="TButton", text="Increase Player 2 Points by 1", command=lambda: self.scoring.p2Scores())
        self.p2ScoreDecrease = ttk.Button(self.root, style="TButton", text="Decrease Player 2 Score by 1", command=lambda: self.scoring.p2Decrease())

        self.resetButton = ttk.Button(self.root, style="TButton", text="Reset Scores", command=self.scoring.reset)
        self.update()
        self.layout()
        
    def update(self):
        self.p1ScoresLabel.config(text=f"Points: {self.scoring.p1Points}, Games: {self.scoring.p1Games}, Sets: {self.scoring.p1Sets}")
        self.p2ScoresLabel.config(text=f"Points: {self.scoring.p2Points}, Games: {self.scoring.p2Games}, Sets: {self.scoring.p2Sets}")

    def layout(self):
        self.root.title("Table Tennis Scoring App")
        self.root.geometry("300x325")
        self.root.config(bg="#393e41")

        self.p1ScoresLabel.pack(pady=5)
        self.p1ScoreIncrease.pack(pady=5)
        self.p1ScoreDecrease.pack(pady=5)
        self.p2ScoresLabel.pack(pady=5)
        self.p2ScoreIncrease.pack(pady=5)
        self.p2ScoreDecrease.pack(pady=5)
        self.resetButton.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    scoring = Scoring(None)  # Pass None initially
    app = ScoringApp(root, scoring)
    scoring.app = app  # Assign the ScoringApp instance to the Scoring class
    root.mainloop()
