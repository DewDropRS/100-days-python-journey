from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier"

# Scoreboard inherits Turtle
class Scoreboard(Turtle):
    def __init__(self, screen_turtle):
        super().__init__()
        self.screen_turtle = screen_turtle
        self.score = 0
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        write_y = self.screen_turtle.window_height() // 2 - (self.screen_turtle.window_height() * .05)
        left_score_x = -self.screen_turtle.window_width()//4
        right_score_x = self.screen_turtle.window_width()//4
        self.goto(left_score_x, write_y)
        self.write(f"{self.left_score}", align="center", font =("Courier", 20, "bold"))
        self.goto(right_score_x, write_y)
        self.write(f"{self.right_score}", align="center", font=("Courier", 20, "bold"))

    def increase_left_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font =("Courier", 18, "bold"))