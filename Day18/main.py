import turtle as t
import random

colors = [
    (239, 246, 241), (246, 241, 239), (234, 239, 245), (220, 221, 225),
    (240, 232, 219), (228, 234, 238), (241, 209, 91), (234, 66, 31),
    (244, 229, 39), (44, 108, 140), (145, 18, 36), (27, 38, 66),
    (232, 129, 26), (37, 41, 33), (10, 97, 74), (236, 81, 108)
]

t.colormode(255)

turtle = t.Turtle()
turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

for dot in range(1, 101):
    turtle.dot(20, random.choice(colors))
    turtle.forward(50)

    if dot % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen = t.Screen()
screen.exitonclick()