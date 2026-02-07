# Day 19: Turtle Event Listeners - Etch-A-Sketch & Turtle Race

## Project Description
Two interactive turtle graphics programs demonstrating event-driven programming in Python. The first is an Etch-A-Sketch style drawing tool controlled by keyboard inputs. The second is an animated turtle racing game where users can bet on which turtle will win, featuring custom turtle classes, random movement, and winner announcement.

## Concepts Covered
- **Event Listeners**: Using `screen.listen()` and `screen.onkey()` for keyboard event handling
- **Higher-Order Functions**: Passing functions as arguments without parentheses
- **Custom Classes with Inheritance**: Extending the `Turtle` class to create `MyTurtle` with custom behaviors
- **Object-Oriented Design**: Creating multiple instances of custom turtle objects
- **Dictionary Data Structures**: Managing multiple turtle objects with name-based lookup
- **Global State Management**: Using global variables to control game state
- **Timer Events**: Using `screen.ontimer()` for animation loops
- **User Input Dialogs**: Getting user input with `screen.textinput()`
- **Conditional Logic**: Checking win conditions and validating user input
- **Random Module**: Generating random movement distances and speeds
- **Coordinate Calculations**: Positioning objects relative to screen boundaries
- **Text Rendering**: Using turtle's `write()` method for on-screen text display

## Program 1: Etch-A-Sketch (Exercise)

### Key Features
- Keyboard-controlled turtle drawing
- W/S: Move forward/backward
- A/D: Turn counter-clockwise/clockwise
- C: Clear screen and reset
- Demonstrates event binding and callback functions

### What I Learned
This exercise reinforced event-driven programming concepts. The key insight was understanding higher-order functions - passing function references (without parentheses) to `screen.onkey()` so they're called later when the key is pressed. The `screen.listen()` method activates the screen to receive keyboard events, enabling interactive control of the turtle.

## Program 2: Turtle Race (Main Project)

### Key Features
- 5 racing turtles with distinct colors and names (Lottie, Tilly, Pepper, Delilah, Tygra)
- User betting system with input validation
- Random movement with varying speeds for realistic racing
- Finish line drawn dynamically based on screen dimensions
- Winner announcement with personalized message based on user's bet
- Trail dots showing turtle paths
- Label display showing turtle names and numbers

### What I Learned
This project demonstrates practical application of OOP principles through class inheritance. The `MyTurtle` class extends Python's `Turtle` class, adding custom attributes (`name`, `rgb_color`) and methods (`move_forwards_random()`). This shows how inheritance allows building specialized objects from existing classes.

**Key technical implementations:**

1. **Dynamic Screen Layout**: Functions like `get_width_boundaries()` and `get_height_boundaries()` calculate positions relative to screen size, making the game work on any window dimensions. The finish line and starting positions are calculated as percentages of screen dimensions rather than hardcoded values.

2. **Animation Loop**: The `race()` function uses `screen.ontimer()` to create a repeating animation loop with 100ms intervals. This recursive timer approach provides smooth animation while allowing the game to check win conditions after each movement cycle.

3. **Win Condition Management**: The global `game_active` flag controls the race state. Each turtle's movement triggers `check_winner()`, which stops the race when any turtle crosses the finish line. This prevents multiple winners and ensures clean game termination.

4. **Random Movement Strategy**: Turtles use both random speeds (from `speed_list`) and random distances (1-50 pixels) for each move, creating unpredictable but fair racing dynamics. The dot trail provides visual feedback of movement patterns.

5. **User Interaction Flow**: The game validates user input (case-insensitive, checks against valid names) and displays the user's selection in the chosen turtle's color, reinforcing the betting choice visually before the race begins.

The dictionary structure (`turtle_dict`) allows efficient lookup and iteration over all racing turtles, demonstrating practical use of key-value data structures for managing multiple objects.

## How to Run

**Etch-A-Sketch:**
```bash
python main1.py
```

**Turtle Race:**
```bash
python main2.py
```

## Requirements
No external packages required - uses Python standard library only

## Sample Output

**Etch-A-Sketch:**
User draws by pressing W/A/S/D keys, creating custom drawings on a blank canvas.

**Turtle Race:**
```
Welcome to the turtle race!

[Input dialog appears]
Which turtle will win?
Lottie, Tilly, Pepper, Delilah, Tygra

You picked Tilly to win.

[Race animation with colored turtles moving toward finish line]

Tilly Wins!
You guessed correctly!
```

## Notes

**Design Decisions:**

*Etch-A-Sketch:*
- Small movement increments (10 units) provide precise control
- `t.reset()` clears both drawing and turtle position for fresh starts
- Simple key mapping (WASD) follows common gaming controls

*Turtle Race:*
- 5 turtles provide good balance between visual clarity and competition
- Color codes are manually selected for visual distinction on black background
- 75-pixel vertical spacing between turtles prevents overlap
- Finish line positioned at 80% of screen width to allow racing distance
- Text labels positioned above turtles for clear identification
- Speed variation (0, 1, 3, 6, 10) creates realistic race dynamics where turtles alternate between fast bursts and slower movement

**Custom Color Generation:**
The `generate_list_of_visually_distinct_colors()` function creates RGB colors with one dominant channel (red, green, or blue), ensuring visual distinction between turtles. However, the final implementation uses predefined `color_codes` for consistent, aesthetically pleasing colors.

**Future Enhancement Ideas:**
- Add obstacle course elements (barriers, speed boosts)
- Track race statistics (fastest lap, closest finish)
- Implement different race tracks (oval, figure-8)
- Add multiple rounds with point scoring
- Difficulty settings (number of turtles, race distance)
- Sound effects for race start and finish
- Turtle "personalities" (consistent fast/slow/erratic behavior)

---
*Part of the 100 Days of Code - The Complete Python Pro Bootcamp*