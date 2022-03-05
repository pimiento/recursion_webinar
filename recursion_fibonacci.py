#!/usr/bin/env python3
fname="fibonacci.png"
from visualiser.visualiser import Visualiser as vs

@vs(node_properties_kwargs={
    "shape": "record",
    "color": "#f57542",
    "style": "filled",
    "fillcolor": "grey"
})
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n=n-1) + fib(n=n-2)
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
