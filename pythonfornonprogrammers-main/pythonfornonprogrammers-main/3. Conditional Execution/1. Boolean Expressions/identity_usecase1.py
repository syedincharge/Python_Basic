print("\n=== PRACTICAL USE CASES ===")

# Cache implementation using identity
class Cache:
    def __init__(self):
        self._cache = {}
    
    def get(self, key, default=None):
        return self._cache.get(key, default)
    
    def set(self, key, value):
        # Convert lists to tuples for hashing
        if isinstance(key, list):
            key = tuple(key)
        self._cache[key] = value
    
    def is_cached(self, key):
        # Convert lists to tuples for lookup
        if isinstance(key, list):
            key = tuple(key)
        return key in self._cache

cache = Cache()
data1 = [1, 2, 3]
data2 = [1, 2, 3]

cache.set(data1, "cached_data")
cache.set(data1, "cached_data")  # Error: lists can't be dictionary keys
print(f"data1 is cached: {cache.is_cached(data1)}")  # True
print(f"data2 is cached: {cache.is_cached(data2)}")  # False (different object)

# Default argument checking
def process_with_default(data=object()):
    if data is process_with_default.__defaults__[0]:
        print("Using default value")
    else:
        print("Using provided value")

process_with_default()  # Using default value
process_with_default("custom")  # Using provided value