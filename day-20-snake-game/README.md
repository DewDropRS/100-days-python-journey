# Day 20: Snake Game

## Project Description
A classic Snake game implementation using Python's Turtle graphics module with object-oriented design. Players control a snake that grows longer as it eats colorful food pellets, with progressive difficulty through increasing speed. The game features collision detection for walls and self-collision, dynamic color changes, and intelligent food spawning that avoids placing food on the snake's body.

## Concepts Covered
- **Object-Oriented Programming**: Multiple custom classes (`Snake`, `Food`, `Scoreboard`, `MyTurtle`) with inheritance
- **Class Inheritance**: Extending `Turtle` class to create specialized `MyTurtle`, `Food`, and `Scoreboard` classes
- **Modular Code Organization**: Separating game logic across multiple files for maintainability
- **List Slicing**: Using `snake.segments[1:]` to check tail collisions
- **Game Loop**: Implementing main game loop with `while` and `time.sleep()` for speed control
- **Collision Detection**: Distance-based detection for food collection and self-collision
- **Boundary Detection**: Checking coordinates against screen limits
- **Event Handling**: Keyboard input for directional control using arrow keys
- **Screen Control**: Using `screen.tracer(0)` and `screen.update()` for smooth animation
- **Dynamic Difficulty**: Progressive speed increase based on score
- **Color Management**: RGB color codes and random color selection
- **List Comprehension**: Filtering available colors to ensure variety

## Key Features
- Classic snake movement with arrow key controls
- Snake grows by one segment with each food pellet eaten
- Score tracking displayed in real-time
- **Enhanced: Progressive speed increase** - game gets faster as score increases
- **Enhanced: Color-changing snake** - snake adopts the color of eaten food
- **Enhanced: Smart food spawning** - ensures food never spawns on snake's body
- **Enhanced: Color variety** - each new food pellet has a different color than the previous
- Boundary collision detection (hitting walls ends game)
- Self-collision detection (hitting own body ends game)
- Movement restrictions prevent snake from reversing into itself
- Game over screen with final score

## What I Learned
This project reinforced Object-Oriented Programming through practical game development. The modular architecture separates concerns effectively:
- `Snake` class manages snake state and movement logic
- `Food` class handles food positioning and color
- `Scoreboard` class manages score display and game over messaging
- `MyTurtle` class provides a reusable turtle with consistent initial properties

**Key technical implementations:**

1. **Snake Movement Algorithm**: The snake moves by updating each segment to the position of the segment in front of it, starting from the tail. This creates the classic "follow the leader" snake movement:
```python
for seg_num in range(len(self.segments) - 1, 0, -1):
    self.segments[seg_num].setpos(*self.segments[seg_num - 1].pos())
self.segments[0].forward(MOVE_STEP)
```

2. **Movement Restrictions**: Directional methods check current heading before allowing turns, preventing the snake from reversing into its own body. For example, if heading down (270°), the snake cannot turn up (90°).

3. **Progressive Difficulty**: The speed calculation `max(0.02, base_speed - (scoreboard.score * 0.005))` creates accelerating difficulty. Each point reduces sleep time by 0.005 seconds, with a minimum of 0.02 seconds to maintain playability.

4. **Smart Food Placement**: The `refresh()` method uses a while loop to continuously generate random positions until finding one that doesn't overlap with any snake segment:
```python
while True:
    random_x, random_y = # generate random position
    if not overlapping with snake:
        place food and break
```

5. **Color Management Enhancement**: Food color selection excludes the previous color using list comprehension, ensuring visual variety between consecutive food pellets.

6. **Collision Detection**: Uses turtle's `distance()` method with threshold values (15 for food, 10 for self-collision, 5 for boundary buffer) to detect various collision types accurately.

The use of `screen.tracer(0)` and `screen.update()` provides smooth animation by controlling when the screen refreshes, eliminating flickering that would occur with automatic updates.

## How to Run
```bash
python main.py
```

## Requirements
No external packages required - uses Python standard library only

## File Structure
```
day-020-snake-game/
├── main.py           # Main game loop and collision detection
├── snake.py          # Snake class with movement and growth logic
├── food.py           # Food class with positioning and color management
├── scoreboard.py     # Scoreboard class for score display
└── myturtle.py       # Base MyTurtle class for consistent turtle creation
```

## Sample Gameplay
- Use arrow keys to control snake direction
- Snake starts with 3 segments
- Eating food adds 1 segment and 1 point to score
- Game speed increases progressively with score
- Snake changes color to match eaten food
- Game ends when snake hits wall or its own body
- Final score displayed at game over

## Notes

**Enhancements Beyond Course Requirements:**

1. **Progressive Speed Increase**: Game difficulty scales with score through decreasing sleep intervals, creating increasingly challenging gameplay.

2. **Color-Changing Snake**: Snake adopts the color of each food pellet it eats, providing visual feedback and making the game more engaging.

3. **Smart Food Spawning**: Food never spawns on the snake's body, preventing unfair food placement that could appear unreachable.

4. **Food Color Variety**: Each new food pellet guarantees a different color from the previous one, ensuring visual distinction.

**Design Decisions:**
- 20-pixel movement increments align with turtle's default size for precise collision detection
- Buffer zones (5-10 pixels) around boundaries and collision detection prevent edge case glitches
- Color palette limited to 7 distinct, vibrant colors for clear visibility on black background
- Minimum speed threshold (0.02 seconds) prevents game from becoming unplayable at high scores
- Score displayed in top-right corner to avoid obstructing gameplay area

**Future Enhancement Ideas:**
- High score persistence using file I/O
- Multiple difficulty levels (easy, medium, hard)
- Power-ups (speed boost, invincibility, score multiplier)
- Obstacles and maze layouts
- Two-player competitive mode
- Sound effects for eating and collisions
- Pause functionality
- Different snake skins/themes
- Achievement system
- Leaderboard with player names

---
*Part of the 100 Days of Code - The Complete Python Pro Bootcamp*