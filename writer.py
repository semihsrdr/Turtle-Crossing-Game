import time
from turtle import Turtle,Screen

class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-450,350)
        self.level = 1
        self.write(f"Level {self.level}",False,"center",font=("Arial",20,"normal"))

    def update_level(self):
        self.clear()
        self.write(f"Level {self.level}", False, "center", font=("Arial", 20, "normal"))

    def death_animation(self):
        Screen().bgcolor("red")
        time.sleep(0.2)
        Screen().bgcolor("gray")

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over", False, "center", font=("Arial", 50, "bold"))
