from turtle import Turtle
import random
colors=["blue","green","black","white","yellow"]
def random_y():
    random_y=random.randint(-325,400)
    return random_y
def random_x():
    random_x=random.randint(500,1500)
    return random_x
class Car(Turtle):
    def __init__(self):
        super().__init__("square")
        self.move_x=-2
        self.shapesize(1,2)
        self.color(random.choice(colors))
        self.penup()
        self.goto(random_x(),random_y())

    def move_car(self):
        self.setx(self.xcor()+self.move_x)

    def create_cars(self):
        for i in range(20):
            car=Car()
            return car

    def go_start(self):
        self.setx(500)
        self.sety(random_y())


    def hit_turtle(self, turtle):
        if self.distance(turtle)<20:
            return False

    def speed_up(self):
        self.move_x -= 0.40