
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        self.success = True

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def post_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q.{self.question_number}: {question.text} True or False?: ").lower()
        self.check_answer(user_choice, question.answer)

    def check_answer(self, user_choice, question_answer):
        if user_choice == question_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"{self.score}/{len(self.question_list)}\n")
        else:
            print(f"That's wrong!! The correct answer is {question_answer.capitalize()}\n")
            print(f"Your final score is: {self.score}/{len(self.question_list)}\n")
            self.success = False

