from turtle import Turtle, Screen
import random


color_list = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

tim = Turtle()
tim.hideturtle()
screen = Screen()
tim.speed("fast")
screen.colormode(255)

def start():
    tim.penup()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)

def line():
    for i in range (10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

def position():
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.forward(-500)


def dots():
    for i in range (10):
        line()
        position()


start()
dots()
screen.exitonclick()