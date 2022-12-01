from turtle import  Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    # Attributes
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.c_speed = 0.1
        self.level = 0
        self.level_incrase()

    # level up
    def level_incrase(self):
        self.c_speed *= 0.7
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    # GAME OVER!
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!",  align="center", font=FONT)