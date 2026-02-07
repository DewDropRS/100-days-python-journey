from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

def play_game():
    screen = Screen()
    screen.setup(800,600)
    screen.bgcolor('black')
    screen.title("My Pong Game - Originally developed by Allan Alcorn for Atari")
    #turn off animation (requires screen.update in a while loop)
    screen.tracer(0)
    screen_width = screen.window_width()
    screen_height = screen.window_height()
    right_boundary = screen_width / 2
    left_boundary = -screen_width / 2
    top_boundary = screen_height / 2
    bottom_boundary = -screen_height / 2
    boundary_buffer = 2
    draw_center_line(screen_height)
    # Get winning score from user
    # Get winning score from user
    winning_score_input = screen.textinput("Game Setup",
                                           "Enter the target score between 3 and 21 (must win by 2 points): ")

    # Validate and set winning score
    try:
        winning_score = int(winning_score_input)

        # Check if within range
        if winning_score < 3 or winning_score > 21:
            print("Out of range, defaulting to 5 points")
            winning_score = 5
        # Check if even number
        elif winning_score % 2 == 0:
            winning_score += 1  # Make it odd
            print(f"Adjusted to odd number: {winning_score}")

    except (ValueError, TypeError):
        winning_score = 5  # Default if invalid input
        print("Invalid input, defaulting to 5 points")

    # Display start message IMMEDIATELY after winning score input
    start_message_y = top_boundary - 60
    start_message = Turtle()
    start_message.hideturtle()
    start_message.color("white")
    start_message.penup()
    start_message.goto(0, start_message_y)
    start_message.write("Press SPACE to start", align="center", font=("Courier", 18, "normal"))
    screen.update()  # Show the message

    scoreboard = Scoreboard(screen)


    #instantiate paddle objects
    right_paddle = Paddle(350, top_boundary, bottom_boundary, boundary_buffer)
    left_paddle = Paddle(-350, top_boundary, bottom_boundary, boundary_buffer)
    #instantiate ball object
    ball = Ball()
    screen.listen()
    screen.update()

    # demonstrates functions as inputs (pass only the name without parentheses)
    # A higher-order function is a function that does one of these:
    # Takes one or more functions as arguments (parameters)
    # OR Returns a function as its result
    screen.onkeypress(right_paddle.start_move_up, "Up")
    screen.onkeypress(right_paddle.start_move_down, "Down")
    screen.onkeyrelease(right_paddle.stop_move, "Up")
    screen.onkeyrelease(right_paddle.stop_move, "Down")

    screen.onkeypress(left_paddle.start_move_up, "a")
    screen.onkeypress(left_paddle.start_move_down, "z")
    screen.onkeyrelease(left_paddle.stop_move, "a")
    screen.onkeyrelease(left_paddle.stop_move, "z")

    game_is_on = False

    def start_game():
        nonlocal game_is_on
        game_is_on = True
        start_message.clear()

    # User clicks the space bar when they are ready to play
    screen.onkey(start_game, "space")

    # Game loop
    while not game_is_on:
        screen.update()  # Keep screen responsive while waiting

    while game_is_on:
        #~60 FPS (1/60 = ~ 0.016 seconds)
        time.sleep(0.016)
        ball.move()

        # allow movement of a paddle
        # paddles should not move off the playable screen
        right_paddle.move(top_boundary, bottom_boundary, boundary_buffer)
        left_paddle.move(top_boundary, bottom_boundary, boundary_buffer)

        # check for collisions at top and bottom boundaries
        if ball.ycor() > (top_boundary - ball.radius ) or ball.ycor() < (bottom_boundary + ball.radius + boundary_buffer):
           #change directions
            ball.bounce_y()

        # Detect collision with paddles
        # have to consider not only the x coordinate value but the distance between the turtle centroids
        if ((ball.distance(right_paddle) < 50 and ball.xcor() > 330) or
                (ball.distance(left_paddle) < 50 and ball.xcor() < -330)):
            ball.bounce_x()

        # Left player scores
        elif ball.xcor() > right_boundary:
            # print(f"ball went off right boundary so left player should score. ball.xcor: {ball.xcor()}")
            ball.reset()
            time.sleep(1)
            scoreboard.increase_left_score()

        # Right player scores
        elif ball.xcor() < left_boundary:
           # print(f"ball went off left boundary so right player should score. ball.xcor: {ball.xcor()}")
            ball.reset()
            time.sleep(1)
            scoreboard.increase_right_score()

        # Check for winner (after any score update)
        if ((scoreboard.left_score >= winning_score or scoreboard.right_score >= winning_score) and
                abs(scoreboard.left_score - scoreboard.right_score) >= 2):
            ball.hideturtle()
            game_is_on = False
            scoreboard.game_over()

        screen.update()
    # Ask to play again
    play_again = screen.textinput("Game Over", "Play again? (yes/no):")
    screen.clear()  # Clear the screen

    if play_again and play_again.lower() in ['yes', 'y']:
        screen.clear()
        play_game()  # Recursive call - starts fresh
    else:
        screen.bye()  # Close the window

    screen.exitonclick()


def draw_center_line(screen_height):
    """Draw dashed line down the center of screen"""
    line = Turtle()
    line.hideturtle()
    line.color("white")
    line.penup()
    line.goto(0, screen_height / 2)
    line.setheading(270)  # Point downward
    line.pensize(3)

    # Draw dashed line
    for _ in range(int(screen_height / 20)):
        line.pendown()
        line.forward(10)  # Dash length
        line.penup()
        line.forward(10)  # Gap length

    return line
# Start the game
play_game()
