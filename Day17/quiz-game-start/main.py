from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for ques in question_data:
    question_text = ques["question"]
    question_answer = ques["correct_answer"]
    new_ques = Question(question=question_text, answer=question_answer)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've Completed the quiz.")
print(f"Your Final score is: {quiz.score}/{quiz.question_number}")
