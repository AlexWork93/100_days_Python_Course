class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (y/n): ")
        self.question_number += 1
        return answer

    def has_next_question(self):
        return self.question_number <= len(self.question_list) - 1

    def validate_answer(self, answer):
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Wrong input")
            self.validate_answer(input("Try again y/n: "))

    def check_answer(self, answer):
        answer = self.validate_answer(answer)
        if self.question_list[self.question_number - 1].answer == answer:
            self.score += 1

        print(f"Your current score: {self.score}/{self.question_number}")
