print("\n=== INTERACTIVE PRACTICE ===")

def guess_the_length():
    test_cases = [
        ("Python", 6),
        ([1, 2, 3, 4], 4),
        ({"a": 1, "b": 2}, 2),
        ((1,), 1),
        ("", 0)
    ]
    
    score = 0
    for data, correct_length in test_cases:
        print(f"What is len({data})?")
        try:
            guess = int(input("Your guess: "))
            if guess == correct_length:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The answer is {correct_length}")
        except ValueError:
            print("Please enter a valid number!")
        print()
    
    print(f"Your score: {score}/{len(test_cases)}")

# Uncomment to play the game
guess_the_length()