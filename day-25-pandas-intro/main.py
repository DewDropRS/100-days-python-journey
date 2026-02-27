# import the csv module
import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # save column names for reference
#     column_names = next(data)
#      # skip header which are column names
#     next(data)
#     temperatures = []
#     for row in data:
#         temperature = int(row[1])
#         temperatures.append(int(temperature))
#
# print(f"column names: {column_names}")
# print(f"temperatures: {temperatures}")
import pandas
# Better to use pandas library
# Additional parameters can be included. See the README file for some examples.
#https://pandas.pydata.org/docs/
import pandas as pd
# #data_file is a DataFrame
data_file = pd.read_csv("weather_data.csv" )
print(data_file)
temperatures = data_file["temp"]
print(temperatures)
print(temperatures.describe())

# A series is like the entire column from your csv file
# A series is like a list

# pandas.DataFrame.to_dict()
data_file = pd.read_csv("weather_data.csv" )
data_dict = data_file.to_dict()
print(data_dict)
# {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
#  'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
#  'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

# data_file["temp"] is a series so now you can do series things to it
temp_list = data_file["temp"].to_list()
print(temp_list)

# getting mean, describe of the temp series
print(data_file["temp"].mean())
print(data_file["temp"].describe())

#get ahold of columns quickly by accessing them as the dataframe attributes
# case-sensitive
print(data_file.condition)

#Filter data row-wise
# remember that data_file.temp is a series
print(data_file[data_file.day == "Tuesday"]) # this returns the entire row for Tuesday
print(data_file[data_file.temp == data_file.temp.max()]) # this returns the entire row where temperature is at the max

tuesday = data_file[data_file.day == "Tuesday"]
print(tuesday.condition) # print only the condition of the Tuesday row

#get temperature and covert to Fahrenheit
data_file["temp_fahrenheit"] = data_file.temp * 9/5 + 32
monday = data_file[data_file.day == "Monday"]
print(f"Monday's temperature in Fahrenheit: {monday.temp_fahrenheit}")

# create a dataframe from a dictionary
data_dict2 = {
    "students": ["Paul", "Randy", "Aaron"],
    "scores": [76,56,65]
}
data = pandas.DataFrame(data_dict2)
print(data)
data.to_csv("new_data.csv")