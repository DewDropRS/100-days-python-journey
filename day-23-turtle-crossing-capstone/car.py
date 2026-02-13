from turtle import Turtle


class Car(Turtle):
    def __init__(self, lane):
        """Initialize a car object. Takes a lane object. It is given a shapesize, color
        and goes to its start position."""
        super().__init__()
        self.shape("square")
        # each car is 20 x 40
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(lane.color)
        self.penup()
        if lane.direction == "left":
            self.goto(280, lane.y_position)
            self.start_position_x = 280
        else:
            self.goto(-280, lane.y_position)
            self.start_position_x = -280
        self.direction = lane.direction
        self.speed_value = lane.speed

    def move(self):
        """Cars move forward by the lane speed based and direction."""

        if self.direction == "left":
            self.forward(-self.speed_value)
        else:
            self.forward(self.speed_value)