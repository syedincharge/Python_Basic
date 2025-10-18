#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com
print("=== STRING LENGTH EXAMPLES ===")

# Basic string
print(f'len("hello") = {len("hello")}')  # 5
print(f'len("hello world") = {len("hello world")}')  # 11 (includes space)

# Empty string
print(f'len("") = {len("")}')  # 0

# Strings with spaces and special characters
print(f'len("   ") = {len("   ")}')  # 3 (spaces count as characters)
print(f'len("hello\\nworld") = {len("hello\nworld")}')  # 11 (\\n is one character)
print(f'len("café") = {len("café")}')  # 4 (accented characters count as one)



print("\n=== LIST LENGTH EXAMPLES ===")

# Basic lists
numbers = [1, 2, 3, 4, 5]
print(f"len([1, 2, 3, 4, 5]) = {len(numbers)}")  # 5

fruits = ["apple", "banana", "cherry"]
print(f'len(["apple", "banana", "cherry"]) = {len(fruits)}')  # 3

# Nested lists
nested_list = [[1, 2], [3, 4, 5], [6]]
print(f"len([[1, 2], [3, 4, 5], [6]]) = {len(nested_list)}")  # 3 (counts outer list)

# Empty list
empty_list = []
print(f"len([]) = {len(empty_list)}")  # 0

# Mixed data types
mixed = [1, "hello", 3.14, True, None]
print(f'len([1, "hello", 3.14, True, None]) = {len(mixed)}')  # 5


print("\n=== TUPLE LENGTH EXAMPLES ===")

# Basic tuples
coordinates = (10, 20)
print(f"len((10, 20)) = {len(coordinates)}")  # 2

colors = ("red", "green", "blue")
print(f'len(("red", "green", "blue")) = {len(colors)}')  # 3

# Single element tuple (note the comma)
single = (5,)
print(f"len((5,)) = {len(single)}")  # 1

# Empty tuple
empty_tuple = ()
print(f"len(()) = {len(empty_tuple)}")  # 0


print("\n=== SET LENGTH EXAMPLES ===")

# Basic sets
unique_numbers = {1, 2, 3, 4, 5}
print(f"len({{1, 2, 3, 4, 5}}) = {len(unique_numbers)}")  # 5

# Sets remove duplicates
duplicate_numbers = {1, 2, 2, 3, 3, 3, 4}
print(f"len({{1, 2, 2, 3, 3, 3, 4}}) = {len(duplicate_numbers)}")  # 4

# Empty set
empty_set = set()
print(f"len(set()) = {len(empty_set)}")  # 0

print("\n=== REAL-WORLD EXAMPLES ===")

# Password length validation
def validate_password(password):
    if len(password) >= 8:
        return "✅ Password is secure"
    else:
        return "❌ Password must be at least 8 characters"

print(validate_password("short"))  # ❌
print(validate_password("verylongpassword"))  # ✅

# Shopping cart item count
shopping_cart = ["apples", "bananas", "milk", "bread"]
print(f"Shopping cart has {len(shopping_cart)} items")

# Username character limit
username = "super_user_123"
if len(username) <= 15:
    print(f"Username '{username}' is valid")
else:
    print("Username too long")

# Sentence word count (basic)
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
print(f"Sentence has {len(words)} words")

print("\n=== ADVANCED EXAMPLES ===")

# Multi-line string
multi_line = """Line 1
Line 2
Line 3"""
print(f"Multi-line string length = {len(multi_line)}")  # Includes newlines

# Bytes object
byte_data = b"hello"
print(f"len(b'hello') = {len(byte_data)}")  # 5

# Range object
numbers_range = range(10)
print(f"len(range(10)) = {len(numbers_range)}")  # 10

# Custom objects with __len__ method
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    
    def __len__(self):
        return len(self.songs)

my_playlist = Playlist(["Song 1", "Song 2", "Song 3"])
print(f"Custom object length = {len(my_playlist)}")  # 3


print("\n=== COMMON MISTAKES & EDGE CASES ===")

# len() with None (ERROR)
try:
    print(len(None))
except TypeError as e:
    print(f"Error with None: {e}")

# len() with numbers (ERROR)
try:
    print(len(42))
except TypeError as e:
    print(f"Error with number: {e}")

# len() with boolean (ERROR)
try:
    print(len(True))
except TypeError as e:
    print(f"Error with boolean: {e}")

# Working with strings containing emojis
emoji_string = "Hello 👋 World 🌍"
print(f'len("Hello 👋 World 🌍") = {len(emoji_string)}')  # Some emojis count as multiple characters

# Using len() in conditional statements
data = [1, 2, 3]
if len(data) > 0:
    print("List is not empty")
else:
    print("List is empty")

# More Pythonic way to check if empty
if data:
    print("List is not empty (Pythonic way)")
else:
    print("List is empty (Pythonic way)")
    
    
print("\n=== PERFORMANCE & BEST PRACTICES ===")

import time

# Large data structures
large_list = list(range(1000000))

start_time = time.time()
length = len(large_list)
end_time = time.time()

print(f"Time to get length of 1,000,000 item list: {(end_time - start_time)*1000:.6f} milliseconds")

# len() is O(1) - constant time operation
print("len() has O(1) time complexity - it's very fast!")

# Using len() in loops (good practice)
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# Better: using enumerate
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")    