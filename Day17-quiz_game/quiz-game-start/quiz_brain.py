import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ques_text = html.unescape(current_question.text)
        user_input = input(f"Q.{self.question_number}: {ques_text}? (True/False): ").capitalize()
        self.check_answer(current_question, user_input)

    def check_answer(self, current_question, user_input):
        if current_question.answer == user_input:
            self.score += 1
            print("Hurray! You got it right.")
        else:
            print("Oops!! That's Wrong.")
        print(f"The correct answer was: {current_question.answer}")
        print(f"Your Current Score is: {self.score}/{self.question_number}")
        print("\n")
        
