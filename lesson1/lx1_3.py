from turtle import *
from random import *

def runstar():
    screensize(600,400)
    n = randint(5,20)
    for i in range(1,n+1):
        up()
        x=randint(-300,300)
        y=randint(-200,200)
        goto(x,y)
        down()
        pencolor(random(),random(),random())
        pensize(randint(1,10))
        angle=randint(6,18)
        step=randint(50,200)
        for j in range(1,angle+1):
            forward(step)
            goto(x, y)
            left(360/angle)

if __name__=='__main__':
    runstar()