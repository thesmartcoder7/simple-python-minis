from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
question_pair = {}

for item in range(0, len(question_data)):
    question_pair = question_data[item]
    question = Question(question=question_pair["text"], answer=question_pair["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() and quiz.success:
    quiz.post_question()

print("Thank you for playing")
