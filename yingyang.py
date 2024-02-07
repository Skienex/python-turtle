from turtle import *

def yingyang(position, size):
    global curr_yingyangs
    global max_yingyangs
    # Outer ring
    penup()
    goto(position[0] - size, position[1] - size)
    pendown()
    begin_fill()
    circle(size, 180)
    circle(size / 2, 180)
    circle(-(size / 2), 180)
    end_fill()
    circle(-size, 180)

    # Inner Circles
    inner_position = []
    fillcolor("#ffffff")
    right(90)
    for i in range(2):
        forward(size / 2)
        left(90)
        forward(size / 6)
        left(90)
        pendown()
        begin_fill()
        circle(size / 6)
        inner_position.append(pos())
        end_fill()
        penup()
        left(90)
        forward(size / 6)
        left(90)
        forward(size / 2)
        fillcolor("#000000")

    # Yingyang in the first smaller circle
    left(90)
    curr_yingyangs += 1
    if curr_yingyangs < max_yingyangs:
        yingyang(inner_position[0], size / 6)

speed(10)
max_yingyangs = 4
curr_yingyangs = 0
yingyang((0, 0), 400)
done()