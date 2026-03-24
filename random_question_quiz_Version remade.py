import random

# Predefined questions with answers
questions = [
    {"question": "What is the capital of India?", "answer": "New Delhi"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "Who invented Python?", "answer": "Guido van Rossum"},
    {"question": "What is the square root of 64?", "answer": "8"}
]

score = 0
num_questions = len(questions)

print("Welcome to the Quiz!")
print(f"Total Questions: {num_questions}\n")

# Shuffle questions
random.shuffle(questions)

for i, q in enumerate(questions, 1):
    print(f"Question {i}: {q['question']}")
    user_answer = input("Enter your answer: ").strip()
    
    if user_answer.lower() == q['answer'].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {q['answer']}")
    print()

print("="*40)
print(f"Quiz Complete!")
print(f"Your Score: {score}/{num_questions}")
print(f"Percentage: {(score/num_questions)*100:.1f}%")
print("="*40)
