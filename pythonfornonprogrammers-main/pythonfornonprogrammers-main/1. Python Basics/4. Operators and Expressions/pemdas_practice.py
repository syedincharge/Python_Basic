

print("\n=== PRACTICE EXERCISES ===")

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

print("PEMDAS Practice - Answers:\n")

for i, expr in enumerate(exercises, 1):
    result = eval(expr)
    print(f"{i}. {expr} = {result}")
    
    
    