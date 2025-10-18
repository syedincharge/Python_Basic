print("\n=== PEMDAS PRACTICE WITH STEP-BY-STEP SOLUTIONS ===")

exercises = [
    ("4 + 6 * 2", "Multiplication before addition: 6*2=12, then 4+12=16"),
    ("(4 + 6) * 2", "Parentheses first: (4+6)=10, then 10*2=20"),
    ("12 / 4 * 3", "Left to right: 12/4=3, then 3*3=9"),
    ("2 ** 3 * 2", "Exponent first: 2³=8, then 8*2=16"),
    ("10 - 3 + 2", "Left to right: 10-3=7, then 7+2=9"),
    ("8 + 4 / 2 ** 2", "Exponent: 2²=4, Division: 4/4=1, Addition: 8+1=9"),
    ("(8 + 4) / 2 ** 2", "Parentheses: (8+4)=12, Exponent: 2²=4, Division: 12/4=3"),
    ("3 * 2 ** 3 + 1", "Exponent: 2³=8, Multiplication: 3*8=24, Addition: 24+1=25")
]

for i, (expr, explanation) in enumerate(exercises, 1):
    result = eval(expr)
    print(f"\nExercise {i}: {expr}")
    print(f"Answer: {result}")
    print(f"Explanation: {explanation}")