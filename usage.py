from memoizek import MemoizeK

def add(a, b):
    return a(b)

def func(a):
    return a * 2

m = MemoizeK(add, 3)

m(1,2)    # miss! returns fresh calculation, cache after: [3]
m(1,2)    # hit! returns cached calculation, cache after: [3]
m(10,2)   # miss! returns fresh calculation, cache after: [12,3]
m(1,42)   # miss! returns fresh calculation, cache after: [43,12,3]
m(10,2)   # hit! returns cached calculation, cache after: [12,43,3]
m(1,2)    # hit! returns cached calculation, cache after: [3,12,43]
m(43,43)  # miss! returns fresh calculation, cache after: [86,3,12]
