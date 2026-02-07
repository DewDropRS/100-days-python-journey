# Day 18: Hirst Spot Painting Generator

## Project Description
A Python program that generates artwork inspired by Damien Hirst's iconic spot paintings using the Turtle graphics module. The program extracts colors from an actual Hirst painting image using the colorgram library, then creates a customizable grid of colorful dots with random color selection, simulating the artist's signature style.

## Concepts Covered
- **Turtle Graphics Module**: Creating visual graphics programmatically using Python's turtle library
- **Color Extraction**: Using the `colorgram` library to extract RGB color palettes from images
- **RGB Color Mode**: Working with RGB tuples for precise color specification
- **List Comprehension**: Efficiently creating lists of RGB tuples from color objects
- **Function Parameters with Defaults**: Creating flexible functions with customizable behavior
- **Nested Loops**: Using nested for loops to create grid patterns
- **Coordinate System Mathematics**: Calculating position coordinates for grid layout
- **Event Handling**: Implementing mouse click events to control program execution
- **Global Variables**: Managing state across functions for user interaction control
- **Turtle Speed & Visibility**: Optimizing drawing performance and visual output

## Key Features
- Extracts color palette from a reference Damien Hirst painting image
- Generates customizable dot grids (rows, columns, size, spacing)
- Random color selection from extracted palette
- Dynamic window sizing based on grid parameters
- Configurable border spacing
- User can stop painting by clicking on the canvas
- Fast rendering with turtle speed optimization

## What I Learned
This project demonstrates practical application of the Turtle graphics module for creating algorithmic art. The key challenge was calculating the coordinate system for centering the dot grid - determining the starting position (`first_dot_x`, `first_dot_y`) required understanding how to center a grid of arbitrary size within the canvas using the formula: `-(dots - 1) * spacing / 2`.

The `colorgram` library integration shows how Python packages can extend functionality - extracting RGB values from an actual Damien Hirst painting and converting them to turtle-compatible tuples using list comprehension. This demonstrates a real-world workflow: analyze source material → extract data → generate derivative work.

Implementing the `stop_on_click()` event handler reinforced event-driven programming concepts. The global `running` variable allows the user to interrupt the nested loops cleanly by clicking anywhere on the canvas, demonstrating graceful program control.

The `paint_like_hirst()` function design emphasizes flexibility through default parameters - users can generate anything from a simple 5x5 grid to complex 20x20 patterns by adjusting arguments. The function also handles dynamic window resizing based on the requested grid dimensions, ensuring the artwork always fits properly within the canvas.

Performance optimization through `t.speed('fastest')` and `t.hideturtle()` significantly improves rendering time for larger grids, showing attention to user experience.

## How to Run
```bash
pip install colorgram.py --break-system-packages
python main.py
```

**Note:** Ensure `damien_hirst_dot_image.jpg` is in the same directory as the script.

## Requirements
```
colorgram.py==1.2.0
```

## Sample Output
The program generates a 10x10 grid of colorful dots, each 50 pixels in diameter with 50-pixel spacing, creating a 550x550 pixel canvas with borders. Colors are randomly selected from the palette extracted from the reference Damien Hirst image.

## Notes
The implementation uses mathematical calculations to center the grid:
- Window dimensions: `(dots * spacing) + (2 * border)`
- Starting position: `-(dots - 1) * spacing / 2`

This ensures the artwork is always centered regardless of grid size.

**Design Choices:**
- Nested loops iterate row-by-row (bottom to top, left to right) mimicking how a physical artist might work
- `colormode(255)` enables standard RGB color format (0-255) rather than Turtle's default 0-1 range
- Event-driven stop mechanism allows user control without keyboard interrupts
- Function parameters with defaults balance ease of use with customization

**Future Enhancement Ideas:**
- Save generated artwork as image files (PNG, JPG)
- GUI controls for real-time parameter adjustment
- Color palette selection from multiple reference images

---
*Part of the 100 Days of Code - The Complete Python Pro Bootcamp*