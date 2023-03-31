class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def print_question_with_answer(self):
        print("====================")
        print(self.text)
        print(self.answer)
        print("====================")

