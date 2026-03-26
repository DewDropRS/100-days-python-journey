# NATO Phonetic Alphabet Converter

A Python script that takes a user-entered word and returns the corresponding NATO phonetic alphabet codes (e.g., "Hi" → `['Hotel', 'India']`).

---

## What It Does

- Reads NATO phonetic alphabet data from a CSV file into a Pandas DataFrame
- Builds a lookup dictionary from that DataFrame using dictionary comprehension
- Prompts the user to enter a word
- Returns the NATO phonetic equivalent as a list
- Handles invalid input (numbers, symbols) using exception handling

---

## Concepts Practiced

### Dictionary Comprehension from a DataFrame

```python
nato_phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
```

**What this line does:**

`df.iterrows()` loops through each row of the DataFrame, returning a tuple of `(index, row)` for every row. Each `row` is a Pandas Series, so you can access columns by name as attributes — `row.letter` and `row.code`.

The comprehension builds a dictionary where:
- **Key** = `row.letter` — the letter column value (e.g., `"A"`)
- **Value** = `row.code` — the NATO code column value (e.g., `"Alfa"`)

The general pattern is:
```python
new_dict = {new_key:new_value for (index, row) in df.iterrows()}
```

So the result looks like:
```python
{'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', ...}
```

---

### Exception Handling with `try / except / else`

```python
try:
    if not user_input.replace(" ", "").isalpha():
        raise ValueError("Name must contain letters only.")

except ValueError as e:
    print(f"Invalid input: {e}")
    generate_nato_phonetic()  # recursively re-prompts the user

else:
    # runs only if no exception was raised
    nato_phonetic_result = [nato_phonetic_dict[letter] for letter in user_input_list]
    print(nato_phonetic_result)
```

| Block | When it runs |
|---|---|
| `try` | Always — this is where you put the code that might fail |
| `except` | Only if an exception is raised in `try` |
| `else` | Only if **no** exception was raised |
| `finally` | Always, error or not (optional, not used here) |

The script uses **recursion** in the `except` block to re-prompt the user instead of crashing.

---

### List Comprehension

Used in two places:

```python
# Uppercase each letter of user input
user_input_list = [letter.upper() for letter in user_input]

# Look up each letter in the NATO dictionary
nato_phonetic_result = [nato_phonetic_dict[letter] for letter in user_input_list]
```

---

## Example Output

```
Enter a word: Hi
['Hotel', 'India']

Enter a word: 123
Invalid input: Name must contain letters only.
Enter a word:
```

---

## Files

| File | Description |
|---|---|
| `main.py` | Main script |
| `nato_phonetic_alphabet.csv` | Source data with `letter` and `code` columns |