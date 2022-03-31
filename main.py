from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
import time

INITIAL_BRICK = (-354, 270)


def reset():
    ball.reset_position()
    paddle.reset_position()
    screen.update()
    time.sleep(0.5)


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()

bricks = {}
x_cor, y_cor = INITIAL_BRICK
for y in range(5):
    for x in range(11):
        bricks[f"brick_{x}_{y}"] = Brick(x_cor, y_cor)
        x_cor += 70
    x_cor, _ = INITIAL_BRICK
    y_cor -= 30


screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

reset()

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(paddle) < 45 and ball.ycor() < -245:
        ball.move_speed *= 0.99
        print(ball.move_speed)
        ball.bounce_y()

    for brick in bricks:
        if ball.distance(bricks[brick]) < 60 and ball.ycor() > (bricks[brick].ycor() - 30) and bricks[brick].exist is True:
            bricks[brick].disappear()
            ball.bounce_y()

    if ball.ycor() < -290:
        reset()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()



# screen.exitonclick()
