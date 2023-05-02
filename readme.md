## MemoizeK

A (very) simple adjustable cache in Python. A cache 'hit' is registered when the arguments to your function match exactly, so for example:

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

I ([@alanb43](https://github.com/alanb43)) wanted to make this for use in a project, but also as an excuse to learn about packages in python + getting a package on https://pypi.org/. The repo will reflect the release when it's up!