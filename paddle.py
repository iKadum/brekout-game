from turtle import Turtle

PADDLE_COLOR = "white"


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(PADDLE_COLOR)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)

    def reset_position(self):
        self.goto(0, -270)

    def new_position(self, x_cor):
        new_x = x_cor
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        if new_x > -430:
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        if new_x < 430:
            self.goto(new_x, self.ycor())
