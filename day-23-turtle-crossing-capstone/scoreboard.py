import turtle
from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-260,260)

class Scoreboard(Turtle):
    """Initializes the scoreboard."""
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.level = 1
        self.update_scoreboard()

    def level_up(self):
        """Levels up by one."""
        self.level +=1

    def update_scoreboard(self):
        """Updates the scoreboard by re-writing the level to the screen."""
        self.clear()
        self.goto(SCOREBOARD_POSITION)
        self.write(f"LEVEL: {self.level}", align="left", font=("Courier", 14, "bold"))

    def game_over(self):
        """Writes game over to the screen."""
        self.goto(0,SCOREBOARD_POSITION[1])
        self.write(f"Game Over", align="center", font =("Courier", 14, "bold"))