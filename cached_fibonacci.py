#!/usr/bin/env python3
fname="cached_fibonacci.png"
cache = {0: 1, 1: 1}
from visualiser.visualiser import Visualiser as vs

@vs(node_properties_kwargs={
    "shape": "record",
    "color": "#f57542",
    "style": "filled",
    "fillcolor": "grey"
})
def fib(n):
    if n not in cache:
        cache[n] = \
            fib(n=n-1) + fib(n=n-2)
    return cache[n]
def main():
    import io
    import sys
    trap = io.StringIO()
    sys.stdout = trap
    fib(n=5)
    vs.make_animation(fname.split(".")[0] + ".gif", delay=1)
    sys.stdout = sys.__stdout__
    print(fname, end='')


if __name__ == "__main__":
    main()
