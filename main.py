from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

INITIAL_BRICK = (-353, 240)  # position of the upper left first brick



def reset():
    ball.reset_position()
    paddle.reset_position()
    screen.update()
    time.sleep(0.5)


def create_bricks():
    bricks_ = {}
    x_cor, y_cor = INITIAL_BRICK
    for _y in range(scoreboard.level + 5):  # every level more rows
        for _x in range(11):  # 11 bricks in every row
            bricks_[f"brick_{_x}_{_y}"] = Brick(x_cor, y_cor)  # every Brick object has its own name - brick_x_y
            x_cor += 70  # new brick 70 px on the right
        x_cor, _ = INITIAL_BRICK  # reset x to first column
        y_cor -= 30  # new row 30 px down

    return bricks_, y_cor


def destroy_brick(bri):
    bri.disappear()
    scoreboard.hit_brick()
    del bri
    # ball.move_speed *= 0.99  # ball moves faster
    # print(ball.move_speed)  # DEBUG


# create screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)
canvas = screen.getcanvas()

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

bricks, lower_brick = create_bricks()  # function returns bricks dictionary and the y of the last brick

# # move paddle with keyboard
# screen.listen()
# screen.onkeypress(paddle.move_left, "Left")
# screen.onkeypress(paddle.move_right, "Right")

reset()

game_is_on = True
while game_is_on:
    if scoreboard.balls < 1:
        game_is_on = False
        break

    # # move paddle with mouse
    # canvas = screen.getcanvas()
    # x = canvas.winfo_pointerx() - canvas.winfo_rootx() - 400
    x, y = ball.pos()
    paddle.new_position(x)

    ball.move()
    time.sleep(ball.move_speed)
    screen.update()

    # ball hits right or left wall
    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.bounce_x()

    # ball hits top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # ball hits paddle
    if -255 < ball.ycor() < -245 and ball.distance(paddle) < 65 and ball.going_up is False:
        ball.bounce_y()

        # # change ball movement angle if hit edge of paddle
        # if ball.distance(paddle) > 40:
        #     ball.x_step += 1
        # if ball.distance(paddle) > 50:
        #     ball.x_step += 1
        # if ball.distance(paddle) > 55:
        #     ball.x_step += 1

        # print(ball.x_step, ball.y_step)  # DEBUG

    # ball falls down
    if ball.ycor() < -290:
        scoreboard.miss_ball()
        reset()

    # ball hits brick
    if ball.ycor() > lower_brick:  # don't do for loop unnecessary
        # print(ball.ycor(), lower_brick)  # DEBUG
        for brick in bricks:
            if ball.distance(bricks[brick]) < 55 and abs(bricks[brick].ycor() - ball.ycor()) < 5:  # ball hits side
                ball.bounce_x()
                destroy_brick(bricks[brick])
                bricks.pop(brick, None)
                # print(bricks)  # DEBUG
                break
            if ball.distance(bricks[brick]) < 40 and abs(bricks[brick].ycor() - ball.ycor()) < 35:
                ball.bounce_y()
                destroy_brick(bricks[brick])
                bricks.pop(brick, None)
                # print(bricks)  # DEBUG
                break

    # print(ball.x_step)  # DEBUG

    # last brick is destroyed
    no_of_bricks = len(bricks)
    if no_of_bricks < 1:
        screen.update()
        ball.move_speed *= 0.5
        scoreboard.next_level()
        bricks, lower_brick = create_bricks()
        no_of_bricks = len(bricks)
        reset()


scoreboard.game_over()

screen.exitonclick()
