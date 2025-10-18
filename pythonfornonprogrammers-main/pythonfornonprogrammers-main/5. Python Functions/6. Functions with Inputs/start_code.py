#   Created by Syed Rizvi
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

# Functions with Inputs
def greet(name):
    """Greet the person with the given name."""
    print(f"Hello, {name}! Welcome to Python functions.")
greet("Alice")
greet("Bob")
def add(a, b):
    """Return the sum of two numbers a and b."""
    return a + b
result1 = add(5, 3)
result2 = add(-2, 10)
print(f"Sum 1: {result1}")
print(f"Sum 2: {result2}")
def multiply(x, y):
    """Return the product of two numbers x and y."""
    return x * y
prod1 = multiply(4, 6)
prod2 = multiply(-3, 7)
print(f"Product 1: {prod1}")
print(f"Product 2: {prod2}")
def power(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent
pow1 = power(2, 3)
pow2 = power(5, 4)
print(f"2^3 = {pow1}")
print(f"5^4 = {pow2}")
def divide(numerator, denominator):
    """Return the division of numerator by denominator. Handle division by zero."""
    if denominator == 0:
        return "Error: Division by zero is undefined."
    return numerator / denominator
div1 = divide(10, 2)
div2 = divide(5, 0)
print(f"10 / 2 = {div1}")
print(f"5 / 0 = {div2}")
# Call the functions with different inputs to demonstrate their functionality
greet("Charlie")    
sum3 = add(20, 30)
print(f"Sum 3: {sum3}")
prod3 = multiply(8, 9)
print(f"Product 3: {prod3}")
pow3 = power(3, 5)
print(f"3^5 = {pow3}")
div3 = divide(15, 3)
print(f"15 / 3 = {div3}")
div4 = divide(7, 0)
print(f"7 / 0 = {div4}")

#   Created by Syed Rizvi
