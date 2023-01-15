#!/usr/bin/env python3
"""
Генерируем случайный граф
"""
import matplotlib.pyplot as plt
from graph3 import dfs_path
import networkx as nx
from itertools import combinations
from random import random


def ER(n, p):
    V = set([v for v in range(n)])
    E = set()
    for combination in combinations(V, 2):
        a = random()
        if a < p:
            E.add(combination)

    g = nx.Graph()
    g.add_nodes_from(V)
    g.add_edges_from(E)

    return g


if __name__ == "__main__":
    n = 10
    p = 0.4
    G = ER(n, p)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    # превратим в словарь смежности
    g = dict(G.adjacency())
    path = dfs_path(g, 1, 8)
    plt.title(f"Путь от вершины 1 к вершине 8: {path}")
    plt.show()
