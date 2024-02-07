from turtle import *

def draw(initial_size):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    speed(10)
    bgcolor("black")
    pensize(2)

    for i in range(200):
        color(colors[i % 6])
        forward(initial_size + i)
        left(59)

    hideturtle()


draw(30)

done()