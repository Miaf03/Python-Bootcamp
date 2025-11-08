from turtle import Turtle

class Brick(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(position)

    def destroy(self):
        self.goto(1000, 1000)
        self.hideturtle()