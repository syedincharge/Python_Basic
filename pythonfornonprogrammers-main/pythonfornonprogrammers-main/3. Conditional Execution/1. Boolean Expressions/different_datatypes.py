print("\n=== IDENTITY WITH DIFFERENT DATA TYPES ===")

# Integers
a = 100
b = 100
c = 1000
d = 1000
print(f"a is b: {a is b}")              # True (small integers cached)
print(f"c is d: {c is d}")              # False (larger integers not cached)

# Strings
s1 = "hello"
s2 = "hello"
s3 = "hello world"
s4 = "hello world"
print(f"s1 is s2: {s1 is s2}")          # True (string interning)
print(f"s3 is s4: {s3 is s4}")          # False (longer strings may not be interned)

# Lists (mutable - never same object unless assigned)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 is list2: {list1 is list2}")  # False
print(f"list1 is list3: {list1 is list3}")  # True

# Tuples (immutable - may be cached)
tuple1 = (1, 2)
tuple2 = (1, 2)
tuple3 = tuple1
print(f"tuple1 is tuple2: {tuple1 is tuple2}")  # False (usually)
print(f"tuple1 is tuple3: {tuple1 is tuple3}")  # True



print("\n=== IDENTITY WITH None ===")

# Always use 'is' for None comparisons
value1 = None
value2 = None
value3 = "something"

print(f"value1 is None: {value1 is None}")          # True
print(f"value2 is None: {value2 is None}")          # True
print(f"value1 is value2: {value1 is value2}")      # True (only one None object)
print(f"value3 is None: {value3 is None}")          # False
print(f"value3 is not None: {value3 is not None}")  # True

# Common pattern for default values
def process_data(data=None):
    if data is None:
        data = []
    data.append("processed")
    return data

print(f"process_data(): {process_data()}")          # ['processed']
print(f"process_data([1,2]): {process_data([1,2])}") # [1, 2, 'processed']



print("\n=== IDENTITY WITH BOOLEAN VALUES ===")

# There's only one True and one False object in Python
bool1 = True
bool2 = True
bool3 = False
bool4 = (1 == 1)  # Evaluates to True
bool5 = (1 == 2)  # Evaluates to False

print(f"bool1 is True: {bool1 is True}")            # True
print(f"bool1 is bool2: {bool1 is bool2}")          # True
print(f"bool3 is False: {bool3 is False}")          # True
print(f"bool4 is True: {bool4 is True}")            # True
print(f"bool5 is False: {bool5 is False}")          # True
print(f"True is not False: {True is not False}")    # True