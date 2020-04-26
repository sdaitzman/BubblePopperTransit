#!/usr/bin/env python3
#Initial shortest path implementation using Dijkstra's algorithm
import networkx as nx
import datastructure as ds

def dijkstra(G, i, j,weights):
    """
    Returns the shortest path from i to j in graph G
    G: graph 
    i: start node (type: LocationNode)
    j: end node (type: LocationNode)
    weights: dictionary of weights for criteria specified by user
    """

    e = G.edges
    dist = {}
    visited = []
    path = []

    #set all distances to infinity 
    for n in G.nodes:
        if n != i:
            dist[n] = float('inf')
        else: 
            dist[n] = 0
            visited.append(n)
    

    while visited != []:
        current = visited.pop(0) #remove first item 

        if current == j: #destination reached 
            break
        else:
            next = findNext(current,G,w) #finds the best neighbor depending on the weights
            path.append(next)

    return path

def findNext(current,G,weights):
    """
    Finds the best neighbor depending on the weights 
    current: current LocationNode
    G: graph containing LocationNodes
    weights: dictionary of weights for criteria specified by user
    """

    next = G.neighbors[0] #first LocationNode in the list of its neighbors

    for edge in G.current.edges: #iterate through every edge for that node
        myScore = score(edge,weights)
        if myScore < score(G.next,weights): #if better score than best
            next = edge

    return next
            
def score(edge,weights):
    '''
    Give an edge a weighted sum according to the weights assigned by the user 
    '''
    for i in range(len(weights)):
        score = score + edge[i]*weights[i]

#Testing 
G = nx.MultiDiGraph()

olin = ds.LocationNode([1,1])
eliot = ds.LocationNode([0,0])

G.add_node(eliot)
G.add_node(olin)

uberTime = ds.Timing('immediate',15)
uber = ds.TransitEdge(olin,eliot,8,'uber',0,uberTime)