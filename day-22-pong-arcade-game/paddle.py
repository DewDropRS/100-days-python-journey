from turtle import Turtle
MOVE_STEP = 10

class Paddle(Turtle):
    def __init__(self, xpos,t_boundary, b_boundary, buffer):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(5, 1, None)
        self.color("white")
        self.penup()
        self.goto(xpos, 0)
        self.showturtle()
        self.direction = 0

        # Add paddle dimensions as attributes
        self.width = 20 * self.shapesize()[1]
        self.height = 20 * self.shapesize()[0]
        self.half_width = self.width / 2
        self.half_height = self.height / 2

        # boundaries passed through
        self.top_boundary = t_boundary
        self.bottom_boundary = b_boundary
        self.boundary_buffer = buffer

    def move(self,t_boundary, b_boundary, buffer):
        """Moves the paddle up by the constant MOVE_STEP and direction"""
        if self.direction != 0:
            new_y = self.ycor() + (MOVE_STEP * self.direction)
            # Check boundaries before moving
            if self.top_boundary - self.half_height - self.boundary_buffer > new_y > self.bottom_boundary + self.half_height + self.boundary_buffer:
                self.goto(self.xcor(), new_y)


    def start_move_up(self):
        """Sets the direction as positive multiplier"""
        self.direction =1

    def start_move_down(self):
        """Sets the direction as negative multiplier"""
        self.direction = -1

    def stop_move(self):
        """Sets the direction as 0 to stop movement"""
        self.direction = 0