from turtle import Turtle
STARTING_POSITION = (0, -212.5)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        """Initializes a default player."""
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()


    def move(self):
        """Moves a distance of 10 pixels"""
        self.forward(MOVE_DISTANCE)

    def head_up(self):
        """Sets the direction of the turtle to go up."""
        self.hideturtle()
        self.setheading(90)
        self.showturtle()
        self.move()

    def head_down(self):
        """Sets the direction of the turtle to go down."""
        self.hideturtle()
        self.setheading(270)
        self.showturtle()
        self.move()

    def head_left(self):
        """Sets the direction of the turtle to go left."""
        self.hideturtle()
        self.setheading(-180)
        self.showturtle()
        self.move()

    def head_right(self):
        """Sets the direction of the turtle to go right."""
        self.hideturtle()
        self.setheading(0)
        self.showturtle()
        self.move()

    def at_finish(self, finish_pos):
        """Checks if player safely crossed the roads by checking it y coordinate."""
        return self.ycor() >= finish_pos

    def reset(self):
        """Resets the player to the starting position"""
        self.goto(STARTING_POSITION)