import random
from turtle import Turtle

COLOR_CODES = [
    (255, 0, 0),  # Red
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 0),  # Green
    (128, 0, 128),  # Purple
    (255, 165, 0),  # Orange
    (255, 192, 203),  # Pink
        ]

class Food(Turtle):
    """Class for food in the Snake game."""

    def __init__(self,  screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food_radius = (20 * 0.5) // 2  # = 5
        self.buffer = int(self.food_radius * 3)  # = 10
        self.current_color = random.choice(COLOR_CODES)
        self.color(self.current_color)
        self.speed("fastest")
        random_x = random.randint(-self.screen_width // 2 + self.buffer, self.screen_width // 2 - self.buffer)
        random_y = random.randint(-self.screen_height // 2 + self.buffer, self.screen_height // 2 - self.buffer)
        self.goto(random_x,random_y)

    def refresh(self, snake = None):
        """Food pellet will appear at a random position on the screen and with a different color than prior color."""

        available_colors = [c for c in COLOR_CODES if c != self.current_color]
        self.current_color = random.choice(available_colors)
        self.color(self.current_color)

        while True:
            random_x = random.randint(-self.screen_width // 2 + self.buffer, self.screen_width // 2 - self.buffer)
            random_y = random.randint(-self.screen_height // 2 + self.buffer, self.screen_height // 2 - self.buffer)

            food_on_snake = False
            for segment in snake.segments:
                if segment.distance(random_x, random_y) < self.buffer:
                    food_on_snake = True
                    break

            if not food_on_snake:
                self.goto(random_x, random_y)
                break

