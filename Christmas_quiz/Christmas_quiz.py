

# Christmas Quiz
def ask_question(prompt, answer):
    """Ask a question and return True if the answer is correct, False otherwise."""
    user_answer = input(prompt + " ")
    return user_answer.lower() == answer.lower()

def run_quiz(questions):
    """Run the quiz using a list of questions."""
    score = 0
    for question, answer in questions:
        if ask_question(question, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was '{answer}'.")
        print()

    print(f"Quiz complete! Your score is {score}/{len(questions)}.")

# List of questions and answers
quiz_questions = [
    ("What color is Rudolph's nose?", "Red"),
    ("What do you hang above the door for a kiss at Christmas?", "Mistletoe"),
    ("In 'Home Alone', where are the McCallisters going on vacation when they leave Kevin behind?", "Paris"),
    ("Which country started the tradition of putting up a Christmas tree?", "Germany"),
    # Add more questions as desired
]

# Run the quiz
run_quiz(quiz_questions)
