from turtle import Turtle
import random

# Variables
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    # Attributes
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.penup()
        self.spawn()

    # Spawning
    def spawn(self):
        self.goto(300, random.randint(-260, 260))

    # movement
    def movement(self):
        self.goto(self.xcor() - MOVE_INCREMENT, self.ycor())