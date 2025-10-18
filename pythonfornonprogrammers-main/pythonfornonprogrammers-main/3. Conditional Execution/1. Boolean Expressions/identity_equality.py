print("\n=== IDENTITY vs EQUALITY DEEP DIVE ===")

# Same value, different objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 = [1, 2, 3]")
print("list2 = [1, 2, 3]")
print("list3 = list1")

print(f"list1 == list2: {list1 == list2}")      # True (same content)
print(f"list1 is list2: {list1 is list2}")      # False (different objects)
print(f"list1 == list3: {list1 == list3}")      # True (same content)
print(f"list1 is list3: {list1 is list3}")      # True (same object)

# Modifying one affects the other if they're the same object
list1.append(4)
print(f"After list1.append(4):")
print(f"list1: {list1}")  # [1, 2, 3, 4]
print(f"list2: {list2}")  # [1, 2, 3]
print(f"list3: {list3}")  # [1, 2, 3, 4]