import time
from turtle import Screen
from car import Car
from character import Character
from writer import Writer

screen=Screen()
screen.setup(1024,800)
screen.title("Turtle Crossing")
screen.bgcolor("gray")
screen.tracer(0)

my_turtle=Character()
writer=Writer()

cars=[]
for i in range(30):
    car=Car()
    cars.append(car)

screen.listen()
screen.onkeypress(my_turtle.go_up,"Up")
screen.onkeypress(my_turtle.go_down,"Down")
screen.onkeypress(my_turtle.go_right,"Right")
screen.onkeypress(my_turtle.go_left,"Left")


game_on=True
while game_on:
    time.sleep(0.01)
    screen.update()
    for i in cars:
        i.move_car()
        if i.xcor()<-550:
            i.go_start()
        if my_turtle.next_level(writer):
            for j in cars:
                j.speed_up()

        if i.hit_turtle(my_turtle)==False:
            game_on=False
            writer.death_animation()
            time.sleep(0.2)
            for j in cars:
                j.hideturtle()
            my_turtle.reset_position()
            screen.update()
            writer.game_over()
            break





screen.exitonclick()