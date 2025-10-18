print("\n=== PRACTICE EXERCISES ===")

# Try to predict the results before running!
exercises = [
    "4 + 6 * 2",
    "(4 + 6) * 2", 
    "12 / 4 * 3",
    "2 ** 3 * 2",
    "10 - 3 + 2",
    "8 + 4 / 2 ** 2",
    "(8 + 4) / 2 ** 2",
    "3 * 2 ** 3 + 1"
]

print("Try to solve these exercises mentally first, then check the answers:\n")

for i, expr in enumerate(exercises, 1):
    result = eval(expr)
    print(f"Exercise {i}: {expr} = {result}")

print("\n=== EXPLANATIONS ===")
explanations = [
    "4 + 6 * 2 = 4 + 12 = 16 (Multiplication before addition)",
    "(4 + 6) * 2 = 10 * 2 = 20 (Parentheses first)",
    "12 / 4 * 3 = 3 * 3 = 9 (Left to right: division then multiplication)",
    "2 ** 3 * 2 = 8 * 2 = 16 (Exponent before multiplication)",
    "10 - 3 + 2 = 7 + 2 = 9 (Left to right: subtraction then addition)",
    "8 + 4 / 2 ** 2 = 8 + 4 / 4 = 8 + 1 = 9 (Exponent → Division → Addition)",
    "(8 + 4) / 2 ** 2 = 12 / 4 = 3 (Parentheses → Exponent → Division)",
    "3 * 2 ** 3 + 1 = 3 * 8 + 1 = 24 + 1 = 25 (Exponent → Multiplication → Addition)"
]

for explanation in explanations:
    print(explanation)
    
    
    