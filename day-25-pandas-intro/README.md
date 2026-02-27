# Pandas Introduction — Project Notes

A beginner project introducing the pandas library as a better alternative to Python's built-in `csv` module for working with tabular data.

**Docs:** https://pandas.pydata.org/docs/

---

## Reading a CSV with the `csv` Module (the old way)

Before pandas, you'd read a CSV manually like this:

```python
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    column_names = next(data)  # save header row
    next(data)                 # skip header before looping
    temperatures = []
    for row in data:
        temperatures.append(int(row[1]))
```

Pandas makes this much simpler and more powerful.

---

## Reading a CSV with Pandas

```python
import pandas as pd

data_file = pd.read_csv("weather_data.csv")
print(data_file)  # prints the full DataFrame
```

`pd.read_csv()` returns a **DataFrame** — a table-like structure made up of rows and columns.

### Useful `pd.read_csv()` Parameters

#### Basics
```python
df = pd.read_csv("file.csv",
    header=0,           # row to use as column names (0 = first row, default)
    index_col=0,        # column to use as the row index
    usecols=["a","b"],  # only load specific columns (saves memory)
    nrows=100,          # only read the first N rows (great for previewing big files)
    skiprows=2,         # skip N rows from the top
)
```

#### Data Types & Missing Values
```python
df = pd.read_csv("file.csv",
    dtype={"age": int, "salary": float},  # enforce column types explicitly
    na_values=["N/A", "none", "--"],       # treat these strings as NaN
    keep_default_na=True,                  # whether pandas auto-detects nulls (default True)
)
```

#### Formatting
```python
df = pd.read_csv("file.csv",
    sep="\t",                  # delimiter — use for TSV files or pipe-separated ("|")
    encoding="utf-8",          # handle special characters (also try "latin-1" if utf-8 fails)
    thousands=",",             # treat commas in numbers like 1,000 → 1000
    parse_dates=["date_col"],  # auto-parse a column as datetime
)
```

#### Large Files
```python
df = pd.read_csv("file.csv",
    chunksize=10000,  # returns an iterator of DataFrames instead of loading all at once
)
```

**Most commonly used day-to-day:** `usecols`, `dtype`, `na_values`, `sep`, `parse_dates`

---

## DataFrames and Series

- A **DataFrame** is the entire table (rows + columns)
- A **Series** is a single column from that table — it has special pandas methods available

```python
# Selecting a column returns a Series
temperatures = data_file["temp"]

# You can also access columns as attributes (case-sensitive)
print(data_file.condition)
```

> ⚠️ `data_file.to_dict()` converts the DataFrame to a plain Python dictionary.
> Once converted, columns are no longer Series and pandas methods won't work on them.
> Always index the DataFrame directly to get a Series: `data_file["temp"]`

---

## Useful Series Methods

```python
data_file["temp"].mean()        # average
data_file["temp"].max()         # maximum value
data_file["temp"].min()         # minimum value
data_file["temp"].describe()    # summary stats (count, mean, std, min, max, etc.)
data_file["temp"].to_list()     # convert Series to a plain Python list
```

---

## Converting a DataFrame to a Dictionary

```python
data_dict = data_file.to_dict()
# Returns nested dicts: {'temp': {0: 12, 1: 14, ...}, 'day': {0: 'Monday', ...}}
```

---

## Filtering Rows

```python
# Returns the entire row where day == "Tuesday"
data_file[data_file.day == "Tuesday"]

# Returns the entire row where temp is at its maximum
data_file[data_file.temp == data_file.temp.max()]

# Chain to get a specific column from a filtered row
tuesday = data_file[data_file.day == "Tuesday"]
print(tuesday.condition)
```

---

## Adding a Calculated Column

Math operations on a Series are **vectorized** — they apply to every row automatically with no loop needed.

```python
# Convert Celsius to Fahrenheit and store as a new column
data_file["temp_fahrenheit"] = data_file.temp * 9/5 + 32

# Access the new column for a specific row
monday = data_file[data_file.day == "Monday"]
print(monday.temp_fahrenheit)
```

---

## Creating a DataFrame from a Dictionary

```python
data_dict2 = {
    "students": ["Paul", "Randy", "Aaron"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict2)
print(data)
```

---

## Exporting a DataFrame to CSV

```python
data.to_csv("new_data.csv")
```