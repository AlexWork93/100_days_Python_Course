class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.user_answer = None

    def set_user_answer(self, user_answer: bool):
        self.user_answer = user_answer

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

    def check_answer(self, user_answer):
        correct_answer = True if self.current_question.answer == "True" else False
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
