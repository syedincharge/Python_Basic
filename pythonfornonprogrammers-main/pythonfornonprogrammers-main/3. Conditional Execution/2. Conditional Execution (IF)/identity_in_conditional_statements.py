print("\n=== IDENTITY IN CONDITIONAL STATEMENTS ===")

# Common patterns
def handle_data(data):
    if data is None:
        return "No data provided"
    elif data is True:
        return "Data is explicitly True"
    elif data is False:
        return "Data is explicitly False"
    else:
        return f"Data: {data}"

print(f"handle_data(None): {handle_data(None)}")
print(f"handle_data(True): {handle_data(True)}")
print(f"handle_data(False): {handle_data(False)}")
print(f"handle_data('test'): {handle_data('Syed')}")



# Singleton pattern check
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print(f"singleton1 is singleton2: {singleton1 is singleton2}")  # True