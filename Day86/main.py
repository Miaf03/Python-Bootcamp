import time
from ball import Ball
from brick import Brick
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Colorful Breakout Game")
screen.tracer(0)

paddle = Paddle((0, -250))
ball = Ball()
scoreboard = Scoreboard()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
bricks = []

y_start = 250
for color in colors:
    for x in range(-350, 400, 100):
        brick = Brick((x, y_start), color)
        bricks.append(brick)
    y_start -= 25

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_y()

    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.destroy()
            bricks.remove(brick)
            ball.bounce_y()
            scoreboard.add_point()

    if ball.ycor() < -300:
        scoreboard.lose_life()
        ball.reset_position()

        if scoreboard.lives == 0:
            scoreboard.game_over()
            game_is_on = False

    if not bricks:
        scoreboard.you_win()
        game_is_on = False

screen.mainloop()