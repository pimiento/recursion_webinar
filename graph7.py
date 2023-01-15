#!/usr/bin/env python3
"""
Топологическая сортировка
"""
import matplotlib.pyplot as plt
import networkx as nx


# DAG — Directed Acyclic Graph
dag = nx.DiGraph([
    ("calculus", "linear algebra"),
    ("linear algebra", "theoretical cs"),
    ("algorithms", "theoretical cs"),
    ("algorithms", "databases"),
    ("algorithms", "scientific computing"),
    ("introduction to cs", "algorithms"),
    ("introduction to cs", "advanced programming"),
    ("advanced programming", "scientific computing"),
    ("scientific computing", "computational biology"),
    ("theoretical cs", "computational biology"),
    ("theoretical cs", "artificial intelligence"),
    ("artificial intelligence", "robotics"),
    ("artificial intelligence", "machine learning"),
    ("artificial intelligence", "neural networks"),
    ("machine learning", "neural networks"),
    ("neural networks", "deep learning")
])
pos = nx.spring_layout(dag)
nx.draw_networkx(dag, pos)
plt.show()
for e in nx.topological_sort(dag):
    print(e)
