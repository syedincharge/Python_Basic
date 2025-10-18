#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

#  Strings

print("""Hello
World""")

#  Integers

print(12)
#print(parseInt("12")+(13))
print(1,000,000)
print(1_000_000)

# Floating Type
print(3.14159)

#Boolean
print(True)
print(False)

print(type("12"))
print(type(12))

def is_even(n):
    """Return True if n is an even integer, otherwise False."""
    try:
        return int(n) % 2 == 0
    except (TypeError, ValueError):
        return False

# Examples
print(is_even(2))       # True
print(is_even(3))       # False
print(is_even(0))       # True
print(is_even(-4))      # True
print(is_even("10"))    # True
print(is_even("abc"))   # False

# Boolean conversions and logical operators
print(bool(0), bool(1))                 # False True
print(bool(""), bool("hello"))          # False True
print(bool([]), bool([0]))              # False True

a, b = True, False
print(a and b, a or b, not a)           # False True False

def selection_sort(arr):
    """Return a new list with the elements of arr sorted (ascending) without using built-in sort() or sorted()."""
    a = arr[:]  # make a shallow copy to avoid mutating the original
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a

# Examples
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Original:", nums)
print("Sorted:  ", selection_sort(nums))

# Sort two arrays using built-in functions

arr1 = [7, 3, 5, 2, 9, 1]
arr2 = [10, -1, 4, 4, 0]

# Use sorted() to get a new sorted list (ascending)
sorted_arr1 = sorted(arr1)

# Use list.sort() to sort in-place (ascending)
arr2.sort()

print("arr1 (original):", arr1)
print("sorted_arr1 (new):", sorted_arr1)
print("arr2 (in-place sorted):", arr2)

# Examples of getting descending order
print("arr1 descending:", sorted(arr1, reverse=True))
print("arr2 descending:", sorted(arr2, reverse=True))

# A Function to add two strings together
def add_strings(str1, str2):
    """Return the concatenation of str1 and str2."""
    return str1 + str2
# Examples
print(add_strings("Hello, ", "world!"))  # "Hello, world!"
print(add_strings("Python", "3.10"))      # "Python3.10"
print(add_strings("", "Empty"))           # "Empty"
print(add_strings("123", "456"))         # "123456"
print(add_strings("Foo", ""))             # "Foo"
print(add_strings(" ", "Space"))         # " Space"
print(add_strings("Line1\n", "Line2"))   # "Line1\nLine2"

# A Function to multiply two integers
def multiply_integers(a, b):
    """Return the product of two integers a and b."""
    return a * b    

# Examples
print(multiply_integers(3, 4))    # 12
print(multiply_integers(-2, 5))   # -10
print(multiply_integers(0, 100))   # 0
print(multiply_integers(-3, -6))  # 18
print(multiply_integers(7, 1))    # 7
print(multiply_integers(10, -10)) # -100
print(multiply_integers(123, 0))  # 0

# A Function to check if a floating-point number is positive
def is_positive_float(num):
    """Return True if num is a positive floating-point number, otherwise False."""
    return isinstance(num, float) and num > 0   
# Examples
print(is_positive_float(3.14))    # True
print(is_positive_float(-2.71))   # False
print(is_positive_float(0.0))     # False
print(is_positive_float(1))       # False
print(is_positive_float(2.0))     # True
print(is_positive_float(-0.1))    # False
print(is_positive_float(100.5))   # True

# A Function to check if a boolean value is True
def is_true(value):
    """Return True if value is True, otherwise False."""
    return value is True
# Examples
print(is_true(True))      # True
print(is_true(False))     # False
print(is_true(1))         # False
print(is_true(0))         # False
print(is_true("True"))    # False
print(is_true(None))      # False
print(is_true([]))        # False
print(is_true({}))        # False
print(is_true(True and True))  # True
print(is_true(True or False))  # True   

# A Function to demonstrate type checking
def check_type(value):
    """Return the type of the given value."""
    return type(value)
# Examples
print(check_type("Hello"))   # <class 'str'>
print(check_type(42))        # <class 'int'>
print(check_type(3.14))      # <class 'float'>
print(check_type(True))      # <class 'bool'>
print(check_type([]))        # <class 'list'>
print(check_type({}))        # <class 'dict'>
print(check_type(None))      # <class 'NoneType'>
print(check_type((1, 2)))   # <class 'tuple'>
print(check_type(set()))     # <class 'set'>
print(check_type(lambda x: x))  # <class 'function'>    


