#!/usr/bin/env python3
"""DFS Path"""
from graph import Graph

def dfs_path(g, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end: return path
    if start not in g: return None
    for v in g[start]:
        if v not in path:
            ext_path = dfs_path(g, v, end, path)
            if ext_path is not None:
                return ext_path
    return None


if __name__ == "__main__":
    edges = [('a', 'b'), ('a', 'c'), ('b', 'a'), ('c', 'd')]
    g = Graph.from_edges(edges)
    print(dfs_path(g.adj_dict, "a", "d"))
