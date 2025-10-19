#   Created by Syed Rizvi
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

# Calculater app that adds, subtracts, multiplies and divides

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculate(a, b, operation):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
        return "Invalid operation"

def main():
    # First calculation
    operation = input("Pick operation from this list (+, -, *, /): \n")
    n1 = float(input("Enter first number: \n"))
    n2 = float(input("Enter second number: \n"))
    
    output = calculate(n1, n2, operation)
    print(f"{n1} {operation} {n2} = {output}")
    
    # Second calculation (chaining)
    if isinstance(output, str):
        print(f"Cannot chain operations due to: {output}")
    else:
        new_operation = input("Pick another operation (+, -, *, /) or 'q' to quit: \n")
        if new_operation.lower() != 'q':
            n3 = float(input("Enter next number: \n"))
            final_output = calculate(output, n3, new_operation)
            print(f"{output} {new_operation} {n3} = {final_output}")

if __name__ == "__main__":
    main()







