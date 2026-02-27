# The goal of this project is to create a squirrel_count.csv file
# something like this:
# primary fur color, red is cinnamon
# color, count
# 0,grey,2473
# 1,red,392
# 2,black,103

import pandas as pd
pd.set_option("display.max_columns", None)  # show all columns
pd.set_option("display.max_rows", None)     # show all rows
pd.set_option("display.max_colwidth", None) # show full content of each cell

squirrel_df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260218.csv",
                          usecols = ["Unique Squirrel ID", "Primary Fur Color"])
squirrel_df["Primary Fur Color"] = squirrel_df["Primary Fur Color"].replace("Cinnamon", "Red")
print(squirrel_df.head())

#aggregate by fur color
grouped_by_color_stats = squirrel_df.groupby("Primary Fur Color").agg(
    count=("Unique Squirrel ID", "count"),
    distinct_count = ("Unique Squirrel ID", "nunique"),
)
grouped_by_color_stats.to_csv("squirrel_count_by_color.csv")
sightings_total = squirrel_df.agg("count")
sightings_unique = squirrel_df.agg("nunique")
print(f"Grouped stats: {grouped_by_color_stats}\n"
      f"Total sightings:{sightings_total}\n"
      f"Total unique sightings: {sightings_unique}")

