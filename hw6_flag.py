################################################################################
# HW6, CS103 Fall 2018 Johnstone
# name: Alison Rocco
# blazerid: arocco
################################################################################

from turtle import *
import random
# if you prefer, you may replace this import with:
# from turtle import *
# which will allow you to use left rather than turtle.left

# please add other functions to help you divide and conquer this problem
# (thought exercise: what basic units of code do you reuse several times?)
# (thought exercise: what basic units of code have a clean semantic meaning?)

def flagOutline (w, x, y):
    speed(0)
    up()
    goto(x,y)
    down()
    pencolor("black")
    for c in range(4):
        forward(w)
        left(90)

def flagA ():
    up()
    goto(x,y)
    down()
    color("white")
    begin_fill()
    for c in range(2):
        forward(w/2)
        left(90)
        forward(w)
        left(90)
    end_fill()

    up()
    goto(x+w/2,y)
    down()
    color("blue")
    begin_fill()
    for c in range(2):
        forward(w/2)
        left(90)
        forward(w)
        left(90)
    end_fill()

    up()
    goto(x+w, y)
    down()
    color("light grey")
    begin_fill()
    for c in range(1):
        left(120)
        forward(w/1.8)
        right(60)
        forward(w/1.8)
        left(-60)
    end_fill()
    flagOutline(w,x,y)
  
def flagP():
    up()
    goto(x1, y1)
    down()
    fillcolor("blue")
    begin_fill()
    for c in range(4):
        forward(w)
        left(90)
    end_fill()
    up()
    goto(x1+w/3, y1)
    left(90)
    forward(w/3)
    right(90)
    down()
    fillcolor("white")
    begin_fill()
    for c in range(4):
        forward(w/3)
        left(90)
    end_fill()
    flagOutline(w, x1, y1)

def flagR():
    up()
    goto(x2, y2)
    down()
    fillcolor("yellow")
    begin_fill()
    for c in range(4):
        forward(w)
        left(90)
    end_fill()
    def redSquare():
        color("red")
        begin_fill()
        for c in range(4):
            forward(w/2.5)
            left(90)
        end_fill()

    redSquare()
    forward(w/2.5 + w/5)
    redSquare()
    forward(w/2.5)
    left(90)
    forward(w/2.5 + w/5)
    redSquare()
    forward(w/2.5)
    left(90)
    forward(w/2.5 + w/5)
    redSquare()
    left(180)
    flagOutline(w, x2, y2)
    done()


w = random.randint(100,200)
x = random.randint(-200,0)
y = random.randint(-200,0)
flagOutline(w, x, y)

print("The result of flagA")
flagA()

s = random.randint(1,11)
x1 = (x+w) + s
y1 = y
print("The result of flagP")
flagP()

x2 = (x1+w) + s
y2 = y
print("The result of flagR")
flagR()