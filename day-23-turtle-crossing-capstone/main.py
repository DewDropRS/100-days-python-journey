# Standard library imports
import time
import random

# Third-party imports
from turtle import Screen, Turtle

# Local imports
from player import Player
from scoreboard import Scoreboard
from lane import Lane

# Lane centers where cars drive
LANE_Y_POSITIONS = [-150, -100, -50, 0, 50, 100]
lane_car_colors = ["black", "red", "green", "yellow", "blue", "purple"]
FINISH_LINE_Y = LANE_Y_POSITIONS[-1] + 40
SPEED_INCREASE_FACTOR = 1.1

def setup_game():
    """Initializes screen, draws background graphics, creates game objects."""
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Draw lane backgrounds
    draw_backgrounds()

    # Create game objects
    scoreboard = Scoreboard()
    traffic_lanes = create_traffic_lanes()
    player = Player()

    screen.onkey(player.head_up, "Up")
    screen.onkey(player.head_down, "Down")
    screen.onkey(player.head_left, "Left")
    screen.onkey(player.head_right, "Right")

    screen.listen()

    return screen, scoreboard, traffic_lanes, player

def draw_backgrounds():
    """Draws the background for car lanes that alternate between gray and dark gray.
    Also draws grass areas above and below the car lanes."""

    lane_bg = Turtle()
    lane_bg.hideturtle()
    lane_bg.penup()
    lane_bg.speed(0)
    lane_bg_colors = ["gray", "dark gray", "gray", "dark gray", "gray", "dark gray"]
    lane_height = 50

    # Draw grass below the lanes
    road_bottom = LANE_Y_POSITIONS[0] - lane_height / 2
    lane_bg.goto(-300, -300)
    lane_bg.color("green")
    lane_bg.begin_fill()
    for _ in range(2):
        lane_bg.forward(600)
        lane_bg.left(90)
        lane_bg.forward(road_bottom + 300)
        lane_bg.left(90)
    lane_bg.end_fill()

    # Draw lane backgrounds
    for i, y in enumerate(LANE_Y_POSITIONS):
        lane_bg.goto(-300, y - lane_height / 2)
        lane_bg.color(lane_bg_colors[i])
        lane_bg.begin_fill()
        for _ in range(2):
            lane_bg.forward(600)
            lane_bg.left(90)
            lane_bg.forward(lane_height)
            lane_bg.left(90)
        lane_bg.end_fill()

    # Draw grass above the lanes
    road_top = LANE_Y_POSITIONS[-1] + lane_height / 2
    lane_bg.goto(-300, road_top)
    lane_bg.color("green")
    lane_bg.begin_fill()
    for _ in range(2):
        lane_bg.forward(600)
        lane_bg.left(90)
        lane_bg.forward(300 - road_top)
        lane_bg.left(90)
    lane_bg.end_fill()

def create_traffic_lanes():
    """Create and returns list of lange objects."""
    traffic_lanes = []
    for i in range(len(LANE_Y_POSITIONS)):
        color = lane_car_colors[i]
        if i%2 == 0:
            speed = random.randint(5, 7)
            new_lane = Lane(LANE_Y_POSITIONS[i], direction = "left", speed = speed, color=color)
        else:
            speed = random.randint(5, 7)
            new_lane = Lane(LANE_Y_POSITIONS[i], direction="right", speed=speed, color=color)

        traffic_lanes.append(new_lane)
    return traffic_lanes




# Now catch them outside the function:
screen, scoreboard, traffic_lane, player = setup_game()
# Each loop is equal to 1 frame, cars move forward 10 steps each loop

def play_game():
    """Executes game play. Checks for collisions. Checks if player
    made it safely across the roads. If so, game levels up and
    speed increases. If game is over from a collision, player is asked if
    they would like to play again."""
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        for l in traffic_lane:
            l.update()

        # Collision check
        for lane in traffic_lane:
            for car in lane.cars:
                if player.distance(car) < 15:
                    game_is_on = False  # or your game over logic
                    scoreboard.game_over()
                    # Ask to play again
                    play_again = screen.textinput("Game Over", "Play again? (yes/no):")

                    if play_again and play_again.lower() in ['yes', 'y']:
                        for l in traffic_lane:
                            l.reset()
                        player.reset()
                        scoreboard.level = 1
                        scoreboard.update_scoreboard()
                        screen.listen()
                        play_game()  # Recursive call - starts fresh
                    else:
                        screen.bye()  # Close the window

        if player.at_finish(FINISH_LINE_Y):
            scoreboard.level_up()
            scoreboard.update_scoreboard()
            player.reset()

            for l in traffic_lane:
                l.speed *= SPEED_INCREASE_FACTOR


play_game()
screen.exitonclick()