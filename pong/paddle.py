from turtle import Turtle
# values
MOVEMENT = 50


class Paddle(Turtle):
    # Attributes
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(5, 1)
        self.penup()
        self.goto(position)

    # Move up
    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVEMENT)

    # Move down
    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVEMENT)