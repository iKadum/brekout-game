from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
import time

INITIAL_BRICK = (-353, 270)  # position of the upper left first brick


def reset():
    ball.reset_position()
    paddle.reset_position()
    screen.update()
    time.sleep(0.5)


def destroy_brick(bri):
    global no_of_bricks
    bri.disappear()
    ball.move_speed *= 0.99  # ball moves faster
    no_of_bricks -= 1
    print(no_of_bricks)  # DEBUG


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()


bricks = {}  # create bricks in a dictionary
x_cor, y_cor = INITIAL_BRICK
for y in range(5):  # 5 brick rows
    for x in range(11):  # 11 bricks in every row
        bricks[f"brick_{x}_{y}"] = Brick(x_cor, y_cor)  # every Brick object has its own name - brick_x_y
        x_cor += 70  # new brick 70 px on the right
    x_cor, _ = INITIAL_BRICK  # reset x to first column
    y_cor -= 30  # new row 30 px down

no_of_bricks = len(bricks)
print(no_of_bricks)

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

reset()

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    # ball hits right or left wall
    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.bounce_x()

    # ball hits top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # ball hits paddle
    if -255 < ball.ycor() < -245 and ball.distance(paddle) < 65 and ball.going_up is False:
        ball.bounce_y()

    # ball falls down
    if ball.ycor() < -290:
        reset()

    # ball hits brick
    for brick in bricks:
        if ball.distance(bricks[brick]) < 55 and abs(bricks[brick].ycor() - ball.ycor()) < 5:  # ball hits side
            ball.bounce_x()
            destroy_brick(bricks[brick])
            break
        if ball.distance(bricks[brick]) < 40 and abs(bricks[brick].ycor() - ball.ycor()) < 35:
            ball.bounce_y()
            destroy_brick(bricks[brick])
            break

    # last brick is destroyed
    if no_of_bricks < 1:
        game_is_on = False


print("GAME OVER")

screen.exitonclick()
