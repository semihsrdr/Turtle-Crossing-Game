from turtle import Turtle

class Character(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.sety(-375)
        self.shapesize(1.5,1.5,1.5)
        self.setheading(90)
        self.x_move=5
        self.y_move=5


    def go_up(self):
        self.sety(self.ycor()+self.y_move)

    def go_down(self):
        self.sety(self.ycor()-self.y_move)

    def go_right(self):
        self.setx(self.xcor()+self.y_move)

    def go_left(self):
        self.setx(self.xcor()-self.y_move)

    def reset_position(self):
        self.sety(-375)
        self.setx(0)

    def next_level(self,writer):
        if self.ycor()>400:
            print("new level")
            self.reset_position()
            writer.level+=1
            writer.update_level()
            return True


