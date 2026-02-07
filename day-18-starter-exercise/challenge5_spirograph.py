from turtle import Turtle, Screen, colormode
from random import randint
t = Turtle()
colormode(255)
screen = Screen()
# angle_step_size = 5

angle = 0 #starting angle
colormode(255)
# t.speed("fastest")
running = True

def stop_on_click(x,y):
    """Allows the user to stop the random walk with a mouse click."""
    global running
    running = False
    print("Random walk stopped by user.")

def get_random_rgb_tuple():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r,g,b)
    return color

def draw_circle_spirograph(angle_step_size = 2, speed="fastest"):
    global angle
    t.speed(speed)
    number_angle_steps = int(360/angle_step_size)
    screen.onclick(stop_on_click)

    for n in range(0,number_angle_steps):
        if not running:
            break
        t.color(get_random_rgb_tuple())
        t.setheading(angle)
        # print(f"turtle heading: {t.heading()}") #for debugging
        t.circle(100,None, None)
        #increment angle by step size
        angle += angle_step_size

    screen.exitonclick()

# draw_circle_spirograph()
draw_circle_spirograph(5,"fastest")