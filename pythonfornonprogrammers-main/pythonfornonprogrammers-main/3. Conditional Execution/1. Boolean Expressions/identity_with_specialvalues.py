print("\n=== IDENTITY WITH SPECIAL VALUES ===")

# Ellipsis
ellipsis1 = ...
ellipsis2 = ...
print(f"ellipsis1 is ...: {ellipsis1 is ...}")      # True
print(f"ellipsis1 is ellipsis2: {ellipsis1 is ellipsis2}")  # True

# NotImplemented
not_implemented1 = NotImplemented
not_implemented2 = NotImplemented
print(f"not_implemented1 is NotImplemented: {not_implemented1 is NotImplemented}")  # True

# Built-in functions
print(f"len is len: {len is len}")                  # True
print(f"print is print: {print is print}")          # True