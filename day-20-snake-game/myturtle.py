from turtle import Turtle

# MyTurtle inherits Turtle
class MyTurtle(Turtle):
    def __init__(self,start_pos=(0,0)):
        super().__init__()
        # default turtle size is 20x20
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(start_pos)