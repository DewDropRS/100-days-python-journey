# Day 23: Capstone - Turtle Crossing Game

## Project Description
A Crossy Road-style arcade game using Python's Turtle graphics. Navigate a turtle across five lanes of bidirectional traffic with increasing difficulty. Features randomized traffic patterns, progressive speed increases, and replay functionality.

## Concepts Covered
- **Object-Oriented Programming**: Custom classes (`Player`, `Lane`, `Car`, `Scoreboard`)
- **Class Inheritance**: Extending `Turtle` class for game objects
- **Frame-Based Game Loop**: Managing spawning, movement, and collision detection
- **Spawn Management**: Frame counters with weighted random intervals
- **Traffic Simulation**: Independent lane management with bidirectional traffic
- **Collision Detection**: Distance-based checking across lanes
- **List Management**: Dynamic car spawning and cleanup
- **State Management**: Level progression with speed scaling
- **Recursion**: Game replay functionality

## Key Features
- Four-directional player movement (arrow keys)
- Six lanes with alternating left/right traffic.
- Randomized initial lane speeds (5-7)
- Weighted spawn intervals for realistic traffic patterns
- Anti-bunching logic prevents cars spawning too close
- Visual lane backgrounds (gray roads, grass borders)
- Lane-specific car colors
- Progressive difficulty (10% speed increase per level)
- Real-time level display
- Collision detection with replay option

## What I Learned
This project demonstrates building a traffic simulation system with multiple independent agents. Key implementations include:

1. **Frame-Based Spawning**: Each lane maintains independent counters for realistic traffic timing
2. **Weighted Random Intervals**: Uses `random.choices()` with custom weights for organic spawn patterns
3. **Anti-Bunching**: Distance checking prevents impossible car clusters
4. **Bidirectional Traffic**: Alternating lane directions with direction-specific spawn points and speeds
5. **Efficient Cleanup**: O(1) removal of off-screen cars (always checks first in list)
6. **Collision Detection**: Nested loop checks all cars across all lanes each frame
7. **Progressive Difficulty**: Multiplicative speed increase (×1.1) creates exponential scaling

## How to Run
```bash
python main.py
```

## Requirements
Python standard library only - no external packages required

## File Structure
```
day-023-turtle-crossing-capstone/
├── main.py           # Game loop, setup, collision detection
├── player.py         # Player movement and finish detection
├── lane.py           # Spawn management and car coordination
├── car.py            # Car movement
└── scoreboard.py     # Level display
```

## Controls
- **Arrow Keys**: Move turtle (Up/Down/Left/Right)

## Notes

**Key Enhancements:**
- Bidirectional traffic with multi-directional player movement (Frogger-style)
- Weighted spawn distribution creates realistic traffic flow
- Anti-bunching logic ensures fair gameplay
- Visual lane system with color-coded cars
- Randomized lane speeds for unique playthroughs
- Frame-based independent lane spawning

**Design Decisions:**
- 10 FPS for playable reaction time
- 15-pixel collision threshold
- 50-pixel minimum spawn spacing
- Multiplicative speed scaling (×1.1 per level)

**Future Enhancements:**
- Add Lives
- Add one ups
---
*Part of the 100 Days of Code - The Complete Python Pro Bootcamp*