
letter = "/"
with open("my_file.txt", mode="a+") as file:
    file.write("\nnew text")

with open("new_file.txt", mode="a+") as file:
    file.write("\nnew text")

with open("my_file.txt") as file:
    contents = file.read()
    print(f"File contents: {contents}")

