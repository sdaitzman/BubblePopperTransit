#!/usr/bin/env python3
import networkx as nx

i = 1
j = 3

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

G.add_weighted_edges_from([(1, 2, 1), (1, 3, 7), (1, 4, 1), (3, 4, 1)])

dist = {}
visited = []
queue = []
path = []

for n in G.nodes:
    queue.append(n)
    if n != i:
        dist[n] = 1000000000000
    else: 
        dist[n] = 0
        visited.append(n)


min = 1000000000000 
for k in dist:
    node = k
    break

for n in dist:
    if dist[n] < min: 
        min = dist[n]
        node = n
    
