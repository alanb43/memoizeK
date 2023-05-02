# MemoizeK

An adjustable memoization library in Python that only caches the results from the K most recent arguments.

# Rationale

I ([@alanb43](https://github.com/alanb43)) got the inspiration from [memoize-one](https://github.com/alexreardon/memoize-one) in TypeScript, but I really wanted to use this as an excuse to learn about packages in python + getting a package on https://pypi.org/.

# Usage

```python
from memoizek import MemoizeK

def compute(func, *args):
    return func(*args)

def add(a,b):
    return a + b

memo_compute = MemoizeK(compute, 2)
memo_compute(add, 1, 2) # registers a miss, returns 3
memo_compute(add, 1, 2) # registers a hit, returns cached value
memo_compute(add, 2, 1) # registers a miss, arguments don't match!
```

# Installation
Coming soon