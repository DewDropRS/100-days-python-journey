# Day 25 — U.S. States Game

## Project Description

An interactive geography quiz game built with Python's Turtle graphics module. The player is prompted to name all 50 U.S. states. Each correct answer places the state name on its location on a map of the United States.

---

## Key Features

- Interactive on-screen text input for user guesses
- Input normalization — strips extra spaces and corrects capitalization
- State name lookup against a CSV dataset using pandas
- Turtle graphics writes each correct state name directly onto the map in green
- Score tracker displayed in the input prompt title
- If player names all 50 states then congratulations is printed to screen
- If player quits because they can no longer name more states then states not guessed will appear on the map in red as well as the final score
- If player was not able to guess some states, those states are saved to a csv file for learning

---

## Concepts Covered

- Turtle graphics (`Screen`, `Turtle`, `textinput`, `goto`, `write`)
- pandas DataFrames (`read_csv`, boolean filtering, `.squeeze()`)
- Input normalization with `str.split()` and `str.join()`
- List comprehensions for dictionary lookups
- Functions and modularity
- While loops with break conditions

---

## What I Learned

### Input Normalization
Using `.split()` with no arguments removes all extra whitespace and splits on any whitespace character. Rejoining with a single space normalizes internal spacing in one clean line:
```python
answer = ' '.join(answer.split()).title()
```

### DataFrame vs Dictionary — Method Differences
When checking if a value exists, the syntax differs depending on the data structure:

| Structure | Check membership | Get values |
|---|---|---|
| DataFrame | `df["col"].values` | no parentheses — it's a property |
| Dictionary | `dict.values()` | parentheses required — it's a method |

Confusing these causes a `TypeError: argument of type 'builtin_function_or_method' is not iterable`.

### DataFrame Row Lookup with `.squeeze()`
Filtering a DataFrame returns a new DataFrame, even if only one row matches. `.squeeze()` flattens a single-row DataFrame into a Series so you can access columns directly:
```python
# Without squeeze — need .values[0] to extract
x = df[df["state"] == user_input]["x"].values[0]

# With squeeze — access column directly
row = df[df["state"] == user_input].squeeze()
x = row["x"]
```

### List Comprehensions
A list comprehension builds a list in a single line using the structure:
```python
[expression for item in iterable if condition]
```
Used here to find the index of a matching state in a dictionary:
```python
# items() returns each key-value pair as a tuple (index, state_name)
# k and v unpack each tuple into key and value
# [0] grabs the first (and only) match
idx = [k for k, v in states_dict["state"].items() if v == user_input][0]
```
Equivalent for loop:
```python
for k, v in states_dict["state"].items():
    if v == user_input:
        idx = k
        break
```

### Two Approaches to Map Updates
The project intentionally keeps both implementations for reference:

**Dictionary approach** (`update_map`) — uses a list comprehension to find the index, then accesses x/y from the nested dictionary.

**DataFrame approach** (`update_map_alternate`) — filters the DataFrame directly and uses `.squeeze()` for clean column access. More readable and idiomatic for pandas workflows.

---

## How to Run

1. Install dependencies:
```bash
pip install pandas
```

2. Make sure the following files are in the same directory:
   - `main.py`
   - `50_states.csv`
   - `blank_states_img.gif`

3. Run the script:
```bash
python main.py
```

4. Type state names into the input prompt. Spelling and capitalization are corrected automatically.

## Possible Future Enhancements

- **Wrong answer limit** — allow only 3 incorrect guesses before the game ends, displaying a "Game Over" message with your final score
- **Timed mode** — give the player 5 minutes to name as many states as possible, using Python's `time` module to track elapsed time and display a countdown
- **No repeats** — track already-guessed states in a list and notify the player if they enter a state they've already named
- **Give up / reveal option** — let the player type "quit" to end the game early and have the turtle write all remaining unguessed states on the map in a different color
- **High score tracker** — save the player's best score and time to a text file and display it at the start of each game as a personal best to beat