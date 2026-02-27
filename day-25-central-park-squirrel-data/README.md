# Squirrel Census — Fur Color Analysis

An intermediary pandas exercise using the [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) dataset.

## What it does

Reads the squirrel sighting data, groups it by primary fur color, and exports a summary count to `squirrel_count_by_color.csv`.

**Output example:**

| Primary Fur Color | count | distinct_count |
|---|---|---|
| Black | 103 | 103 |
| Cinnamon | 392 | 392 |
| Gray | 2473 | 2473 |

> Note: "Cinnamon" is the dataset's label for red/reddish squirrels.

## Requirements

- Python 3.x
- pandas

```
pip install pandas
```

## Pandas techniques used

- `pd.read_csv()` with `usecols` to load only the needed columns
- `groupby()` + `agg()` to count total and distinct squirrel IDs per fur color
- `to_csv()` to export a DataFrame directly to CSV
- `agg("count")` and `agg("nunique")` on the full DataFrame for overall totals

## Usage

Place the census CSV in the same directory as the script and run:

```
python main.py
```