print("\n=== PRACTICAL USE CASES  # 1 ===")

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
print(f"data1 is cached: {cache.is_cached(data1)}")  # True
print(f"data2 is cached: {cache.is_cached(data2)}")  # True (same content)
print(f"Cache contents: {cache._cache}")  # {(1, 2, 3): 'cached_data'}



print("\n=== PRACTICAL USE CASES  # 2 ===")

# Cache implementation using object identity
class Cache:
    def __init__(self):
        self._cache = {}
    
    def get(self, key, default=None):
        return self._cache.get(id(key), default)
    
    def set(self, key, value):
        self._cache[id(key)] = value
    
    def is_cached(self, key):
        return id(key) in self._cache

cache = Cache()
data1 = [1, 2, 3]
data2 = [1, 2, 3]  # Different object, same content

cache.set(data1, "cached_data")
print(f"data1 is cached: {cache.is_cached(data1)}")  # True
print(f"data2 is cached: {cache.is_cached(data2)}")  # False (different object)
print(f"data1 id: {id(data1)}")
print(f"data2 id: {id(data2)}")



print("\n=== PRACTICAL USE CASES  # 3 ===")

# Cache implementation using object identity
class Cache:
    def __init__(self):
        self._cache = {}
    
    def get(self, key, default=None):
        return self._cache.get(id(key), default)
    
    def set(self, key, value):
        self._cache[id(key)] = value
    
    def is_cached(self, key):
        return id(key) in self._cache

cache = Cache()
data1 = [1, 2, 3]
data2 = [1, 2, 3]

cache.set(data1, "cached_data")
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