from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("grey")
        self.penup()
        self.x_step = 10
        self.y_step = 10
        self.move_speed = 0.03
        self.going_up = True
        self.going_right = True

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, -250)
        self.x_step = 10
        self.y_step = 10
        self.going_up = True
        self.going_right = True

    def bounce_y(self):
        if self.going_up is True:
            self.going_up = False
        else:
            self.going_up = True
        self.y_step *= -1
        print("bounce Y")  # debug

    def bounce_x(self):
        if self.going_right is True:
            self.going_right = False
        else:
            self.going_right = True
        self.x_step *= -1
        print("bounce X")  # debug
