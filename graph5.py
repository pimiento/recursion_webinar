#!/usr/bin/env python3
"""
Breadth-first search: поиск вширину
"""
from graph4 import ER

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def bfs_path(g, v, w):
    edge_to = {}
    q = deque(maxlen=len(g))
    marked = {v: True}
    q.append(v)
    while q:
        start = q.popleft()
        for n in g[start]:
            if n not in marked:
                edge_to[n] = start
                marked[n] = True
                q.append(n)
    # Найдём кратчайший путь
    p = deque(maxlen=len(g))
    x = w
    while x != v:
        p.appendleft(x)
        x = edge_to[x]
    p.appendleft(x)
    return list(p)


if __name__ == "__main__":
    n = 10
    p = 0.3
    G = ER(n, p)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    # превратим в словарь смежности
    g = dict(G.adjacency())
    path = bfs_path(g, 1, 8)
    plt.title(f"Путь от вершины 1 к вершине 8: {path}")
    plt.show()
