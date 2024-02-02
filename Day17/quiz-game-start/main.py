from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for ques in question_data:
    question_text = ques["text"]
    question_answer = ques["answer"]
    new_ques = Question(question=question_text, answer=question_answer)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    