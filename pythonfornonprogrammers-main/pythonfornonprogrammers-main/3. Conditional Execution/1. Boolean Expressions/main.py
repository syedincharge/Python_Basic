#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

     # Boolean Examples 
     
print("=== BASIC COMPARISON OPERATORS ===")

# Equality
print(f"1 == 2: {1 == 2}")        # False
print(f"1 == 1: {1 == 1}")        # True
print(f"'a' == 'a': {'a' == 'a'}") # True
print(f"'a' == 'b': {'a' == 'b'}") # False

# Inequality
print(f"1 != 2: {1 != 2}")        # True
print(f"1 != 1: {1 != 1}")        # False
print(f"'a' != 'b': {'a' != 'b'}") # True

# Less than
print(f"2 < 1: {2 < 1}")          # False
print(f"1 < 2: {1 < 2}")          # True
print(f"'a' < 'b': {'a' < 'b'}")   # True (alphabetical)

# Greater than
print(f"2 > 1: {2 > 1}")          # True
print(f"1 > 2: {1 > 2}")          # False
print(f"'b' > 'a': {'b' > 'a'}")   # True

# Less than or equal to
print(f"2 <= 1: {2 <= 1}")        # False
print(f"2 <= 2: {2 <= 2}")        # True
print(f"1 <= 2: {1 <= 2}")        # True

# Greater than or equal to
print(f"2 >= 1: {2 >= 1}")        # True
print(f"2 >= 2: {2 >= 2}")        # True
print(f"1 >= 2: {1 >= 2}")        # False

# NOTE: 2 => 1 is INVALID SYNTAX! Always use >=


print("\n=== STRING COMPARISONS ===")

# Case sensitivity
print(f"'hello' == 'hello': {'hello' == 'hello'}")     # True
print(f"'hello' == 'HELLO': {'hello' == 'HELLO'}")     # False
print(f"'hello'.lower() == 'HELLO'.lower(): {'hello'.lower() == 'HELLO'.lower()}") # True

# Alphabetical order
print(f"'apple' < 'banana': {'apple' < 'banana'}")     # True
print(f"'zebra' > 'apple': {'zebra' > 'apple'}")       # True
print(f"'cat' == 'cat': {'cat' == 'cat'}")             # True

# String length comparisons
name1 = "John"
name2 = "Jonathan"
print(f"len('{name1}') > len('{name2}'): {len(name1) > len(name2)}")  # False
print(f"len('{name1}') < len('{name2}'): {len(name1) < len(name2)}")  # True



print("\n=== LOGICAL OPERATORS ===")

# AND operator (both must be True)
print(f"True and True: {True and True}")           # True
print(f"True and False: {True and False}")         # False
print(f"False and True: {False and True}")         # False
print(f"False and False: {False and False}")       # False

# OR operator (at least one True)
print(f"True or True: {True or True}")             # True
print(f"True or False: {True or False}")           # True
print(f"False or True: {False or True}")           # True
print(f"False or False: {False or False}")         # False

# NOT operator (reverses the value)
print(f"not True: {not True}")                     # False
print(f"not False: {not False}")                   # True

# Combined logical operations
print(f"not (True and False): {not (True and False)}")     # True
print(f"(True or False) and True: {(True or False) and True}") # True


print("\n=== REAL-WORLD LOGICAL SCENARIOS ===")

# Age verification for driving
age = 18
has_license = True
print(f"Can drive: {age >= 16 and has_license}")   # True

# Login system
username = "admin"
password = "12345"
correct_username = "admin"
correct_password = "12345"
print(f"Login successful: {username == correct_username and password == correct_password}") # True

# Discount eligibility
is_student = True
is_senior = False
print(f"Gets discount: {is_student or is_senior}") # True

# Number range checking
number = 25
print(f"Between 10 and 50: {number >= 10 and number <= 50}") # True
print(f"Outside 10-50: {number < 10 or number > 50}")        # False



print("\n=== MIXED DATA TYPE COMPARISONS ===")

# Numeric comparisons
print(f"5 == 5.0: {5 == 5.0}")                     # True
print(f"5 == '5': {5 == '5'}")                     # False (different types)
print(f"5 == int('5'): {5 == int('5')}")           # True

# Boolean with numbers
print(f"True == 1: {True == 1}")                   # True
print(f"False == 0: {False == 0}")                 # True
print(f"True == 2: {True == 2}")                   # False

# None comparisons
print(f"None == None: {None == None}")             # True
print(f"None == False: {None == False}")           # False
print(f"None == 0: {None == 0}")                   # False


print("\n=== COMPLEX BOOLEAN EXPRESSIONS ===")

# Multiple conditions
x = 10
y = 20
z = 30
print(f"x < y < z: {x < y < z}")                   # True
print(f"x > y or y < z: {x > y or y < z}")         # True
print(f"not (x > y): {not (x > y)}")               # True

