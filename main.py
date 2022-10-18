from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


if __name__ == '__main__':
    question_bank = []
    for item in question_data:
        new_q = Question(item['question'], item['correct_answer'])
        question_bank.append(new_q)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print(f"You've completer the quiz.\nYour final score was {quiz.score}/{quiz.question_number}")
