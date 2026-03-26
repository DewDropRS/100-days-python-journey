import random
import pandas as pd

numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(f"New list using for loop: {new_list}")

# list comprehension way
# n + 1 is the expression; the "new item"
# remember this then replace with your list name and expression
# new_list = [new_item for item in list]
new_list = [n + 1 for n in numbers]
print(f"New list using List Comprehension way: {new_list}")

# works with strings too
name = "Rocio Segura Ana-Sofia"
new_list = [letter for letter in name]
print(new_list)

# works with ranges
# remember that range won't include the last number in the tuple
# exercise: double each number in range(1,5)
doubled_range_list = [n*2 for n in range(1,5)]
print(doubled_range_list)

# Conditional List Comprehension
# new_list = [new_item for item in list if test]

names =["Daniel", "Rocio", "Rosa", "Justin", "Jo", "Rick"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names_all_caps = [name.upper() for name in names if len(name) >= 5]
print(long_names_all_caps)

#exercise from exercise 17: Data Overlap
with open('file1.txt', 'r') as f1:
    file1 = f1.readlines()
with open('file2.txt', 'r') as f2:
    file2 = f2.readlines()

result = [int(n) for n in file1 if n in file2]

print(result)

# Dictionary Comprehension part 1
# new_dict = {new_key: new_vlaue for item in list}
# new dictionary based on the values of another dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items()}

names = ['Tilly', 'Lottie', 'Pepper', 'Tygra', 'Delilah']
student_scores ={student:random.randint(1,100) for student in names }
print(student_scores)

# create passed students dictionary
passed_students = {student:score for (student,score) in student_scores.items() if score >= 60 }
print(passed_students)



# Dictionary Comprehension 1
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given
# sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.  *
# *Do NOT** Create a dictionary directly.
# Try to use Dictionary Comprehension instead of a Loop.
#
# To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word.
# Note that "Swallow?" therefore has a length of 8.
# new_dict = {new_key: new_vlaue for item in list}
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# Dictionary Comprehension 2
# You are going to use Dictionary Comprehension to create a dictionary called weather_f
# that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
#
# To convert temp_c into temp_f use this formula:
# (temp_c * 9/5) + 32 = temp_f
#
# Celsius to Fahrenheit chart
# **Do NOT** Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
# .keys() → just the keys
# .values() → just the values
# .items() → key-value pairs (what you need for unpacking)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# new_dict = {new_key: new_value for item in list}
weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
print(weather_f)

# How to Iterate rows over a Pandas DataFrame

names = ['Tilly', 'Lottie', 'Pepper', 'Tygra', 'Delilah']
student_dict ={student:random.randint(45,100) for student in names }
print(student_dict)
student_data_frame = pd.DataFrame(student_dict.items(), columns = ['student', 'score'])
print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
        # print(index)
        # print(row) # get row at the index (this is a series)
        # print(row.student)
        # print(row.score)
        if row.student == "Tygra":
            print(row.score)

