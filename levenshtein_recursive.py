#!/usr/bin/env python3
fname="levenshtein_recursive.gif"
from visualiser.visualiser import Visualiser as vs

@vs(node_properties_kwargs={
    "shape": "record",
    "color": "#f57542",
    "style": "filled",
    "fillcolor": "grey"
})
def lev(a: str, b: str) -> int:
    if not a: return len(b)
    if not b: return len(a)
    return min([
        lev(a[1:],b[1:])+(a[0]!=b[0]),
        lev(a[1:],b)+1,
        lev(a,b[1:])+1
    ])

def main():
    import io
    import sys
    lev("foo", "bar")
    vs.make_animation(fname.split(".")[0] + ".gif", delay=1)
    print(fname, end='')


if __name__ == "__main__":
    main()
