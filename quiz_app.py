class Question:
    def __init__(self, prompt, options, correct_option):
        self.prompt = prompt
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, answer):
        return answer.lower() == self.correct_option.lower()
class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)
    def start(self):
        for question in self.questions:
            print(question.prompt)
            for i, option in enumerate(question.options):
                print(f"{chr(65 + i)}. {option}")
            answer = input("Your answer: ").strip()

            if question.is_correct(answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is {question.correct_option}.\n")

        print(f"Quiz over! Your score is {self.score}/{len(self.questions)}")
def main():
    quiz = Quiz()

    quiz.add_question(Question(
        "What is the capital of France?",
        ["Berlin", "Madrid", "Paris", "Rome"],
        "C"
    ))
    quiz.add_question(Question(
        "What is 2 + 2?",
        ["3", "4", "5", "6"],
        "B"
    ))
    quiz.add_question(Question(
        "Which planet is known as the Red Planet?",
        ["Earth", "Mars", "Jupiter", "Saturn"],
        "B"
    ))
    quiz.start()
if __name__ == "__main__":
    main()
