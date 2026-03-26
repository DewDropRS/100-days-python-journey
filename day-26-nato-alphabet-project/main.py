import pandas as pd

#pattern to follow for reference only
#new_dict = {new_key:new_value for (index, row) in df.iterrows()}

df = pd.read_csv("nato_phonetic_alphabet.csv")
# print(df)
nato_phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# print(nato_phonetic_dict)

def generate_nato_phonetic():
    """Takes a word and returns a NATO phonetic list.

    :returns: NATO phonetic list
    """

    user_input = input("Enter a word: ")

    #unpack the user input
    user_input_list = [letter.upper() for letter in user_input]

    # First option
    # if not user_input.replace(" ", "").isalpha():
    #     raise ValueError("Name must contain letters and spaces only.")
    #
    # nato_phonetic_result = [nato_phonetic_dict[letter] for letter in user_input_list]
    # print(nato_phonetic_result)

    # Second option
    # example output:
    # Enter a word: 123
    # Invalid input: Name must contain letters only.
    # Validation check complete.

    try:
        if not user_input.replace(" ", "").isalpha():
            raise ValueError("Name must contain letters only.")

    except ValueError as e:
        print(f"Invalid input: {e}")
        generate_nato_phonetic()

    else:
        # runs only if no exception
        nato_phonetic_result = [nato_phonetic_dict[letter] for letter in user_input_list]
        print(nato_phonetic_result)

    #optional
    # finally:
    #     # always runs, error or not
    #     print("Validation check complete.")


generate_nato_phonetic()