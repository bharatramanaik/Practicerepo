# closure
def calc(x):
    def myfunc(y):
        return y + x
    return myfunc

a = calc(2)
b = calc(3)
print(a(4))
print(b(5))