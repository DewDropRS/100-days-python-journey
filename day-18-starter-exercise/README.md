# Day 18: Turtle Graphics - Starter Exercises

## Project Description
A series of progressive turtle graphics challenges exploring Python's turtle module, culminating in a random walk program with boundary constraints. The exercises progress from basic shapes to dynamic, colorful random walks that stay within the canvas boundaries.

## Concepts Covered
- **Turtle Graphics Module**: Creating visual graphics with Python's turtle library
- **Import Syntax Variations**: Understanding different import methods and their trade-offs
- **Random Module**: Generating random integers for colors and directions
- **RGB Color Mode**: Working with RGB tuples (0-255) for precise color specification
- **Loops with Range**: Creating repeating patterns and shapes
- **Functions with Parameters**: Encapsulating drawing logic in reusable functions
- **Boundary Detection Logic**: Calculating and checking screen limits to constrain movement
- **Coordinate System**: Understanding turtle positioning with `xcor()` and `ycor()`
- **Conditional Movement**: Using if/else to validate moves before execution
- **Event Handling**: Implementing mouse click events to stop execution
- **Global State Management**: Using global variables for user interaction control
- **Turtle Speed Control**: Optimizing performance with speed settings

## Challenges Completed

### Challenge 1: Draw a Square
Basic turtle movement with color cycling through each side.

### Challenge 2: Draw a Dashed Line
Creating dashed patterns using `penup()` and `pendown()` methods.

### Challenge 3: Draw Polygons
Algorithmic shape generation - drawing polygons from triangles (3 sides) through dodecagons (12 sides) with random colors for each edge. Demonstrates calculating interior angles: `360/vertex_count`.

### Challenge 4: Random Walk (Main Project)
**Key Features:**
- Random directional movement in 90-degree increments (N, S, E, W)
- Random RGB color generation for each segment
- Boundary detection prevents turtle from leaving the canvas
- Thicker pen width (5 pixels) for visibility
- User can stop the walk by clicking on the canvas
- Validates each move before execution to ensure turtle stays in bounds

## What I Learned
This series of exercises demonstrated progressive complexity in turtle graphics programming. The progression from simple shapes to algorithmic polygon generation reinforced how mathematical formulas translate to visual output.

**Challenge 4 (Random Walk)** was the most substantial exercise, requiring implementation of boundary detection logic. The `is_within_bounds()` function calculates the turtle's potential new position based on heading angle and distance, then validates against screen dimensions before allowing the move. This involved:
- Understanding turtle's coordinate system (centered at origin)
- Calculating screen boundaries using `window_width()` and `window_height()`
- Predicting turtle position based on cardinal directions (0°, 90°, 180°, 270°)
- Implementing move validation to prevent off-screen drawing

The event-driven `stop_on_click()` handler demonstrates user interaction control, allowing graceful loop termination via mouse click. The global `running` variable enables clean exit from the drawing loop.

Performance optimization through strategic `speed(0)` calls during heading changes followed by `speed(6)` for visible drawing creates smooth animation while maintaining visual feedback.

## How to Run
```bash
python main.py
```

## Requirements
No external packages required - uses Python standard library only

## Sample Output
The random walk creates colorful, maze-like patterns with thick lines, changing color with each segment. The turtle moves randomly within the canvas boundaries until stopped by user click or reaching 1000 segments.

## Notes
**Code Organization:**
The commented-out challenges (1-3) remain in the code to show learning progression and can be uncommented to view those exercises.

**Design Decisions:**
- 90-degree angles only (grid-like movement) rather than arbitrary angles
- Boundary validation happens before movement (prevents partial moves off-screen)
- 20-pixel segments provide good balance between detail and performance
- 1000 iterations prevent infinite loops while allowing substantial artwork generation

**Import Best Practices Demonstrated:**
```python
# Good - explicit and clear
from turtle import Turtle, Screen, colormode

# Acceptable for very long names
import turtle as t

# Avoid - unclear origins and potential conflicts
from turtle import *
```

---
*Part of the 100 Days of Code - The Complete Python Pro Bootcamp*