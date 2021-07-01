from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Avery", 200, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,-100)
        self.l_score = 0
        self.r_score = 0
        self.color("gray")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.l_score} {self.r_score}", font=FONT, align=ALIGNMENT)


    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()