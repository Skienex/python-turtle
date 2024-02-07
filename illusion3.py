from turtle import *

def draw(size):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    speed(10)
    bgcolor("black")
    pensize(2)

    for i in range(300):
        color(colors[i % 6])
        forward(size)
        left(59)
        forward(size)
        left(59)
        forward(size)
        left(59)
        forward(size)
        left(121)
        size += 2

    hideturtle()


draw(20)

done()
