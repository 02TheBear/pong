import turtle
import time
import random as rand
from constants import vw2, vh2, vh
from window import wn
from funktions import StartSeq

def Players_Pong():
    start = time.time()

    StartSeq()

    #ball
    def ball_up():
        y = ball.ycor()
        y += 4
        ball.sety(y)

    def ball_down():
        y = ball.ycor()
        y -= 4
        ball.sety(y)

    def ball_right():
        x = ball.xcor()
        x += 1
        ball.setx(x)

    def ball_left():
        x = ball.xcor()
        x -= 1
        ball.setx(x)

    #ball
    wn.onkeypress(ball_up, "u")
    wn.onkeypress(ball_down, "j")
    wn.onkeypress(ball_left, "h")
    wn.onkeypress(ball_right, "k")

    #main loop
    while True:
        score_a = 0
        score_b = 0
        timeBegin = time.time()
        Now = timeBegin - start
        Now = (int(Now*10))/10
        wn.update()

        Timer.clear()
        Timer.write("{}".format(Now) , align="center", font=("Courier", 24, "normal"))

        #time -b point
        now = time.time()
        if start + 30 < now:
            start = time.time()
            score_b -= 1
            pen.clear()
            pen.write("Player A: {} Player B: {} Player C: {}".format(score_a, score_b, score_c) , align="center", font=("Courier", 24, "normal"))
        else:
            pass

        #move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #border check
        if ball.ycor() > (vh2-10):
            ball.sety((vh2-10))
            ball.dy *= -1

        if ball.ycor() < -(vh2-10):
            ball.sety(-(vh2-10))
            ball.dy *= -1

        if ball.xcor() > (vw2-10):
            ball.goto(0, rand.randint(-(vh-50), (vh-50)))
            ball.dx = (rand.randint(1, 10)/10)
            ball.dy = 1 - ball.dx
            ball.dx *= -1
            score_a += 1
            score_b += 1
            pen.clear()
            pen.write("Player A: {} Player B: {} Player C: {}".format(score_a, score_b, score_c) , align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -(vw2-10):
            ball.goto(0, rand.randint(-(vh-50), (vh-50)))
            ball.dx = (rand.randint(1, 2))
            ball.dy = 1 - ball.dx
            ball.dx *= -1
            score_c += 1
            score_b += 1
            pen.clear()
            pen.write("Player A: {} Player B: {} Player C: {}".format(score_a, score_b, score_c) , align="center", font=("Courier", 24, "normal"))

        #paddle hit ball
        if (ball.xcor() < -(vw2-60)) and (ball.xcor() > -(vw2-50)) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-(vw2-60))
            ball.dx *= -1

        if (ball.xcor() > (vw2-60)) and (ball.xcor() < (vw2-50)) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40):
            ball.setx((vw2-60))
            ball.dx *= -1

        timeElapsed = time.time() - timeBegin
        if timeElapsed < 0.05:
            time.sleep(0.05 - timeElapsed)