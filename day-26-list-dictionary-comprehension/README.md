# Day 26 - List & Dictionary Comprehension

## Overview
This project covers Python list and dictionary comprehension techniques, conditional filtering, file I/O with comprehensions, and an introduction to iterating over Pandas DataFrames.

---

## Concepts Covered

### List Comprehension
A concise way to build lists from existing iterables, replacing traditional `for` loops.

```python
# Basic syntax
new_list = [new_item for item in list]

# Example: increment each number
new_list = [n + 1 for n in numbers]
```

- Works with strings, ranges, and any iterable
- Much more readable and Pythonic than appending in a loop

### Conditional List Comprehension
Filter items while building the list using an `if` clause.

```python
# Syntax
new_list = [new_item for item in list if condition]

# Example: names shorter than 5 characters
short_names = [name for name in names if len(name) < 5]
```

### Data Overlap Exercise
Reads two `.txt` files (one value per row) and finds common values using conditional list comprehension.

```python
with open('file1.txt', 'r') as f1:
    file1 = f1.readlines()
with open('file2.txt', 'r') as f2:
    file2 = f2.readlines()

result = [int(n) for n in file1 if n in file2]
```

---

### Dictionary Comprehension
Build dictionaries from lists or other dictionaries in a single expression.

```python
# From a list
new_dict = {new_key: new_value for item in list}

# From another dictionary
new_dict = {new_key: new_value for (key, value) in dict.items()}
```

> **Reminder:** Use `.items()` to unpack both key and value when iterating over a dictionary.
> - `.keys()` → just the keys
> - `.values()` → just the values
> - `.items()` → key-value pairs (needed for unpacking)

**Examples:**
- Generate random student scores from a list of names
- Filter passing students (score >= 60)
- Count word lengths in a sentence using `.split()`
- Convert Celsius temps to Fahrenheit across a weekly dictionary

---

### Pandas DataFrame from Dictionary
Convert a dictionary into a tabular DataFrame using `.items()` for proper row-based formatting.

```python
# Using .items() gives each student their own row with named columns
student_data_frame = pd.DataFrame(student_dict.items(), columns=['student', 'score'])
```

> **Note:** `pd.DataFrame()` with scalar values requires `index=[0]` in newer pandas versions.
> Using `.items()` avoids this issue entirely and produces a cleaner, row-based structure.

### Iterating Over DataFrame Rows
Use `.iterrows()` to loop through each row and access values by column name.

```python
for (index, row) in student_data_frame.iterrows():
    if row.student == "Tygra":
        print(row.score)
```

---

## Libraries Used
- `random` — generate random integers
- `pandas` — create and iterate over DataFrames

## Files
| File | Description |
|------|-------------|
| `main.py` | Main script with all exercises |
| `file1.txt` | Input file for data overlap exercise |
| `file2.txt` | Input file for data overlap exercise |

---

## Part of
[100 Days of Code - Python](https://github.com/RSegu/100-days-python-journey)