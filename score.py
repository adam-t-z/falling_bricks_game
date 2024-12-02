from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 350)
        self.points = 0
        self.write(f"SCORE: {self.points}", align="center", font=("courier", 25, "normal"))
    
    def update_score(self, added_points = 0, is_triangle=False):
        if is_triangle:
            self.points = 0
        self.clear()
        self.points += added_points
        self.write(f"SCORE: {self.points}", align="center", font=("courier", 25, "normal"))

    def game_over(self):
        self.color("white")
        self.write("Game Over", align="center", font=("arial", 40, "normal"))
        