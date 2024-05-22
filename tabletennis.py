import tkinter
import tkinter.ttk as ttk

class ScoringApp:
    def __init__(self, root):
        self.root = root
        style = ttk.Style()
        style.theme_use(None)
        self.p1Points = 0
        self.p2Points = 0
        self.p1Games = 0
        self.p2Games = 0
        self.p1Sets = 0
        self.p2Sets = 0
        style.theme_use("alt")
        style.configure("TButton", background="#587b7f", foreground="#D3D0CB", font="Abel", relief="flat")
        style.map("TButton", background=[("active", "#E2C044")])

        style.configure("TLabel", background="#393e41", foreground="#D3D0CB", font=("Abel 12"))

        # Create score labels
        self.p1ScoresLabel = ttk.Label(self.root, style="TLabel")
        self.p2ScoresLabel = ttk.Label(self.root, style="TLabel")
        
        self.p1ScoreIncrease = ttk.Button(self.root, style="TButton", text="Increase Player 1 Points by 1", command=self.p1Scores)
        
        self.p2ScoreIncrease = ttk.Button(self.root, text="Increase Player 2 Points by 1", command=self.p2Scores, style="TButton")

        self.layout()  # Call pack in init to set window properties
    
    def p1Scores(self):
        self.p1Points += 1
        if self.p1Points >= 11 and (self.p1Points - self.p2Points) >= 2:
            self.p1Games += 1
            self.p1Points = 0
            self.p2Points = 0
        if self.p1Games >= 3:
            self.p1Sets += 1
            self.p1Points = 0
            self.p1Games = 0
            self.p2Points = 0
            self.p2Games = 0
        self.update()
    def p2Scores(self):
        self.p2Points += 1
        if self.p2Points >= 11 and (self.p2Points - self.p1Points) >= 2:
            self.p2Games += 1
            self.p2Points = 0
            self.p1Points = 0
        if self.p2Games >= 3:
            self.p2Sets += 1
            self.p2Points = 0
            self.p2Games = 0
            self.p1Points = 0
            self.p1Games = 0
        self.update()
    def update(self):
        self.p1ScoresLabel.config(text=f"Points: {self.p1Points}, Games: {self.p1Games}, Sets: {self.p1Sets}")
        self.p2ScoresLabel.config(text=f"Points: {self.p2Points}, Games: {self.p2Games}, Sets: {self.p2Sets}")
    def layout(self):
        self.root.title("Table Tennis Scoring App")
        self.root.geometry("300x200")
        self.root.config(bg="#393e41")

        # Pack the labels and buttons
        self.p1ScoresLabel.pack(pady=5)
        self.p1ScoreIncrease.pack(pady=5)
        self.p2ScoresLabel.pack(pady=5)
        self.p2ScoreIncrease.pack(pady=5)
        self.update()

if __name__ == "__main__":
    root = tkinter.Tk()
    app = ScoringApp(root)
    root.mainloop()