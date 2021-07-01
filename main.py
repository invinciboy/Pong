from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from net import Net
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

scoreboard= Scoreboard()
ball = Ball()

y_cor = -300
for _ in range(0,31):
    new_net = Net((0,y_cor))
    y_cor += 20

screen.listen()
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

game_is_on = True
screen.tracer(1)


while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 360:
        scoreboard.increase_l_score()
        ball.reset_position()

    elif ball.xcor() < -360:
        scoreboard.increase_r_score()
        ball.reset_position()


screen.exitonclick()





