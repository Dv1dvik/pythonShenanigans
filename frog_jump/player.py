from turtle import Turtle

# Variables
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    # Attributes
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.restart()
        self.setheading(90)

    # Movement
    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    # Reset position
    def restart(self):
        self.goto(STARTING_POSITION)