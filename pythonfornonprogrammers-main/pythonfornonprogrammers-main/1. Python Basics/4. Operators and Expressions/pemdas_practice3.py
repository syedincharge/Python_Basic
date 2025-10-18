print("\n=== PEMDAS PRACTICE EXERCISES ===")

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

# Show all questions first
print("Try to solve these exercises:\n")
for i, expr in enumerate(exercises, 1):
    print(f"{i}. {expr}")

input("\nPress Enter to see the answers...")

# Show all answers
print("\n=== ANSWERS ===")
for i, expr in enumerate(exercises, 1):
    result = eval(expr)
    print(f"{i}. {expr} = {result}")