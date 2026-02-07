import colorgram
import random
from turtle import Turtle, Screen, colormode

t = Turtle()
colormode(255)
screen = Screen()

colors = colorgram.extract('damien_hirst_dot_image.jpg',30 )
rgb_tuples = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]


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

# print(color_list)


def stop_on_click(x,y):
    """Allows the user to stop the random walk with a mouse click."""
    global running
    running = False
    print("Random walk stopped by user.")

running = True

def paint_like_hirst(dots_across = 10, dots_down = 10, dot_size = 20, spacing = 50, border = 50):
    """Paint like Hirst. Draws dots across the window canvas. You can specify the number of dots down and
    across that you want. You can specify the dot size, spacing, and border as well.
    Spacing is from dot center to dot center so careful not to make dot size bigger than spacing size unless
    you want the overlapping appearance. The dots will appear on canvas starting from the left bottom corner
    across rows until it reaches the upper right corner."""

    global running
    # Calculate window size based on arguments passed through
    new_window_width = (dots_across * spacing) + (2 * border)
    new_window_height = (dots_down * spacing) + (2 * border)
    # print(f"New window width: {new_window_width}")  # for debugging
    # print(f"New window height: {new_window_height}")  # for debugging

    # Set custom window dimensions
    screen.setup(width = new_window_width, height = new_window_height)

    # need the starting position (left/bottom position)
    # (dots_across -1) are the number of gaps
    first_dot_x = -(dots_across - 1) * spacing / 2 # leftmost starting x position (neg value)
    first_dot_y = -(dots_down - 1) * spacing / 2 # bottommost starting y position (neg value)

    t.speed('fastest')
    t.hideturtle()
    screen.onclick(stop_on_click)
    for row in range(dots_down):
        if not running:
            break
        for col in range(dots_across):
            if not running:
                break
            x_pos = first_dot_x + (col * spacing)
            y_pos = first_dot_y + (row * spacing)
            t.penup()
            t.setposition(x_pos, y_pos)
            t.dot(dot_size,random.choice(rgb_tuples))


    screen.exitonclick()
paint_like_hirst(dots_across = 10, dots_down = 10, dot_size = 50, spacing = 50, border = 50)