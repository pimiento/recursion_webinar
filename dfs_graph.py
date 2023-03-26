#!/usr/bin/env python3
import networkx as nx

G = (
    nx.internet_as_graphs
    .random_internet_as_graph(
        n=50, seed=42
    )
    .adj
)
def DFS(G, V, p=None):
    if p is None:
        p = []
    p += [V]
    for n in G[V]:
        if n not in p:
            p = DFS(G, n, p)
    return path
DFS(G, )
