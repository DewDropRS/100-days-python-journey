#go up one level
PLACEHOLDER = "[name]"
letter = "./Input/Letters/starting_letter.docx"
with open(letter) as template:
    contents = template.read()
    print(f"Letter contents: {contents}")

output_folder = "./Output/ReadyToSend"
invite_list = "./Input/Names/invited_names.txt"

with open(invite_list) as names:
    with open(letter) as template:
        contents = template.read()
    for line in names:
        name = line.strip()
        with open(f"{output_folder}/letter_for_{name}.txt", mode="a") as invite:
            body = contents.replace(PLACEHOLDER, name)
            invite.write(body)
