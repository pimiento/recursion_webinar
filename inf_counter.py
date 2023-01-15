#!/usr/bin/env python3
def inf_counter(x):
    print(x)
    return inf_counter(x+1)
inf_counter(0)
