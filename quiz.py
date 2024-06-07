def Quiz():
    questions = [
        {"question": "What is the correct syntax to print 'Welcome to Quiz' in Python?", "options": ["A) print('Welcome to Quiz')", "B) show('Welcome to Quiz')","C) display('Welcome to Quiz')", "D) none"], "correct": "A"},
        {"question": "What is the purpose of the range() function in Python?", "options": ["A) Generate a sequence of numbers", "B) Find the length of a list","C) Multiply two numbers", "D) Reverse a string"], "correct": "A"},
        {"question": "The value of the Python expression given below would be:4+2**5//10", "options": ["A)  77", "B) 0", "C) 3", "D) 7"], "correct": "D"},
        {"question": "Which function removes a set’s first and the last element from a list?", "options":["A)remove","B)pop","C)discard","D)dispose"], "correct": "B"},
        {"question": "In Python, find which one isn’t an exception handling keyword.", "options": ["A)finally","B)try","C)accept","D)except"], "correct": "C"},
    ]

    score = 0

    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer: ").upper()
        while answer not in ["A", "B", "C", "D"]:
            print("Invalid input. Please enter A, B, C, or D.")
            answer = input("Enter your answer: ").upper()
        if answer == question["correct"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question['correct']}.")

    print(f"Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    Quiz()