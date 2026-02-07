# Day 22: Pong Arcade Game

## Project Description
A faithful recreation of the classic Pong arcade game using Python's Turtle graphics module with modern enhancements. This two-player game features smooth paddle controls, realistic ball physics with acceleration, customizable winning scores, and a "win by 2" rule. The game includes a replay system and pays homage to Allan Alcorn's original 1972 Atari creation.

## Concepts Covered
- **Object-Oriented Programming**: Multiple custom classes (`Paddle`, `Ball`, `Scoreboard`) with inheritance
- **Class Inheritance**: Extending `Turtle` class for game objects
- **Event Handling**: Both `onkeypress` and `onkeyrelease` for smooth paddle control
- **Higher-Order Functions**: Passing functions as arguments to event handlers
- **Game Loop**: Implementing 60 FPS game loop with `time.sleep(0.016)`
- **Collision Detection**: Distance-based and coordinate-based collision checking
- **Boundary Constraints**: Keeping paddles within playable area
- **Ball Physics**: Velocity vectors, bouncing mechanics, and acceleration
- **State Management**: Using `nonlocal` to control game state in nested functions
- **Input Validation**: Validating and sanitizing user input for winning score
- **Recursion**: Using recursive function call for game replay functionality
- **Modular Design**: Separating game logic across multiple files

## Key Features
- Two-player gameplay (Right player: Up/Down arrows, Left player: A/Z keys)
- Smooth paddle movement with press-and-hold controls
- Ball physics with gradual acceleration after each paddle hit (×1.2 multiplier)
- Random initial ball trajectory for variety
- Center dashed line dividing the play field
- Real-time score tracking
- **Enhanced: Customizable winning score** (3-21 points)
- **Enhanced: "Win by 2" rule** - prevents one-point victories
- **Enhanced: "Press SPACE to start"** - controlled game initiation
- **Enhanced: Play again functionality** - replay without restarting program
- Boundary detection keeps paddles on screen
- 1-second pause after each score for player readiness

## What I Learned
This project demonstrates implementing classic arcade game mechanics using object-oriented Python. The modular architecture separates game components effectively:
- `Paddle` class manages paddle state, movement, and boundary constraints
- `Ball` class handles ball physics, collision responses, and reset logic
- `Scoreboard` class manages score display and game over messaging
- `main.py` orchestrates game flow, collision detection, and win conditions

**Key technical implementations:**

1. **Smooth Paddle Control**: Using both `onkeypress` and `onkeyrelease` creates responsive controls. The paddle's `direction` attribute (1, -1, or 0) acts as a multiplier, enabling continuous movement while a key is held:
```python
screen.onkeypress(paddle.start_move_up, "Up")    # Sets direction = 1
screen.onkeyrelease(paddle.stop_move, "Up")       # Sets direction = 0
```

2. **Ball Physics and Acceleration**: The ball maintains separate x and y velocity components. After each paddle collision, `bounce_x()` multiplies velocity by -1.2, reversing direction and increasing speed by 20%. This creates progressively faster gameplay similar to the original Pong.

3. **Collision Detection Strategy**: Combines two approaches:
   - Distance-based: `ball.distance(paddle) < 50` detects general proximity
   - Position-based: `ball.xcor() > 330` ensures ball is actually at paddle location
   
   This dual check prevents false collisions when the ball passes behind the paddle.

4. **Boundary Constraints**: Paddles check their position before moving, accounting for paddle dimensions:
```python
if top_boundary - half_height - buffer > new_y > bottom_boundary + half_height + buffer:
    move to new_y
```

5. **Win by 2 Rule**: The win condition checks both minimum score threshold AND score difference:
```python
if (score >= winning_score) and abs(left_score - right_score) >= 2:
    game_over()
```

6. **Game State Management**: Uses `nonlocal` in the nested `start_game()` function to modify the outer scope's `game_is_on` variable, demonstrating Python's closure mechanics.

7. **60 FPS Game Loop**: `time.sleep(0.016)` creates approximately 60 frames per second (1/60 ≈ 0.016), providing smooth animation consistent with modern gaming standards.

8. **Replay System**: The `play_game()` function calls itself recursively for replays, with `screen.clear()` resetting the display. This provides a seamless restart without program termination.

## How to Run
```bash
python main.py
```

**Gameplay:**
1. Enter target score (3-21, must be odd for "win by 2" rule)
2. Press SPACE to start the game
3. Right player uses Up/Down arrows, left player uses A/Z keys
4. First player to reach target score with 2-point lead wins
5. Choose to play again or exit

## Requirements
No external packages required - uses Python standard library only

## File Structure
```
day-022-pong-game/
├── main.py           # Game loop, collision detection, win conditions
├── paddle.py         # Paddle class with movement and boundary logic
├── ball.py           # Ball class with physics and collision responses
└── scoreboard.py     # Scoreboard class for score display
```

## Controls
**Right Player (Right side):**
- Up Arrow: Move paddle up
- Down Arrow: Move paddle down

**Left Player (Left side):**
- A key: Move paddle up
- Z key: Move paddle down

**Game Control:**
- SPACE: Start game

## Sample Gameplay
```
[Game Setup dialog]
Enter the target score between 3 and 21 (must win by 2 points): 7

Press SPACE to start

[Gameplay with real-time score display]
Left: 4    Right: 3

[Ball accelerates with each paddle hit]

Left: 7    Right: 5
Game Over

Play again? (yes/no): yes
```

## Notes

**Enhancements Beyond Course Requirements:**

1. **Customizable Winning Score**: Players can set target scores between 3-21 points, with input validation ensuring odd numbers for the "win by 2" rule.

2. **Win by 2 Rule**: Prevents anticlimactic one-point victories, requiring a 2-point lead for competitive matches similar to tennis/ping pong rules.

3. **Controlled Start**: "Press SPACE to start" message gives players time to position hands on controls before gameplay begins.

4. **Replay Functionality**: Seamless replay system without program restart, enhancing user experience.

5. **Press-and-Hold Controls**: Using `onkeypress`/`onkeyrelease` instead of just `onkey` provides smoother, more responsive paddle control.

**Design Decisions:**
- 60 FPS (0.016s sleep) provides smooth animation
- Ball acceleration (×1.2 per hit) creates increasing difficulty
- Random initial y-velocity adds variety to each game
- 1-second pause after scoring allows player reaction time
- Paddles positioned at x=±350 (not at screen edge) for realistic gameplay
- Collision detection uses 50-pixel threshold to account for paddle height
- Center dashed line created procedurally for any screen height

**Historical Context:**
The title credits Allan Alcorn, who developed the original Pong for Atari in 1972. Pong was one of the first commercially successful video games and launched the arcade gaming industry.

**Future Enhancement Ideas:**
- Single-player mode with AI opponent
- Difficulty levels (ball speed, paddle size)
- Power-ups (larger paddle, slower ball, extra points)
- Sound effects for paddle hits and scoring
- Particle effects on collisions
- Ball spin mechanics based on paddle movement
- Tournament mode with multiple rounds
- High score persistence
- Different ball speeds for serves
- Angle variation based on where ball hits paddle
- Visual paddle "charge" indicator
- Multiplayer online functionality

---
*Part of the 100 Days of Code - The Complete Python Pro Bootcamp*