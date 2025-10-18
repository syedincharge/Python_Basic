  # Round Function
print(10/3)        # 3.3333333333333335 (exact floating point representation)
print(int(10/3))   # 3 (truncates decimal part)
print(round(10/3)) # 3 (rounds to nearest integer)
print(round(10/3, 2)) # 3.33 (rounds to 2 decimal places)  
  
  
print("=== BASIC round() FUNCTION EXAMPLES ===")


# Basic rounding to nearest integer
print(f"round(3.14159) = {round(3.14159)}")  # 3
print(f"round(3.5) = {round(3.5)}")  # 4
print(f"round(3.4) = {round(3.4)}")  # 3
print(f"round(2.675) = {round(2.675)}")  # 3

# Your original examples
print(f"10/3 = {10/3}")  # 3.3333333333333335
print(f"int(10/3) = {int(10/3)}")  # 3 (truncates decimal)
print(f"round(10/3) = {round(10/3)}")  # 3



print("\n=== ROUNDING WITH PRECISION ===")

# Round to specific decimal places
pi = 3.14159265359

print(f"round(pi, 0) = {round(pi, 0)}")  # 3.0
print(f"round(pi, 1) = {round(pi, 1)}")  # 3.1
print(f"round(pi, 2) = {round(pi, 2)}")  # 3.14
print(f"round(pi, 3) = {round(pi, 3)}")  # 3.142
print(f"round(pi, 4) = {round(pi, 4)}")  # 3.1416

# Financial examples
price = 19.9876
print(f"round(19.9876, 2) = {round(price, 2)}")  # 19.99

temperature = 98.654
print(f"round(98.654, 1) = {round(temperature, 1)}")  # 98.7



print("\n=== ROUNDING DIFFERENT DATA TYPES ===")

# Integers (no change)
print(f"round(5) = {round(5)}")  # 5
print(f"round(5, 2) = {round(5, 2)}")  # 5.0

# Negative numbers
print(f"round(-3.7) = {round(-3.7)}")  # -4
print(f"round(-3.2) = {round(-3.2)}")  # -3
print(f"round(-2.5) = {round(-2.5)}")  # -2

# Zero
print(f"round(0.499) = {round(0.499)}")  # 0
print(f"round(0.5) = {round(0.5)}")  # 0 (bankers rounding)



print("\n=== BANKERS ROUNDING EXAMPLES ===")

# Python uses "round half to even" - rounds to nearest even number
print("Python uses bankers rounding (round half to even):")

print(f"round(2.5) = {round(2.5)}")  # 2 (nearest even)
print(f"round(3.5) = {round(3.5)}")  # 4 (nearest even)
print(f"round(4.5) = {round(4.5)}")  # 4 (nearest even)
print(f"round(5.5) = {round(5.5)}")  # 6 (nearest even)

print(f"round(1.5) = {round(1.5)}")  # 2
print(f"round(2.5) = {round(2.5)}")  # 2
print(f"round(3.5) = {round(3.5)}")  # 4
print(f"round(4.5) = {round(4.5)}")  # 4

# With decimals
print(f"round(1.55, 1) = {round(1.55, 1)}")  # 1.6
print(f"round(1.65, 1) = {round(1.65, 1)}")  # 1.6
print(f"round(1.75, 1) = {round(1.75, 1)}")  # 1.8
  
  
  
print("\n=== ALTERNATIVE ROUNDING METHODS ===")

import math

# math.floor() - always round down
print(f"math.floor(3.7) = {math.floor(3.7)}")  # 3
print(f"math.floor(3.2) = {math.floor(3.2)}")  # 3
print(f"math.floor(-3.7) = {math.floor(-3.7)}")  # -4

# math.ceil() - always round up
print(f"math.ceil(3.2) = {math.ceil(3.2)}")  # 4
print(f"math.ceil(3.7) = {math.ceil(3.7)}")  # 4
print(f"math.ceil(-3.2) = {math.ceil(-3.2)}")  # -3

# math.trunc() - truncate (remove decimal)
print(f"math.trunc(3.7) = {math.trunc(3.7)}")  # 3
print(f"math.trunc(3.2) = {math.trunc(3.2)}")  # 3
print(f"math.trunc(-3.7) = {math.trunc(-3.7)}")  # -3

# int() also truncates
print(f"int(3.7) = {int(3.7)}")  # 3
print(f"int(3.2) = {int(3.2)}")  # 3  


