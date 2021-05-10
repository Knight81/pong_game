from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

RIGHT_PADDLE_POSITION = (350, 0)
LEFT_PADDLE_POSITION = (-350, 0)

screen = Screen()
screen.title("Pong game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_right = Paddle(RIGHT_PADDLE_POSITION)
paddle_left = Paddle(LEFT_PADDLE_POSITION)
ball = Ball()
screen.update()

screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

screen.exitonclick()
