from turtle import Turtle,Screen



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = .1




    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= .5

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= .9

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()




    # def left_serve(self):
    #     self.home()
    #     new_x = self.xcor() - self.x_move
    #     new_y = self.ycor() - self.y_move
    #     self.goto(new_x,new_y)
    #
    # def right_serve(self):
    #     self.home()
    #     new_x = self.xcor() + self.x_move
    #     new_y = self.ycor() + self.y_move
    #     self.goto(new_x,new_y)

