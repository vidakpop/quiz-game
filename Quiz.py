import random
from tabulate import tabulate


class Quiz:
    def __init__(self) -> None:
        # List of quiz questions about Kenya
        self.questionss = [
            {
                "question": "What is the capital of Kenya?",
                "category": "Geography",
                "multiple_choices": {
                    "A": "Nairobi",
                    "B": "Mombasa",
                    "C": "Kisumu",
                    "D": "Nakuru",
                },
                "answer": "A",
            },
            {
                "question": "Which is the official language of Kenya?",
                "category": "Language",
                "multiple_choices": {
                    "A": "Swahili",
                    "B": "English",
                    "C": "French",
                    "D": "Arabic",
                },
                "answer": "A",
            },
            {
                "question": "Which is the highest mountain in Kenya?",
                "category": "Geography",
                "multiple_choices": {
                    "A": "Mount Kilimanjaro",
                    "B": "Mount Elgon",
                    "C": "Mount Kenya",
                    "D": "Aberdare Range",
                },
                "answer": "C",
            },
            {
                "question": "Who was Kenya's first president?",
                "category": "History",
                "multiple_choices": {
                    "A": "Daniel arap Moi",
                    "B": "Mwai Kibaki",
                    "C": "Jomo Kenyatta",
                    "D": "Uhuru Kenyatta",
                },
                "answer": "C",
            },
            {
                "question": "What is the currency of Kenya?",
                "category": "Economy",
                "multiple_choices": {
                    "A": "Dollar",
                    "B": "Shilling",
                    "C": "Euro",
                    "D": "Rand",
                },
                "answer": "B",
            },
        ]
        # Randomize answer choices for each question
        self.questions = [self._randomize_choices(question) for question in self.questionss]
        self.quiz_no = 1
        self.scores = []

    def add(self, question: dict):
        # Add a new question to the quiz
        self.questions.append(self._randomize_choices(question))

    def start(self):
        # Start the quiz and keep track of scores
        self.score = 0
        self.answers = []
        category = self.select_category()
        self.questionzs = [q for q in self.questions if q["category"] == category]
        random.shuffle(self.questionzs)
        for question in self.questionzs:
            print(question["question"])
            for choice, text in question["multiple_choices"].items():
                print(f"{choice}: {text}")
            while True:
                answer = input("Enter your choice: ").upper()
                if answer in question["multiple_choices"]:
                    break
                print("Invalid choice. Please try again.")
            if answer == question["answer"]:
                self.score += 1
            self.answers.append(answer)

    def select_category(self):
        # Select a category to focus the quiz on
        categories = list(set(q["category"] for q in self.questions))
        print("Select a category:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        while True:
            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(categories):
                return categories[int(choice) - 1]
            print("Invalid choice. Please try again.")

    def print_score(self):
        # Print the quiz score and provide options to play again
        headers = ["Question", "Your Answer", "Correct Answer"]
        data = []
        for i, question in enumerate(self.questionzs):
            user_answer = self.answers[i]
            correct_answer = question["answer"]
            data.append(
                [
                    question["question"],
                    question["multiple_choices"][user_answer] + f" ({user_answer})",
                    question["multiple_choices"][correct_answer]
                    + f" ({correct_answer})",
                ]
            )
        self.scores.append(self.score)
        self.tabulate_data(headers, data)
        print(f"Your final score is: {self.score}/{len(self.questionzs)}")
        query = input("Do you want to play again? (y/n) ").lower()
        if query.startswith("y"):
            self.quiz_no += 1
            self.play()
        else:
            print("Thanks for playing. Goodbye!")
            if self.quiz_no > 1:
                print("\nHere's a summary of your scores:")
                self.print_final_score()

    def tabulate_data(self, headers, data):
        # Format and print the results in a table format
        table = tabulate(
            data,
            headers=headers,
            tablefmt="rounded_grid",
            stralign="center",
            numalign="center",
        )
        print(table)

    @staticmethod
    def _randomize_choices(question):
        # Shuffle the answer choices to make the quiz dynamic
        choices = [
            (choice, value) for choice, value in question["multiple_choices"].items()
        ]
        random.shuffle(choices)
        new_choices = {chr(65 + i): value for i, (choice, value) in enumerate(choices)}
        new_answer = [
            key
            for key, value in new_choices.items()
            if value == question["multiple_choices"][question["answer"]]
        ][0]
        return {
            "question": question["question"],
            "category": question["category"],
            "multiple_choices": new_choices,
            "answer": new_answer,
        }

    def print_final_score(self):
        # Print the summary of the final score after multiple quizzes
        headers = ["Quiz No", "Score"]
        data = [[i + 1, score] for i, score in enumerate(self.scores)]
        data.append(["\nTotal", f"""{sum(self.scores)}\n---\n{len(self.scores)}"""])
        self.tabulate_data(headers, data)

    def play(self):
        # Play the quiz
        self.start()
        self.print_score()


# Implement the quiz with Kenyan questions
quiz = Quiz()

# Start playing the quiz
quiz.play()
