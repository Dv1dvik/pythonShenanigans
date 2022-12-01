from turtle import Screen
from paddle import Paddle
from ball import  Ball
from scoreboard import Scoreboard
import time

# Screen settings
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()

# Right paddle controls
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# Left paddle controls
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# BALL and scoreboard
ball = Ball()
scoreboard = Scoreboard()

# Game loop
game_on = True
while game_on:
    time.sleep(ball.move_sped)
    screen.update()
    ball.move()

    # Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < - 335:
        ball.bounce_x()

    # Detecting Right paddle misses
    if ball.xcor() > 380:
        ball.reverse()
        scoreboard.l_point()

    # Detecting Left paddle misses
    if ball.xcor() < -380:
        ball.reverse()
        scoreboard.r_point()

screen.exitonclick()