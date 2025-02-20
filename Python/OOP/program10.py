# yield - it stores the function in memory with its state
def even_gen(limit):
    for i in range(2, limit+1, 2):
        yield i

for i in even_gen(10):
    print(i) 