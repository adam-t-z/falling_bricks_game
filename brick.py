from turtle import Turtle
import random

SHAPES = ["square", "circle", "turtle", "triangle"]
COLORS = ["white", "green", "red", "orange", "purple"]

class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.random_turtle()
        self.ymove = 10
    
    def go_down(self):
        self.goto( self.xcor(), self.ycor() - self.ymove )

    def random_turtle(self):
        self.shape(random.choice(SHAPES))
        self.color(random.choice(COLORS))
        random_size = random.uniform(0.5,2)
        self.shapesize(random_size, random_size )
        self.goto(random.randint(-350,350), 400)
    
