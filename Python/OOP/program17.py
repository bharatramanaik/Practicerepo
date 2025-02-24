class A:
    def __init__(self):
        self.val = "A"
        # print("A")

class B(A):
    def __init__(self):
        super().__init__()
        self.val = "B"
        # print("B")

class C(A):
    def __init__(self):
        super().__init__()
        self.val = "C"
        # print("C")

class D(B, C):
    def __init__(self):
        super().__init__()

obj = D()
print(obj.val)
print(D.mro())