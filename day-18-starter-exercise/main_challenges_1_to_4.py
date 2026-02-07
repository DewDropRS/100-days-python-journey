from turtle import Turtle, Screen, colormode
from random import randint

# for really long names you can use the syntax below:
# import turtle as t

# from turtle import * # avoid this because can be harder to track down which methods/attributes come from what classes
# and you can end up with name conflicts
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('LightSeaGreen')
# timmy.forward(100)
# timmy.right(90)


# for steps in range(100):
#     for c in ('DarkSeaGreen', 'LemonChiffon'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(90)

# Challenge 1: Draw a square
# for c in ('DeepPink', 'chartreuse','gold1', 'blue' ):
#     timmy.pencolor(c)
#     timmy.forward(100)
#     timmy.right(90)

# Challenge 2: Draw a dashed line
# for _ in range(25):
#     timmy.forward(5)
#     timmy.up()
#     timmy.forward(5)
#     timmy.down()

# Challenge 3: Draw polygons
colormode(255)
# def draw_polygon(vertex_count):
#     angle = 360/vertex_count
#
#     for i in range(vertex_count):
#         #prettier with the random colors for each side
#         #alternatively, you can load some colors into a list and choose random from the list
#         r = randint(0, 255)
#         g = randint(0, 255)
#         b = randint(0, 255)
#         timmy.color(r, g, b)
#         timmy.right(angle)
#         timmy.forward(100)
#
#
# for v_cnt in range(3,13):
#     draw_polygon(v_cnt)

# Challenge 4: Random walk
# Each segment of path is a random color
# Change thickness of path
# Looks like only 90 degree turns on a grid-like plane
# Speed up the turtle
# Don't let turtle go off the canvas

# instantiate object Turtle
t = Turtle()
colormode(255)
def draw_segment(turtle, deg, seg_distance):
    """Draw a segment with random color line. Takes a turtle object, angle in degrees, and segment distance."""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turtle.shape('turtle')
    # turtle.hideturtle()
    turtle.speed(0)
    turtle.setheading(angle)
    turtle.speed(6) # back to normal speed
    # turtle.showturtle()
    turtle.color(r, g, b)
    turtle.pensize(5)
    turtle.forward(seg_distance)


screen = Screen()
screen.resetscreen()

def is_within_bounds(turtle_obj, deg, distance):
    """Check if moving turtle in given direction would stay within screen bounds."""

    # Get boundaries
    max_x = screen.window_width() / 2
    min_x = -screen.window_width() / 2
    max_y = screen.window_height() / 2
    min_y = -screen.window_height() / 2

    # Calculate the potential new position of turtle
    new_x = turtle_obj.xcor()
    new_y = turtle_obj.ycor()

    if deg == 0:  # East
        new_x += distance
    elif deg == 90:  # North
        new_y += distance
    elif deg == 180:  # West
        new_x -= distance
    elif deg == 270:  # South
        new_y -= distance

    # Return True if within bounds
    return (min_x <= new_x <= max_x) and (min_y <= new_y <= max_y)

running = True
def stop_on_click(x,y):
    """Allows the user to stop the random walk with a mouse click."""
    global running
    running = False
    print("Random walk stopped by user.")
screen.onclick(stop_on_click)

for i in range(1000):
    if not running:
        break
    angle = 90 * randint(0,3)
    draw_length = 20
    if is_within_bounds(t, angle, draw_length):
        draw_segment(t, angle, draw_length)
    else:
        pass

screen.exitonclick()


