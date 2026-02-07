import json
with open('film_trivia_OTD.json', 'r') as file:
    data = json.load(file)
    print(data)