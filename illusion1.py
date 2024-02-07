from turtle import *


def draw():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    speed(10)
    bgcolor("black")
    pensize(2)

    for i in range(180):
        color(colors[i % 6])
        forward(200)
        right(61)
        forward(100)
        right(120)
        forward(100)
        right(61)
        forward(200)
        right(181)

    hideturtle()


# Call the function to draw the attractive design with black background
draw()

done()
