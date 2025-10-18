
import math


print("\n=== CUSTOM PRECISION ROUNDING ===")

def round_to_multiple(number, multiple):
    """Round to nearest multiple"""
    return round(number / multiple) * multiple

def round_up(number, decimal_places=0):
    """Always round up"""
    multiplier = 10 ** decimal_places
    return math.ceil(number * multiplier) / multiplier

def round_down(number, decimal_places=0):
    """Always round down"""
    multiplier = 10 ** decimal_places
    return math.floor(number * multiplier) / multiplier

# Examples
print(f"round_to_multiple(17, 5) = {round_to_multiple(17, 5)}")  # 15
print(f"round_to_multiple(23, 5) = {round_to_multiple(23, 5)}")  # 25
print(f"round_to_multiple(12.7, 0.5) = {round_to_multiple(12.7, 0.5)}")  # 12.5

print(f"round_up(3.2) = {round_up(3.2)}")  # 4.0
print(f"round_up(3.14159, 2) = {round_up(3.14159, 2)}")  # 3.15

print(f"round_down(3.9) = {round_down(3.9)}")  # 3.0
print(f"round_down(3.14159, 3) = {round_down(3.14159, 3)}")  # 3.141



print("\n=== FINANCIAL & SCIENTIFIC ROUNDING ===")

# Financial calculations
principal = 1000
rate = 0.075  # 7.5%
time = 5

interest = principal * rate * time
print(f"Simple interest: {interest}")
print(f"Rounded to 2 decimals: {round(interest, 2)}")  # 375.0

# Scientific measurements
measurements = [12.3456, 7.8912, 15.2345, 9.8765]
average = sum(measurements) / len(measurements)
print(f"Average measurement: {average}")
print(f"Rounded to 3 significant figures: {round(average, 3)}")  # 11.337

# Currency formatting
def format_currency(amount):
    return f"${round(amount, 2):.2f}"

print(f"format_currency(19.999) = {format_currency(19.999)}")  # $20.00
print(f"format_currency(15.5) = {format_currency(15.5)}")  # $15.50



print("\n=== PYTHON ROUNDING FUNCTIONS ===")

# 1. Basic round() function
print("\n1. BASIC round() EXAMPLES:")
print(f"round(3.14159) = {round(3.14159)}")
print(f"round(3.5) = {round(3.5)}")
print(f"round(2.675) = {round(2.675)}")
print(f"10/3 = {10/3}")
print(f"round(10/3) = {round(10/3)}")
print(f"round(10/3, 2) = {round(10/3, 2)}")

# 2. Rounding with precision
print("\n2. ROUNDING WITH PRECISION:")
pi = 3.14159265359
print(f"round(pi, 0) = {round(pi, 0)}")
print(f"round(pi, 1) = {round(pi, 1)}")
print(f"round(pi, 2) = {round(pi, 2)}")
print(f"round(pi, 3) = {round(pi, 3)}")

# 3. Alternative rounding methods
print("\n3. ALTERNATIVE ROUNDING METHODS:")
import math
print(f"math.floor(3.7) = {math.floor(3.7)}")  # Always down
print(f"math.ceil(3.2) = {math.ceil(3.2)}")    # Always up
print(f"math.trunc(3.7) = {math.trunc(3.7)}")  # Remove decimal
print(f"int(3.7) = {int(3.7)}")               # Truncate to integer

# 4. Bankers rounding examples
print("\n4. BANKERS ROUNDING:")
print(f"round(2.5) = {round(2.5)}")  # 2 (nearest even)
print(f"round(3.5) = {round(3.5)}")  # 4 (nearest even)
print(f"round(4.5) = {round(4.5)}")  # 4 (nearest even)

# 5. Real-world examples
print("\n5. REAL-WORLD EXAMPLES:")
# Currency
price = 19.9876
print(f"Price: ${round(price, 2)}")

# GPA calculation
grades = [3.67, 2.89, 3.42, 4.00]
gpa = sum(grades) / len(grades)
print(f"GPA: {round(gpa, 2)}")

# Temperature
def celsius_to_fahrenheit(celsius):
    return round(celsius * 9/5 + 32, 1)

print(f"20°C = {celsius_to_fahrenheit(20)}°F")



