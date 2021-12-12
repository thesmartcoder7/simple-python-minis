# import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.button_answer = ""
        self.quiz = quiz_brain
        self.updated_score = 0

        self.window = Tk()
        self.window.title("Trivia App")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white")
        self.score_label.config(bg=THEME_COLOR, anchor="e", pady=20)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightbackground=THEME_COLOR)
        self.question_text = self.canvas.create_text(150, 125, text="simple text", fill=THEME_COLOR,
                                                     font=("arial", 13, "normal"), width=250)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.next_question()

        # buttons
        self.true_button = Button(command=self.check_true)
        self.true_p = PhotoImage(file="images/true.png")
        self.true_button.config(image=self.true_p, bg=THEME_COLOR, border=0,
                                highlightthickness=0, highlightbackground=THEME_COLOR,
                                highlightcolor=THEME_COLOR)
        self.true_button.grid(row=2, column=0, pady=50)

        self.false_button = Button(command=self.check_false)
        self.false_p = PhotoImage(file="images/false.png")
        self.false_button.config(image=self.false_p, bg=THEME_COLOR, border=0,
                                 highlightthickness=0, highlightbackground=THEME_COLOR,
                                 highlightcolor=THEME_COLOR)
        self.false_button.grid(row=2, column=1, pady=50)

        self.window.mainloop()

    def next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def check_true(self):
        self.button_answer = "true"
        self.quiz.check_answer(self.button_answer)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if not self.quiz.still_has_questions():
            end_text = f"You've completed the quiz\n\n" \
                       f"Your final score is: {self.quiz.score}/{len(self.quiz.question_list)}"
            self.score_label.config(text="")
            self.canvas.itemconfig(self.question_text, text=end_text)
            return
        self.next_question()

    def check_false(self):
        self.button_answer = "false"
        self.quiz.check_answer(self.button_answer)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if not self.quiz.still_has_questions():
            end_text = f"You've completed the quiz\n\n" \
                       f"Your final score is: {self.quiz.score}/{len(self.quiz.question_list)}"
            self.score_label.config(text="")
            self.canvas.itemconfig(self.question_text, text=end_text)
            return
        self.next_question()
