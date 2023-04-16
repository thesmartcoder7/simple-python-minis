from turtle import Screen
from paddle import Paddle
from ball import Ball, pause
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

ball = Ball()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
score = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        score.left_point()
        pause()

    if ball.xcor() < -400:
        ball.reset_position()
        score.right_point()
        pause()

screen.exitonclick()
