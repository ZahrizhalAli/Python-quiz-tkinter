from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html
from ui import QuizInterface
from scoreboard import Scoreboard

scoreboard = Scoreboard()
print(scoreboard.high_score)
question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    question_level = question['difficulty']

    new_question = Question(question_text, question_answer, question_level)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
