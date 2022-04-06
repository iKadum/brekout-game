from turtle import Turtle
import random

BRICK_COLORS = ["white", "red", "green", "blue", "yellow", "orange"]


class Brick(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(random.choice(BRICK_COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(x, y)

    def disappear(self):
        self.goto(1000, 1000)