# Mathematical expressions in comparisons
a = 5
b = 3
print(f"a + b > a * b: {a + b > a * b}")           # 8 > 15 = False
print(f"a ** 2 == b ** 2 + 4 * b + 4: {a ** 2 == b ** 2 + 4 * b + 4}") # 25 == 25 = True

# String contains check (using in operator)
email = "user@example.com"
print(f"'@' in email: {'@' in email}")             # True
print(f"'.com' in email: {'.com' in email}")       # True
print(f"'gmail' in email: {'gmail' in email}")     # False



print("\n=== IDENTITY (is) vs EQUALITY (==) ===")

# Lists with same content but different objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 == list2: {list1 == list2}")         # True (same content)
print(f"list1 is list2: {list1 is list2}")         # False (different objects)
print(f"list1 is list3: {list1 is list3}")         # True (same object)

# None checking (always use 'is' for None)
value = None
print(f"value is None: {value is None}")           # True
print(f"value == None: {value == None}")           # True (but not preferred)

# Integers (Python caches small integers)
a = 100
b = 100
c = 1000
d = 1000
print(f"a is b: {a is b}")                         # True (cached)
print(f"c is d: {c is d}")                         # False (not cached)



print("\n=== SHORT-CIRCUIT EVALUATION ===")

def true_func():
    print("  true_func called")
    return True

def false_func():
    print("  false_func called")
    return False

print("AND short-circuit (False and ...):")
result1 = false_func() and true_func()  # false_func only

print("\nOR short-circuit (True or ...):")
result2 = true_func() or false_func()   # true_func only

print("\nNo short-circuit:")
result3 = true_func() and false_func()  # both called



print("\n=== BOOLEAN WITH COLLECTIONS ===")

# Empty collections are False, non-empty are True
empty_list = []
full_list = [1, 2, 3]
empty_string = ""
full_string = "hello"
empty_dict = {}
full_dict = {"key": "value"}

print(f"bool(empty_list): {bool(empty_list)}")     # False
print(f"bool(full_list): {bool(full_list)}")       # True
print(f"bool(empty_string): {bool(empty_string)}") # False
print(f"bool(full_string): {bool(full_string)}")   # True
print(f"bool(empty_dict): {bool(empty_dict)}")     # False
print(f"bool(full_dict): {bool(full_dict)}")       # True

# Using in operator
fruits = ["apple", "banana", "orange"]
print(f"'apple' in fruits: {'apple' in fruits}")   # True
print(f"'grape' in fruits: {'grape' in fruits}")   # False
print(f"'apple' not in fruits: {'apple' not in fruits}") # False




print("\n=== ADVANCED BOOLEAN PATTERNS ===")

# De Morgan's Laws
p = True
q = False
print(f"not (p and q) == (not p or not q): {not (p and q) == (not p or not q)}") # True
print(f"not (p or q) == (not p and not q): {not (p or q) == (not p and not q)}") # True

# XOR (exclusive OR) simulation
def xor(a, b):
    return (a and not b) or (not a and b)

print(f"xor(True, True): {xor(True, True)}")       # False
print(f"xor(True, False): {xor(True, False)}")     # True
print(f"xor(False, True): {xor(False, True)}")     # True
print(f"xor(False, False): {xor(False, False)}")   # False

# Using any() and all()
numbers = [1, 2, 3, 4, 5]
print(f"all(n > 0 for n in numbers): {all(n > 0 for n in numbers)}")   # True
print(f"any(n > 10 for n in numbers): {any(n > 10 for n in numbers)}") # False




print("\n=== COMMON MISTAKES ===")

# Mistake: Using = instead of ==
# x = 5  # Assignment
# if x = 5:  # SyntaxError!
# Correct:
x = 5
if x == 5:
    print("Correct comparison")

# Mistake: Chaining comparisons incorrectly
# if 1 < x < 10:  # Correct
# if 1 < x and x < 10:  # Also correct

# Mistake: Confusing and/or precedence
print(f"True or False and False: {True or False and False}")  # True (and has higher precedence)
print(f"(True or False) and False: {(True or False) and False}")  # False

# Mistake: Using is for value comparison
# Correct for values: ==
# Correct for object identity: is




print("=== IDENTITY OPERATORS WITH VARIABLES ===")

x = 1
y = 2
z = x

print(f"x = {x}, y = {y}, z = x")
print(f"x is y: {x is y}")              # False
print(f"x is not y: {x is not y}")      # True
print(f"x is z: {x is z}")              # True
print(f"y is z: {y is z}")              # False
print(f"1 is not 2: {1 is not 2}")      # True

# Reassignment
w = 1
print(f"x is w: {x is w}")              # True (same value, Python may cache)