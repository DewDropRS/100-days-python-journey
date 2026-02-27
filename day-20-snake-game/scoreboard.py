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
        with open("/Users/RSegu/PycharmProjects/100-days-python-journey/day-20-snake-game/data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(write_x, write_y)
        self.color("green")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="right", font =("Courier", 14, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", align="center", font =("Courier", 18, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/RSegu/PycharmProjects/100-days-python-journey/day-20-snake-game/data.txt", mode = "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()