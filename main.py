from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
maxScore = screen.textinput("Score", "First to... | Default is 5 | Type 'inf' for Infinite")
check = True

try:
    maxScore = int(maxScore)
except ValueError:
    if maxScore == "inf":
        maxscore = 0
        check = False
    else:
        maxScore = 5

r_paddle = Paddle(0)
l_paddle = Paddle(1)
ball = Ball()
leftscore = Scoreboard(-75)
rightscore = Scoreboard(50)

screen.listen()
screen.onkey(key="Up", fun=r_paddle.moveUp)
screen.onkey(key="Down", fun=r_paddle.moveDown)
screen.onkey(key="w", fun=l_paddle.moveUp)
screen.onkey(key="s", fun=l_paddle.moveDown)

while True:
    ball.move()
    screen.update()

    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce("x")
        ball.speed()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("y")
    if ball.xcor() > 380:
        ball.reset()
        leftscore.add_score()
    if ball.xcor() < -380:
        ball.reset()
        rightscore.add_score()

    if check:
        if leftscore.score >= maxScore:
            print("Left Wins!")
            screen.bye()
        if rightscore.score >= maxScore:
            print("Right Wins!")
            screen.bye()  

    sleep(0.1)

screen.exitonclick()