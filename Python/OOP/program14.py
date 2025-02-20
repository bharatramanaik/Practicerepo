import time

def cache_function(func):
    cache_value = {}
    def wrapper(*args, **kwargs):
        if args in cache_value:
            return "cached: ",cache_value[args]
        result = func(*args, **kwargs)
        cache_value[args] = result
        print(cache_value)
        return "not cached: ",result
    return wrapper

@cache_function
def my_func(a, b):
    time.sleep(3)
    return a + b

print(my_func(2, 3))
print(my_func(2, 4))
print(my_func(2, 6))
print(my_func(2, 7))
print(my_func(2, 7))