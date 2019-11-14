import turtle
import time
import random as rand
from constants import vw2, vh2, vh
from window import wn
from funktions import StartSeq

def Hard_Pong():
    start = time.time()

    #main loop
    while True:
        timeBegin = time.time()
        Now = timeBegin - start
        Now = (int(Now*10))/10
        wn.update()

        Timer.clear()
        Timer.write("{}".format(Now) , align="center", font=("Courier", 24, "normal"))

        #move the ball
        ball.dx *= 1.001
        ball.dy *= 1.001
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #border check
        if ball.ycor() > (vh2-20):
            ball.sety((vh2-20))
            ball.dy *= -1


        if ball.ycor() < -(vh2-20):
            ball.sety(-(vh2-20))
            ball.dy *= -1
        #ball point
        if ball.xcor() > (vw2-10):
            ball.goto(0, rand.randint(-(vh-50), (vh-50)))
            ball.dx = (rand.randint(2, 10)/10)
            ball.dy = 1 - ball.dx
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b) , align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -(vw2-10):
            ball.goto(0, rand.randint(-(vh-50), (vh-50)))
            ball.dx = (rand.randint(2, 2))
            ball.dy = 1 - ball.dx
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b) , align="center", font=("Courier", 24, "normal"))

        #paddle hit ball
        if (ball.xcor() < -(vw2-70)) and (ball.xcor() > -(vw2-50)) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-(vw2-70))
            ball.dx *= -1

        if (ball.xcor() > (vw2-70)) and (ball.xcor() < (vw2-50)) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40):
            ball.setx((vw2-70))
            ball.dx *= -1

        timeElapsed = time.time() - timeBegin
        if timeElapsed < 0.05:
            time.sleep(0.05 - timeElapsed)