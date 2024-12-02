from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.goto(0,-350)


    def move_right(self):
        if self.xcor() + 40 < 500:
            self.goto( self.xcor() + 40, -350 )

    def move_left(self):
        if self.xcor() - 40 > -500:
            self.goto( self.xcor() - 40, -350 )