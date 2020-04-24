#!/usr/bin/env python3
#Initial shortest path implementation using Dijkstra's algorithm
import networkx as nx

def dijkstra(G, i, j):
    """
    Returns the shortest path from i to j in graph G
    G: graph 
    i: start node 
    j: end node 
    """

    w = G.edges
    dist = {}
    visited = []

    #set all distances to infinity 
    for n in G.nodes:
        if n != i:
            dist[n] = float('inf')
        else: 
            dist[n] = 0
            visited.append(n)
    

    while visited != []:
        node = visited.pop(0) #remove first item 
    
        if node == j: #destination reached 
            break

        adj = G.adj(node)


#Testing 
G = nx.Graph()