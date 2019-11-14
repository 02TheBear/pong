import time
import turtle
from constants import vw2, vh2
from window import wn

#start sequense
def StartSeq():
    score_a = 0
    score_b = 0

    #platta a
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.color("white")
    paddle_a.penup()
    paddle_a.goto(-(vw2 - 50),0)

    #platta b
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.color("white")
    paddle_b.penup()
    paddle_b.goto((vw2 - 50),0)

    #boll
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0,0)
    ball.dx = 3
    ball.dy = 3

    #pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, (vh2-40))
    pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

    #Timer
    Timer = turtle.Turtle()
    Timer.speed(0)
    Timer.color("white")
    Timer.penup()
    Timer.hideturtle()
    Timer.goto(0, -(vh2-40))
    Timer.write("0", align="center", font=("Courier", 24, "normal"))
        #funktion
    #Paddle a
    def paddle_a_up():
        y = paddle_a.ycor()
        if y < (vh2 -40):
            y += 40
            paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        if y > -(vh2 -40):
            y -= 40
        paddle_a.sety(y)

    #Paddle b
    def paddle_b_up():
        y = paddle_b.ycor()
        if y < (vh2 -40):
            y += 40
            paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        if y > -(vh2 -40):
            y -= 40
            paddle_b.sety(y)

    #keys
    wn.listen()
    #paddle a
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    #paddel b
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")
