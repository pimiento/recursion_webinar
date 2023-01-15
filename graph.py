#!/usr/bin/env python3
"""Реализация ненаправленного графа"""
from collections import defaultdict

class Graph:

    def __init__(self):
        self.__adj_dict = defaultdict(set)
        # количество рёбер
        self.__E = 0

    @classmethod
    def from_edges(cls, edges):
        g = cls()
        for v,w in edges:
            g.add_edge(v, w)
        return g

    def to_edges(self):
        for edge in self.__adj_dict:
            for neighbour in self.__adj_dict[edge]:
                yield (edge, neighbour)

    @property
    def V(self):
        return len(self.__adj_dict)

    @property
    def E(self):
        return self.__E

    @property
    def adj_dict(self):
        # чтобы не было возможности изменить снаружи
        return self.__adj_dict.copy()

    def add_edge(self, v, w):
        if not (w in self.__adj_dict[v] or v in self.__adj_dict[w]):
            self.__adj_dict[v].add(w)
            self.__adj_dict[w].add(v)
            self.__E += 1

    def adj(self, v):
        return self.adj_dict[v]

    def __len__(self):
        """длина графа это количество его вершин"""
        return self.V


if __name__ == "__main__":
    edges = [('a', 'b'), ('a', 'c'), ('b', 'a'), ('c', 'd')]
    g = Graph.from_edges(edges)
    print(g.adj_dict)
    print(list(g.to_edges()))
