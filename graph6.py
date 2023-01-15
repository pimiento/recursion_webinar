#!/usr/bin/env python3
from graph import Graph
from graph5 import bfs_path

import networkx as nx
import matplotlib.pyplot as plt


if __name__ == "__main__":
    with open("routes.txt", "r") as fd:
        edges = [l.strip().split() for l in fd.readlines()]
    # g = Graph.from_edges(edges).adj_dict
    g = nx.Graph(edges)
    pos = nx.spring_layout(g)
    nx.draw_networkx(g, pos)
    src = input("Аэропорт отправления: ")
    dst = input("Аэропорт прибытия: ")

    path = bfs_path(g, src, dst)
    # path = nx.shortest_path(g, src, dst)
    plt.title(f"Как добраться от {src} до {dst}: {path}")
    plt.show()
