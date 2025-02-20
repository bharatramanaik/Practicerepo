# decorators
import time


def time_calc(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} time to execute")
        return result
    return wrapper 

@time_calc # by using this the example1 function will pass through the time_calc function
def example1(n):
    for i in range(n):
        print(i)

example1(3)
