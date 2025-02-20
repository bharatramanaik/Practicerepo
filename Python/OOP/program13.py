
def debug_func(func):
    def wrapper(*args, **kwargs):
        arg_values = ', '.join(str(arg) for arg in args)
        kwargs_values = ', '.join(f"{k}: {v}" for k, v in kwargs.items())
        print(f"{func.__name__} {arg_values} {kwargs_values}")
        return func(*args, **kwargs)

    return wrapper


@debug_func
def greet(name, greet="hi"):
    print(f"{greet} {name}")

greet("bharat", "hello")