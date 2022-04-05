import time
from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.level = 1
        self.balls = 3
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}\tLEVEL: {self.level}\tBALL: {self.balls}", align="center", font=FONT)

    def miss_ball(self):
        self.balls -= 1
        self.write_score()

    def hit_brick(self):
        self.score += 10
        self.write_score()

    def next_level(self):
        self.level += 1
        self.goto(0, -45)
        self.write("NEXT LEVEL", align="center", font=("Courier", 90, "normal"))
        time.sleep(1)
        self.goto(0, 270)
        self.write_score()

    def game_over(self):
        self.goto(0, -45)
        self.write("GAME OVER", align="center", font=("Courier", 90, "normal"))

