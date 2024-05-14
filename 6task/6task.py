import csv

class TestModule:
    def __init__(self, questions_csv, users_csv):
        self.questions_csv = questions_csv
        self.users_csv = users_csv
        self.questions = []
        self.load_questions()

    def load_questions(self):
        with open(self.questions_csv, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.questions.append(row)

    def take_exam(self):
        score = 0
        total_questions = len(self.questions)
        for question in self.questions:
            print(question['Question'])
            options = question['Options'].split(',')
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            answer = input("Your answer (enter the option number): ")
            if answer.isdigit() and 1 <= int(answer) <= len(options):
                if options[int(answer) - 1] == question['Answer']:
                    score += 1
        return score, total_questions

    def show_result(self, score, total_questions):
        print("\nTest Result:")
        print(f"Total Questions: {total_questions}")
        print(f"Score: {score}/{total_questions}")
        percentage = (score / total_questions) * 100
        print(f"Percentage: {percentage}%")

    def run_test(self):
        print("Welcome to the Test Module!")
        name = input("Enter your name: ")
        print(f"Hello, My Quiz Player {name}!\n")
        score, total_questions = self.take_exam()
        self.show_result(score, total_questions)


if __name__ == "__main__":
    questions_csv = "questions.csv"
    users_csv = "users.csv"
    test_module = TestModule(questions_csv, users_csv)
    test_module.run_test()
