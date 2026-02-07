from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier"

# MyTurtle inherits Turtle
class Scoreboard(Turtle):
    def __init__(self, screen_turtle):
        super().__init__()
        write_y = screen_turtle.window_height() // 2 - (screen_turtle.window_height() * .05)
        write_x = screen_turtle.window_width() // 2 - (screen_turtle.window_width() * .05)
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(write_x, write_y)
        self.color("green")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="right", font =("Courier", 14, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font =("Courier", 18, "bold"))
