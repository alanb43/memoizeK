from memoizek import MemoizeK

def compute(func, *args):
    return func(*args)

def add(a,b):
    return a + b

memo_compute = MemoizeK(compute, 2)
memo_compute(add, 1, 2) # miss, returns 3
memo_compute(add, 1, 2) # hit, returns cached value (3)
memo_compute(add, 2, 1) # miss, arguments don't match!