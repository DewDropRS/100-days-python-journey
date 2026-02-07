class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def check_answer(self, usr_answer, correct_answer):
        if usr_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You guessed correctly!")
        else:
            print(f"You guessed incorrectly.")
        print(f"The correct answer is: {correct_answer}\n"
              # f"Your current score is: {self.score} out of {len(self.questions_list)} total questions")
                f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1 # May as well increment here. That way don't have to increment the number
            #in the input function below.
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

