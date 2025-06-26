class Scoring:
    def __init__(self, app):
        self.app = app
        self.p1Points, self.p1Games, self.p1Sets = 0, 0, 0
        self.p2Points, self.p2Games, self.p2Sets = 0, 0, 0

    def reset(self):
        self.p1Points, self.p1Games, self.p1Sets = 0, 0, 0
        self.p2Points, self.p2Games, self.p2Sets = 0, 0, 0
        self.app.update()

    def p1Scores(self):
        self.p1Points += 1
        if self.p1Points >= 11 and (self.p1Points - self.p2Points) >= 2:
            self.p1Games += 1
            self.p1Save, self.p2Save = self.p1Points, self.p2Points
            self.p1Points, self.p2Points = 0, 0
            
        if self.p1Games >= 3:
            self.p1Sets += 1
            self.p1Points, self.p2Points, self.p1Games, self.p2Games = 0, 0, 0, 0
        self.app.update()

    def p1Decrease(self):
        self.p1Points -= 1
        if self.p1Points < 0:
            self.p1Points = 0
            if self.p1Sets >= 1:
                self.p1Sets -= 1
                self.p1Games = 2
                self.p1Points, self.p2Points = self.p1Save - 1, self.p2Save
            elif self.p1Games >= 1:
                self.p1Games -= 1
                self.p1Points, self.p2Points = self.p1Save - 1, self.p2Save
        self.app.update()

    def p2Scores(self):
        self.p2Points += 1
        if self.p2Points >= 11 and (self.p2Points - self.p1Points) >= 2:
            self.p2Games += 1
            self.p1Points, self.p2Points = 0, 0
            self.p1Save, self.p2Save = self.p1Points, self.p2Points
        if self.p2Games >= 3:
            self.p2Sets += 1
            self.p1Points, self.p2Points, self.p1Games, self.p2Games = 0, 0, 0, 0
        self.app.update()

    def p2Decrease(self):
        self.p2Points -= 1
        if self.p2Points < 0:
            self.p2Points = 0
            if self.p2Sets >= 1:
                self.p2Sets -= 1
                self.p2Games = 2
                self.p1Points, self.p2Points = self.p1Save - 1, self.p2Save
            elif self.p2Games >= 1:
                self.p2Games -= 1
                self.p1Points, self.p2Points = self.p1Save - 1, self.p2Save
        self.app.update()