from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import json #java script object notation

# from data.py (not in use)
def generate_question_bank():
    question_bank = []

    for question in question_data:
        question_bank.append(Question(question["text"], question["answer"]))
    return question_bank

# enhancement would be to use the Open Trivia Database that is free to use
# https://opentdb.com/
# click on the gear button called API and generate your string of questions
# copy/paste the full string from the resulting URL into a new json file and save in this same directory
# update the parameter argument when calling the function below

def generate_question_bank_from_json(json_data_file):
    # open and read the file
    with open(json_data_file, 'r') as j_file:
        data = json.load(j_file)
    question_bank = []
    for item in data['results']:
        question_bank.append(Question(item['question'], item['correct_answer']))
    return question_bank

def quiz_game():
    current_score = 0
    bank = generate_question_bank_from_json('film_trivia_OTD.json')
    quiz = QuizBrain(bank)
    # print(quiz.questions_list)
    while quiz.still_has_questions():
        quiz.next_question()
        if quiz.question_number == len(bank):
            print(f"You reached the end of the Quiz Game!\n"
                  f"Your final score: {quiz.score}/{quiz.question_number}")
# Test:
quiz_game()

