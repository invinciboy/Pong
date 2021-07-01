from turtle import Turtle

Y_COR = 30

class Net(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("gray")
        self.shapesize(stretch_wid=.5, stretch_len=.2)
        self.penup()
        self.goto(position)