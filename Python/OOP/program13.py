
def debug_func(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} {args}")
        func_args
        return func(*args, **kwargs)

    return wrapper


@debug_func
def greet(name, greet="hi"):
    print(f"{greet} {name}")

greet("bharat", "hello")