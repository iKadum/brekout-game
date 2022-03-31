from turtle import Turtle


class Brick(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(x, y)
        self.exist = True

    def disappear(self):
        self.color("black")
        self.exist = False
