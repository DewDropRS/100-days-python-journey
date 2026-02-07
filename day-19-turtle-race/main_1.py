from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

screen.listen()

def move_forwards():
    t.forward(10)
def move_backwards():
    t.backward(10)
def move_counter_clockwise():
    t.left(10)
def move_clockwise():
    t.right(10)
def clear_screen():
    t.reset()

screen.listen()
# example of Functions as Inputs (don't include parentheses at end)
# Higher order functions
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()

# w = Forwards
# s = Backwards
# a = Counter-Clockwise
# d = Clockwise
# c = clear screen
