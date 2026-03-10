# Unlimited "positional" arguments
# *args gets placed in a tuple and so you can access the arguments using an index
# You can define a function with default values and call the function without arguments or with only
# the required arguments
def add(*args):
    result = 0
    for n in args:
        result += n
    return result

add_result = add(1,2,10,5)
print(add_result)

# **kwargs - unlimited keyword arguments - a dictionary with keys and values!
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n
print(calculate(2, add=3, multiply =5))

# NOTE: When using **kwargs in __init__, use .get() to safely access optional
# parameters instead of kwargs["key"] — direct key access raises a KeyError
# if the argument wasn't passed during instantiation, but .get() returns None
# (or a default value you specify) if the key doesn't exist.

# NOTE: Default values can be set in two equivalent ways:
#   1. In the function signature: def __init__(self, color="blue")
#   2. In .get() when using **kwargs: kwargs.get("color", "blue")
# Option 1 gives you IDE hints/autocomplete. Option 2 is more flexible
# and is why tkinter uses **kwargs — widgets have too many optional
# parameters to list explicitly in the signature.

class MyWidget:
    def __init__(self, **kwargs):
        self.color = kwargs.get("color", "blue")  # defaults to "blue" if not passed
        self.size = kwargs.get("size", 12)         # defaults to 12 if not passed
        self.label = kwargs.get("label")           # returns None if not passed

# Safe — no KeyError even if color, size, or label are omitted
widget1 = MyWidget(color="red")
widget2 = MyWidget()

# NOTE: Use .config() to set multiple widget attributes after instantiation
# instead of setting them one at a time. This is cleaner and more efficient.
#   e.g. button.config(text="Click me", bg="blue", fg="white", font=("Arial", 12))
# This is also useful when you need to UPDATE a widget's appearance later
# in the program (e.g. changing a button's text or color on a button click).