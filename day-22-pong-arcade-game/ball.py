from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        """Initializes a ball turtle object with custom attributes"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 1, None)
        self.penup()
        self.x_speed = 3
        self.y_speed = random.uniform(-2,2)
        self.radius = 20 * self.shapesize()[0] / 2


    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_speed *=-1.2

    def bounce_y(self):
        self.y_speed *=-1.2

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.x_speed = 3
        self.y_speed = random.uniform(-2,2)
