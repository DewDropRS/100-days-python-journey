import turtle
import pandas as pd
from datetime import datetime

screen = turtle.Screen()
screen.title("U.S. States Game")

#Add image as a shape and set it as the turtle's shape
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Read csv file and load to a data frame
df = pd.read_csv('50_states.csv')
states_dict = df.to_dict() #not being used

# This was used by the instructor to get the coordinates for all 50 states on the image
# This is a one time operation. The coordinate data is in 50_states.csv
# Use this if you want to change the size of the screen and need to obtain new coordinates for states
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# create turtle object to write states to map
turtle_writer = turtle.Turtle()
turtle_writer.hideturtle()
turtle_writer.penup()

def is_state(user_input):
    return user_input in df["state"].values

def update_map(user_input):
    """Updates the map when state name is given correctly. Makes use of the data dictionary."""
    # items() returns each key-value pair in the state column as a tuple (index, state_name).
    # The list comprehension iterates through them, filters for the matching state name,
    # and [0] grabs the first (and only) index found.
    idx = [k for k, v in states_dict["state"].items() if v == user_input][0]
    x = states_dict["x"][idx]
    y = states_dict["y"][idx]
    turtle_writer.goto(x, y)
    turtle_writer.write(user_input,align="left",font=("Arial",6,"normal"))
        #also update score
def update_map_alternate(user_input):
    """Updates the map when state name is given correctly. Makes use of the data frame."""
    turtle_writer.color("green")
    row = df[df["state"] == user_input].squeeze()  # get matching row, row is now a series
    turtle_writer.goto(row.x, row.y)
    turtle_writer.write(user_input, align="left", font=("Arial", 8, "bold"))

game_continues = True
game_score = 0
testing_number = 50
guessed_states = []
while game_score <= testing_number:
    if game_score == testing_number:
        turtle_writer.color("black")
        turtle_writer.goto(0,0)
        turtle_writer.write("You named all 50 states!", align="center", font=("Arial", 14, "normal"))

        break
    elif not game_continues:
        # I want a list of things from this collection where some condition is true
        states_not_guessed = [state for state in df["state"] if state not in guessed_states]

        # Create a timestamp string
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Save missed states to CSV for tracking progress over time
        states_not_guessed_df = pd.DataFrame(states_not_guessed, columns=["state"])
        states_not_guessed_df.to_csv(f"states_to_learn_{timestamp}.csv", index=False)

        turtle_writer.color("red")
        for state in states_not_guessed:
            row = df[df["state"] == state].squeeze() # row is a series
            turtle_writer.goto(row.x, row.y) # dot notation
            turtle_writer.write(state, align="left", font=("Arial", 8, "normal"))
        turtle_writer.color("black")
        turtle_writer.goto(0,0)
        turtle_writer.write(f"Way to go! You guessed {game_score}/50 states.", align="center", font=("Arial", 14, "normal"))
        break
    else:
        answer_state = screen.textinput(title = f"{game_score}/50 States Correct", prompt="What's another state's name or type 'quit' to quit game.")
        answer_state_formatted = ' '.join(answer_state.split()).title()
        if answer_state_formatted == 'Quit':
            game_continues = False
        elif is_state(answer_state_formatted):
            if answer_state_formatted not in guessed_states:
                guessed_states.append(answer_state_formatted)
                update_map_alternate(answer_state_formatted)
                game_score +=1


screen.exitonclick()