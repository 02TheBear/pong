import turtle
import time
from constants import vw, vh, vh2
from Hard_Pong import Hard_Pong
from Normal_Pong import Normal_Pong
from Players_Pong import Players_Pong
from window import wn

loop = 0

#Timer
start = time.time()

#Cursor
Cursor = turtle.Turtle()
Cursor.speed(0)
Cursor.shape("square")
Cursor.shapesize(stretch_wid=1, stretch_len=2)
Cursor.color("white")
Cursor.penup()
Cursor.goto(40, 0)

#Pong
Pong = turtle.Turtle()
Pong.speed(0)
Pong.color("white")
Pong.penup()
Pong.hideturtle()
Pong.goto(0, (vh2-100))
Pong.write("Pong", align="center", font=("Courier", 48, "bold"))

#3-Players
Players = turtle.Turtle()
Players.speed(0)
Players.color("white")
Players.penup()
Players.hideturtle()
Players.goto(-80, (vh2-220))
Players.write("3-Players", align="center", font=("Courier", 24, "normal"))

#Normal
Normal = turtle.Turtle()
Normal.speed(0)
Normal.color("white")
Normal.penup()
Normal.hideturtle()
Normal.goto(-55, (vh2-270))
Normal.write("Normal", align="center", font=("Courier", 24, "normal"))

#Hard
Hard = turtle.Turtle()
Hard.speed(0)
Hard.color("white")
Hard.penup()
Hard.hideturtle()
Hard.goto(-40, (vh2-320))
Hard.write("Hard", align="center", font=("Courier", 24, "normal"))

def Clear_items():
    #Remove old stuff
    global loop
    Pong.clear()
    Cursor.clear()
    Normal.clear()
    Hard.clear()
    Players.clear()
    wn.resetscreen()
    loop = 1

#Cursor
def Cursor_up():
    y = Cursor.ycor()
    if y < (vh2 -200):
        y += 50
        Cursor.sety(y)
    else:
        pass

def Cursor_down():
    y = Cursor.ycor()
    if y > (vh2 -300):
        y -= 50
        Cursor.sety(y)
    else:
        pass

def Start_game():
    y = Cursor.ycor()
    if y == (vh2 -200):
        #Remove old stuff
        Clear_items()
        Players_Pong()
        
    elif y == (vh2 -250):
        #Remove old stuff
        Clear_items()
        Normal_Pong()

    elif y == (vh2 -300):
        #Remove old stuff
        Clear_items()
        Hard_Pong()
    else:
        pass

    #keys
    wn.listen()
    #paddle a
    wn.onkeypress(Cursor_up, "o")   
    wn.onkeypress(Cursor_down, "l")
    wn.onkeypress(Start_game, "p")

    while loop == 0:
        wn.update()

    return Timer