from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# Screen
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

# Variables
player = Player()
scoreboard = Scoreboard()
cars = []

# player controls
screen.onkey(player.move, "Up")


# Game loop
game_on = True
num = 0
while game_on:
    time.sleep(scoreboard.c_speed)
    screen.update()

    # creating new car
    if num == 5:
        car = CarManager()
        cars.append(car)
        num = 0

    # moving cars
    for car in cars:
        car.movement()
        # Checking collision
        if player.distance(car) < 24:
            scoreboard.game_over()
            game_on = False

    # Increase level
    if player.ycor() > FINISH_LINE_Y:
        scoreboard.level_incrase()
        player.restart()

    num += 1


screen.exitonclick()
