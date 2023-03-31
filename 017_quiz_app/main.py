from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random
import os


question_base = []
for i in question_data:
    question_base.append(Question(i["text"], i["answer"]))

random.shuffle(question_base)

quiz_brain = QuizBrain(question_base)

while quiz_brain.has_next_question():
    os.system("clear")
    user_answer = quiz_brain.next_question()
    quiz_brain.check_answer(user_answer)
    input("Press enter")
# print(quiz_brain.question_list)
# for i in quiz_brain.question_list:
#     i.print_question_with_answer()
