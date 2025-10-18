#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

#  Operators
print(5 / 2)
print(5 // 2)
print(5 ** 2)
print(2*2+2/2-2)  #  4 + 1 - 2  = 3

print(120%100)  # extract 20 last two digit

# print("Hello" + 100)

print(4*"Hello  ")
string = "name";
print(2*string)

  # Basic PEMDAS Rules 
  # PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print("=== BASIC PEMDAS EXAMPLES ===")

# Example 1: Basic order
result1 = 2 + 3 * 4
print(f"1. 2 + 3 * 4 = {result1}")  # 2 + 12 = 14

# Example 2: With parentheses
result2 = (2 + 3) * 4
print(f"2. (2 + 3) * 4 = {result2}")  # 5 * 4 = 20

# Example 3: Multiple operations
result3 = 10 - 3 * 2 + 8 / 4
print(f"3. 10 - 3 * 2 + 8 / 4 = {result3}")  # 10 - 6 + 2 = 6

# Example 4: With exponents
result4 = 2 ** 3 + 4 * 2
print(f"4. 2 ** 3 + 4 * 2 = {result4}")  # 8 + 8 = 16


print("\n=== PARENTHESES EXAMPLES ===")

# Example 5: Nested parentheses
result5 = ((2 + 3) * (4 - 1)) ** 2
print(f"5. ((2 + 3) * (4 - 1)) ** 2 = {result5}")  # (5 * 3)² = 15² = 225

# Example 6: Complex parentheses
result6 = (10 + (2 * 3) - 4) / 2
print(f"6. (10 + (2 * 3) - 4) / 2 = {result6}")  # (10 + 6 - 4) / 2 = 12 / 2 = 6

# Example 7: Multiple grouping
result7 = (8 - 2) * (3 + 4) / (5 - 1)
print(f"7. (8 - 2) * (3 + 4) / (5 - 1) = {result7}")  # 6 * 7 / 4 = 42 / 4 = 10.5



print("\n=== EXPONENTS EXAMPLES ===")

# Example 8: Basic exponents
result8 = 2 ** 3 ** 2
print(f"8. 2 ** 3 ** 2 = {result8}")  # 2⁹ = 512 (right-associative)

# Example 9: Exponents with parentheses
result9 = (2 ** 3) ** 2
print(f"9. (2 ** 3) ** 2 = {result9}")  # 8² = 64

# Example 10: Mixed with multiplication
result10 = 3 * 2 ** 3
print(f"10. 3 * 2 ** 3 = {result10}")  # 3 * 8 = 24

# Example 11: Exponents and division
result11 = 16 / 2 ** 2
print(f"11. 16 / 2 ** 2 = {result11}")  # 16 / 4 = 4


print("\n=== ADDITION & SUBTRACTION (Left to Right) ===")

# Example 15: Addition and subtraction same priority
result15 = 10 - 3 + 5
print(f"15. 10 - 3 + 5 = {result15}")  # 7 + 5 = 12

# Example 16: Multiple operations
result16 = 20 + 5 - 8 + 3
print(f"16. 20 + 5 - 8 + 3 = {result16}")  # 25 - 8 + 3 = 17 + 3 = 20

# Example 17: Mixed with higher precedence
result17 = 5 + 3 * 2 - 4
print(f"17. 5 + 3 * 2 - 4 = {result17}")  # 5 + 6 - 4 = 7


print("\n=== COMPLEX MIXED EXAMPLES ===")

# Example 18: All operations
result18 = (3 + 2) * 4 ** 2 / 8 - 1
print(f"18. (3 + 2) * 4 ** 2 / 8 - 1 = {result18}")  # 5 * 16 / 8 - 1 = 80 / 8 - 1 = 10 - 1 = 9

# Example 19: Multiple levels
result19 = 2 + 3 * 4 - 8 / 2 ** 2
print(f"19. 2 + 3 * 4 - 8 / 2 ** 2 = {result19}")  # 2 + 12 - 8 / 4 = 2 + 12 - 2 = 12

# Example 20: Real-world calculation
principal = 1000
rate = 0.05
time = 3
compound_interest = principal * (1 + rate) ** time
print(f"20. Compound Interest: 1000 * (1 + 0.05) ** 3 = {compound_interest}")


print("\n=== STEP-BY-STEP ANALYSIS ===")

# Let's break down a complex expression step by step
expression = "8 + 2 * (10 - 3 ** 2) / 4"

print(f"Expression: {expression}")

# Step 1: Parentheses and Exponents
step1 = 3 ** 2  # 9
step2 = 10 - step1  # 1
print(f"Step 1 - Parentheses & Exponents: 10 - 3² = 10 - 9 = 1")

# Step 2: Multiplication and Division
step3 = 2 * step2  # 2
step4 = step3 / 4  # 0.5
print(f"Step 2 - Multiplication & Division: 2 * 1 / 4 = 2 / 4 = 0.5")

# Step 3: Addition and Subtraction
step5 = 8 + step4  # 8.5
print(f"Step 3 - Addition & Subtraction: 8 + 0.5 = 8.5")

final_result = 8 + 2 * (10 - 3 ** 2) / 4
print(f"Final Result: {final_result}")
print(f"Step-by-step matches direct calculation: {step5 == final_result}")


print("\n=== COMMON MISTAKES ===")

# Mistake 1: Forgetting PEMDAS
wrong1 = 1 + 2 * 3  # Some might think 3 * 3 = 9
right1 = 1 + (2 * 3)  # Correct: 1 + 6 = 7
print(f"Mistake 1: 1 + 2 * 3 = {wrong1} (not 9)")

# Mistake 2: Exponents right-associativity
wrong2 = 2 ** 3 ** 2  # Some might think (2³)² = 64
right2 = 2 ** (3 ** 2)  # Correct: 2⁹ = 512
print(f"Mistake 2: 2 ** 3 ** 2 = {wrong2} (not 64)")

# Mistake 3: Division and multiplication order
wrong3 = 8 / 2 * 4  # Some might think 8 / 8 = 1
right3 = (8 / 2) * 4  # Correct: 4 * 4 = 16
print(f"Mistake 3: 8 / 2 * 4 = {wrong3} (not 1)")



    
    
    
    
    
    