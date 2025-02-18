try:
    a = int(input("enter number "))
    print(a)
    raise ZeroDivisionError("zero division error")
except Exception as e:
    print(e)
finally:
    print("finally block")