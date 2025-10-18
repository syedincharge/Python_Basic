import time

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

print("Solve these exercises. Answers will appear in 3 seconds...\n")

for i, expr in enumerate(exercises, 1):
    result = eval(expr)
    print(f"Exercise {i}: {expr} = ?")
    time.sleep(3)  # Wait 3 seconds
    print(f"Answer: {result}\n")
    time.sleep(1)  # Brief pause between exercises