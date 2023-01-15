#!/usr/bin/env python3
"""Реализация ненаправленного графа. DFS"""
from graph import Graph
from collections import defaultdict

class Graph(Graph):

    def dfs(self, v):
        """
        Поиск вглубину.
        Возвращает список вершин, достижимых из заданной
        """
        marked = {}
        count = 0
        def _dfs(G, v):
            nonlocal count
            marked[v] = True
            count += 1
            for w in G.adj(v):
                if not marked.get(w, False):
                    _dfs(G, w)
        _dfs(self, v)
        return list(marked.keys())

if __name__ == "__main__":
    edges = [('a', 'b'), ('a', 'c'), ('b', 'a'), ('c', 'd')]
    g = Graph.from_edges(edges)
    print(g.dfs("a"))
