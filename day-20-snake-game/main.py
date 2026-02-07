from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
import food
import time


screen = Screen()
screen.setup(width=600, height = 600)
SCREEN_WIDTH = screen.window_width()
SCREEN_HEIGHT = screen.window_height()
RIGHT_BOUNDARY = SCREEN_WIDTH / 2
LEFT_BOUNDARY = -SCREEN_WIDTH / 2
TOP_BOUNDARY = SCREEN_HEIGHT / 2
BOTTOM_BOUNDARY = -SCREEN_HEIGHT / 2

screen.colormode(255)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0) #off


snake = Snake()
food = food.Food(SCREEN_WIDTH, SCREEN_HEIGHT)
scoreboard = Scoreboard(screen)

# bind keys
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

screen.listen()
base_speed = 0.5
game_is_on = True
while game_is_on:
    screen.update()
    speed = max(0.02, base_speed - (scoreboard.score * 0.005))
    time.sleep(speed)
    snake.move()

    # detect collision with food pellet
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        snake.grow()
        snake.change_color(food.current_color)
        food.refresh(snake)

    #detect collision with the screen boundaries
    if snake.head.xcor() > (RIGHT_BOUNDARY - 5) or snake.head.xcor() < (LEFT_BOUNDARY + 5)\
            or snake.head.ycor() > (TOP_BOUNDARY - 5) or snake.head.ycor() < (BOTTOM_BOUNDARY + 5):
        game_is_on = False
        scoreboard.game_over()

    # detect collision with its own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()