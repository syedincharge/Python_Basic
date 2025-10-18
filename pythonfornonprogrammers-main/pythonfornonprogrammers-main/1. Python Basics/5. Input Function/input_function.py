import time
print("\n=== PRACTICE EXERCISES ===")

# Try to predict the results using input function before running the result !
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

for i, expr in enumerate(exercises, 1):
    result = eval(expr)
    print(f"Exercise {i}: {expr} = ?")
    input("Press Enter to see answer...")
    

    print(f"Answer: {result}\n")
    
    
name = input("Enter your name?")
print("Hello " + name + " You have learned the PEMADS Rules !")