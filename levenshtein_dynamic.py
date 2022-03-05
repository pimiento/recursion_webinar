#!/usr/bin/env python3
from typing import List, Tuple


MATCH, INSERT, DELETE = [0, 1, 2]


def row_init(j, m):
    # m[0][j] = {"cost": j, "parent": -1}
    m[0][j] = {
        "cost": j,
        "parent": INSERT if j > 0 else -1
    }

def col_init(i, m):
    # m[i][0] = {"cost": i, "parent": -1}
    m[i][0] = {
        "cost": i,
        "parent": DELETE if i > 0 else -1
    }

def match(a: str, b: str) -> int:
    return (a != b)


def cost(c: str) -> int:
    return 1


def goal_cell(a: str, b: str, i: int, j: int, m: List[List[dict]]) -> Tuple[int, int]:
    # for k in range(len(b)-1):
    #     if m[i][k]["cost"] < m[i][j]["cost"]:
    #         j = k
    # return i, j
    i = len(a)-1
    j = len(b)-1
    return i, j


def levenshtein(a: str, b: str, m: List[List[dict]]) -> int:
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if m[i][j] is None:
                m[i][j] = {"parent": -1}
            match_insert_delete = [
                m[i-1][j-1]["cost"] + match(a[i], b[j]),
                m[i][j-1]["cost"] + cost(''),
                m[i-1][j]["cost"] + cost('')
            ]
            m[i][j]["cost"] = min(match_insert_delete)
            m[i][j]["parent"] = match_insert_delete.index(m[i][j]["cost"])
    i, j = goal_cell(a, b, i, j, m)
    return m[i][j]["cost"]


def lev(a: str, b: str) -> Tuple[int, List[List[dict]]]:
    a = " " + a
    b = " " + b
    m = [[None] * (len(b)) for i in range(len(a))]

    for i in range(len(a)):
        col_init(i,m)
    for j in range(len(b)):
        row_init(j, m)

    return levenshtein(a, b, m), m

def insert_out(b: str, j: int) -> None:
    print(f"I: {b[j]}")

def delete_out(a: str, i: int) -> None:
    print(f"D: {a[i]}")

def match_out(a: str, b: str, i: int, j: int) -> None:
    if a[i] == b[j]:
        print(f"M: {a[i]}")
    else:
        print(f"S: {a[i]} -> {b[j]}")

def reconstruct_path(a: str, b: str, i: int, j: int, m: List[List[dict]]) -> None:
    parent = m[i][j]["parent"]
    # print(f"i: {i}\tj: {j}\tparent: {parent}")
    if parent == MATCH:
        reconstruct_path(a, b, i-1, j-1, m)
        match_out(a, b, i-1, j-1)
    elif parent == INSERT:
        reconstruct_path(a, b, i, j-1, m)
        insert_out(b, j-1)
    elif parent == DELETE:
        reconstruct_path(a, b, i-1, j, m)
        delete_out(a, i-1)
    else:
        return

b = "ура"
a = "культура"
result, m = lev(a, b)
print(result)
print("----------------------")
for row in m:
    print(' '.join(f"{cell['cost']:2d}" for cell in row))
print("--cost--^--parent--v--")
for row in m:
    print(' '.join(f"{cell['parent']:2d}" for cell in row))
print("----------------------")
reconstruct_path(a, b, len(a), len(b), m)
