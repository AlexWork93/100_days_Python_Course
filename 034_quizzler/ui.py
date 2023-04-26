THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import *

DELAY = 500

class QuizzUi:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.screen = Tk()
        self.screen.configure(pady=30, padx=30, bg=THEME_COLOR)
        self.canvas = Canvas(width=300,
                             height=250,
                             highlightthickness=0)
        self.score_field = Label(bg=THEME_COLOR, fg='WHITE', text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
        self.score_field.grid(column=1, row=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=260,
                                                     text='here will be a question',
                                                     font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        image_confirm = PhotoImage(file='images/true.png')
        image_reject = PhotoImage(file='images/false.png')
        self.button_confirm = Button(image=image_confirm, highlightthickness=0, command=self.confirm_question)
        self.button_confirm.grid(column=0, row=2)
        self.button_reject = Button(image=image_reject, highlightthickness=0, command=self.reject_question)
        self.button_reject.grid(column=1, row=2)
        self.quiz.next_question()
        self.update_question_field(self.quiz.current_question.text)
        self.canvas.after(DELAY, self.canvas.configure(background='white'))

        self.screen.mainloop()

    def confirm_question(self):
        self.change_color_after_answer(self.quiz.check_answer(True))
        if self.quiz.still_has_questions():
            self.quiz.next_question()
            self.update_question_field(self.quiz.current_question.text)
        else:
            self.finish_game()

        self.canvas.after(DELAY, self.canvas.configure(background='white'))


    def reject_question(self):
        self.change_color_after_answer(self.quiz.check_answer(False))
        if self.quiz.still_has_questions():
            self.quiz.next_question()
            self.update_question_field(self.quiz.current_question.text)
        else:
            self.finish_game()

        self.canvas.after(DELAY, self.canvas.configure(background='white'))


    def update_question_field(self, new_question):
        self.canvas.itemconfig(self.question_text, text=new_question)

    def update_score_field(self, new_score):
        self.score_field.configure(text=new_score)

    def change_color_after_answer(self, answer_status):
        if answer_status:
            self.canvas.configure(background='green')
            self.canvas.update()
            self.score_field.configure(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
        else:
            self.canvas.configure(background='red')
            self.canvas.update()
            self.score_field.configure(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')

    def finish_game(self):
        self.button_confirm.grid_remove()
        self.button_reject.grid_remove()
        self.canvas.itemconfig(self.question_text, text=f'Score: {self.quiz.score}/{self.quiz.question_number}')



