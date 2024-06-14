class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        size_list = len(self.questions_list)
        return self.question_number < size_list

    def check_answer(self, user_input):
        if self.questions_list[self.question_number].answer.lower() == user_input.lower():
            self.score += 1
            print("Correct")
        else:
            print(f"Wrong. The correct answer was {self.questions_list[self.question_number].answer.lower()}")
        print(f"{self.score}/{(self.question_number+1)}")
        print()

    def next_question(self):
        user_input = input(f"Q.{self.question_number+1}: {self.questions_list[self.question_number].text} (True/False): ")
        self.check_answer(user_input)
        self.question_number += 1

