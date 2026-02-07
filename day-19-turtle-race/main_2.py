from turtle import Turtle, Screen, colormode
import random

# Challenge turtle race
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height =600)
screen.title("Turtle Race")
screen.colormode(255)
color_codes = [(144,46,242),(68,48,140),(242,210,46),(242,135,41),(242,95,41)]
game_active = True
finish_line_x = None
turtle_dict = {}
user_guess = ''
# For writing
TOP_LINE_Y = 0
SECOND_LINE_Y = 0
THIRD_LINE_Y = 0

#0 is fastest and 1 is slowest
speed_list = [0,10,6,3,1]
def get_width_boundaries():
    """Returns a tuple for window width"""

    # Get boundaries
    max_x = int(screen.window_width() / 2)
    min_x = int(-screen.window_width() / 2)
    width_tuple = [min_x, max_x]
    return width_tuple

def get_height_boundaries():
    """Returns a tuple for window height"""
    # Get boundaries
    max_y = int(screen.window_height() / 2)
    min_y = int(-screen.window_height() / 2)
    height_tuple = [min_y, max_y]
    return height_tuple
def generate_list_of_visually_distinct_colors(number_colors):
    """Generate a list of visually distinct colors."""
    colors = []
    for _ in range(number_colors):
        channel_choice = random.randint(0, 2)  # this will determine which channel will dominate

        if channel_choice == 0:  # Red dominant
            color = (random.randint(150, 255), random.randint(0, 150), random.randint(0, 150))
        elif channel_choice == 1:  # Green dominant
            color = (random.randint(0, 150), random.randint(150, 255), random.randint(0, 150))
        else:  # Blue dominant
            color = (random.randint(0, 150), random.randint(0, 150), random.randint(150, 255))
        colors.append(color)
    return colors

def draw_finish_line():
    finish_x = (get_width_boundaries()[1]) - (get_width_boundaries()[1] * 0.20)
    top_y = (get_height_boundaries()[1]) - (get_height_boundaries()[1] * 0.40)
    bottom_y = (get_height_boundaries()[0]) + (-get_height_boundaries()[0] * 0.20)
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.goto(finish_x, top_y)
    line.pendown()
    line.pensize(5)
    line.color("white")
    line.goto(finish_x, bottom_y)
    # Add "FINISH" text
    line.penup()
    line.goto(finish_x, top_y)
    line.write("FINISH", align="center", font=("Arial", 16, "bold"))
    return finish_x

def check_winner(turtle):
    global game_active
    if game_active and turtle.xcor() >= finish_line_x:
        game_active = False
        announce_winner(turtle)

def race():
    if game_active:  # Stops when winner crosses finish line
        for racer in turtle_dict:
            turtle_dict[racer].move_forwards_random()
        screen.ontimer(race, 100)

def announce_winner(winner_turtle):
    announcer = Turtle()
    announcer.hideturtle()
    announcer.penup()
    announcer.goto(0, THIRD_LINE_Y)
    announcer.color(winner_turtle.rgb_color)
    # Check if user guessed correctly
    if user_guess.lower() == winner_turtle.name.lower():
        message = f"{winner_turtle.name} Wins!\nYou guessed correctly!"
    elif user_guess:
        message = f"{winner_turtle.name} Wins!\nBetter luck next time!"
    else:
        message = f"{winner_turtle.name} Wins!"

    announcer.write(message,
                   align="center",
                   font=("Arial", 14, "bold"))


class MyTurtle(Turtle):

    def __init__(self, start_pos=(0,0),rgb=(0,0,0)):
        super().__init__()
        self.hideturtle()
        self.shape('turtle')
        self.speed(0)
        self.color(rgb)
        self.rgb_color = rgb  # RGB tuple

        self.name = 'turtle'
        self.penup()

        self.setposition(start_pos)
        self.pendown()
        self.showturtle()

    def move_forwards_random(self):
        """for computer driven race"""
        if game_active:
            self.dot(5)
            self.speed(random.choice(speed_list))
            self.forward(random.randint(1,50))
            check_winner(self)

    def set_random_color_from_color_list(self, c_list):
        """Sets a random color for a turtle from a list of rgb tuples."""
        self.color(random.choice(c_list))

def game():
    """Computer generated game."""
    global color_codes, finish_line_x, turtle_dict, user_guess, TOP_LINE_Y, SECOND_LINE_Y, THIRD_LINE_Y

    # Y-pos constants for writing
    TOP_LINE_Y = (get_height_boundaries()[1]) - (get_height_boundaries()[1] * .15)
    SECOND_LINE_Y = TOP_LINE_Y - 30
    THIRD_LINE_Y = SECOND_LINE_Y - 50

    #title
    width = get_width_boundaries()
    # print(f"Width: {width}")
    # print(f"Height: {height}")
    writer = Turtle()
    writer.hideturtle()  # Hide the turtle
    writer.color("white")
    writer.penup()
    writer.goto(0, TOP_LINE_Y)  # Position at top of screen
    writer.write("Welcome to the turtle race!", align="center", font=("Arial", 14, "bold"))

    #set and draw the finish line
    finish_line_x = draw_finish_line()

    #build racers
    name_list = ['Lottie', 'Tilly','Pepper', 'Delilah', 'Tygra']
    x_pos_buffer = (get_width_boundaries()[1] * 0.10)

    #top of the finish line: top_y = (get_height_boundaries()[1]) - (get_height_boundaries()[1] * 0.40)
    y_pos = (get_height_boundaries()[1]) - (get_height_boundaries()[1] * 0.6)
    for i, key in enumerate(name_list):
        start_pos = (width[0] + x_pos_buffer, y_pos)
        t = MyTurtle(start_pos,color_codes[i])
        t.name = key
        turtle_dict.update({key: t})
        t.hideturtle()
        t.penup()
        t.goto(start_pos[0],start_pos[1]+10)
        t.write(f"{key} ({i + 1})", align = "left", font=("Arial", 14, "normal"))
        t.goto(start_pos)
        t.showturtle()
        t.pendown()
        y_pos -= 75

    user_guess = screen.textinput("Make Your Bet",
                                  f"Which turtle will win?\n{', '.join(name_list)}")

    # Validate guess (case-insensitive)
    if user_guess:
        user_guess = user_guess.title()  # Capitalize first letter
        if user_guess not in name_list:
            user_guess = None

    if user_guess:
        guess_display = Turtle()
        guess_display.hideturtle()
        guess_display.penup()
        guess_display.color(turtle_dict[user_guess].rgb_color)
        guess_display.goto(0, SECOND_LINE_Y)
        guess_display.write(f"You picked {user_guess} to win.",
                           align="center",
                           font=("Arial", 14, "bold"))
    race()
    screen.exitonclick()

# User driven turtle_race not completed yet
# turtle_race()
game()
