print("\n=== IDENTITY IN FUNCTION ARGUMENTS ===")

def modify_list(lst):
    print(f"Inside function - lst is original: {lst is original_list}")
    lst.append(4)
    return lst

original_list = [1, 2, 3]
new_list = modify_list(original_list)

print(f"original_list: {original_list}")  # [1, 2, 3, 4]
print(f"new_list: {new_list}")            # [1, 2, 3, 4]
print(f"original_list is new_list: {original_list is new_list}")  # True

# With copy
copied_list = original_list.copy()
print(f"original_list is copied_list: {original_list is copied_list}")  # False



