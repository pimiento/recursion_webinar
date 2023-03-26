#!/usr/bin/env python3
import sys
import timeit
from typing import List
def sort_alg(L: List[int]]) -> List:
    if L:
        return (
            sort_alg(
        [e for e in L[1:] if e<L[0]]
            ) +
            L[0:1] +
            sort_alg(
        [e for e in L[1:] if e>=L[0]]
            )
        )
    return []
if __name__ == "__main__":
    int_count = sys.argv[1]
    with open(f"data/{int_count}ints.txt", "r") as data:
        arr: List[int] = [int(line.strip()) for line in data.readlines()]
        number:int = 2
        def to_call():
            return sort_alg(arr)
        result = timeit.timeit(to_call, number=number)
        print(
            f"{number} вызовов для {int_count} данных: лучший результат равен {result:.02f}"
        )
        result = sort_alg(arr)
        for i in range(len(result)-1):
            assert result[i] < result[i+1]
