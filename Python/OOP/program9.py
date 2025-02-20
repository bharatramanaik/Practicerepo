# **kwargs - named variable number of arguments
def print_all(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(print_all(name="bh", role="dev", age=23))
print(print_all(name="bh", role="dev"))
print(print_all(name="bh", role="dev", age=23, lang="python"))
