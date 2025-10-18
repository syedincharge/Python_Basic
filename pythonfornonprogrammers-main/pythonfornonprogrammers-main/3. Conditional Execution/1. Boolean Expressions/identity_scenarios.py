# Different import styles
from math import sqrt
from math import sqrt as square_root


print("\n=== ADVANCED IDENTITY SCENARIOS ===")

# Function identity
def my_function():
    return "Hello"

func1 = my_function
func2 = my_function
func3 = lambda: "Hello"

print(f"func1 is my_function: {func1 is my_function}")  # True
print(f"func1 is func2: {func1 is func2}")              # True
print(f"func1 is func3: {func1 is func3}")              # False

# Method identity
class MyClass:
    def method(self):
        pass

obj1 = MyClass()
obj2 = MyClass()
print(f"obj1.method is obj1.method: {obj1.method is obj1.method}")  # True
print(f"obj1.method is obj2.method: {obj1.method is obj2.method}")  # False



print("\n=== IDENTITY WITH IMPORTED MODULES ===")

import math
import math as mathematics

print(f"math is mathematics: {math is mathematics}")  # True


print(f"sqrt is math.sqrt: {sqrt is math.sqrt}")              # True
print(f"sqrt is square_root: {sqrt is square_root}")          # True


print("\n=== IDENTITY OPERATOR PRECEDENCE ===")

a = [1, 2]
b = [1, 2]
c = a

# Combining with other operators
print(f"a is c and a == b: {a is c and a == b}")        # True
print(f"a is not b or a == b: {a is not b or a == b}")  # True
print(f"not (a is b): {not (a is b)}")                  # True

# Complex expressions
x = 10
y = 10
z = 20
print(f"x is y and y is not z: {x is y and y is not z}")  # True



