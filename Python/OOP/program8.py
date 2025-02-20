# *args - variable number of arguments
def cal_sum(*args):
    return sum(args)

print(cal_sum(1,2,3,4))
print(cal_sum(1,2,3,4,5,6))
print(cal_sum(1,2,3))
