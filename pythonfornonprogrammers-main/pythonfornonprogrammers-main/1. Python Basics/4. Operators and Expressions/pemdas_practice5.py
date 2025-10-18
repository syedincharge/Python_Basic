print("\n=== PEMDAS QUIZ ===")

quiz_items = [
    ("4 + 6 * 2", 16, "Multiplication before addition"),
    ("(4 + 6) * 2", 20, "Parentheses first"),
    ("12 / 4 * 3", 9, "Left to right for multiplication/division"),
    ("2 ** 3 * 2", 16, "Exponents before multiplication"),
    ("10 - 3 + 2", 9, "Left to right for addition/subtraction"),
    ("8 + 4 / 2 ** 2", 9, "P → E → M/D → A/S"),
    ("(8 + 4) / 2 ** 2", 3, "Parentheses → Exponents → Division"),
    ("3 * 2 ** 3 + 1", 25, "Exponents → Multiplication → Addition")
]

score = 0
total = len(quiz_items)

print(f"Test your PEMDAS knowledge! {total} questions.\n")

for i, (expr, correct_answer, explanation) in enumerate(quiz_items, 1):
    print(f"Question {i}: What is {expr} ?")
    
    try:
        user_answer = float(input("Your answer: "))
    except ValueError:
        print("Please enter a valid number!\n")
        continue
    
    if abs(user_answer - correct_answer) < 0.001:  # Account for floating point
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect. The answer is {correct_answer}")
    
    print(f"Explanation: {explanation}\n")

print(f"Quiz complete! Your score: {score}/{total} ({score/total*100:.1f}%)")