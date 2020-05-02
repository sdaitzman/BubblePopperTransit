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
    queue = []
    path = [i]

    #set all distances to infinity 
    for n in G.nodes:
        queue.append(n)
        if n != i:
            dist[n] = 1000000000000
        else: 
            dist[n] = 0
            visited.append(n)
    

    while queue != []:
        next = findNext(G,dist,weights) #find the node with the minimum distance in dist dictionary
        print(queue)
        visited.append(next[0]) #add to visited
        queue.remove(next[0])
        path.append(next[0])
        neighbors = findNbrs(G,next[0])
        for n in neighbors:
            if dist[n] > next[1] + neighbors[n]['weight']:
                dist[n] = next[1] + neighbors[n]['weight']
                
                

    return path

def findNext(G, dist, weights):
    """
    Finds the best neighbor depending on the weights 
    G: graph containing LocationNodes
    dist: dictionary of distances 
    weights: dictionary of weights for criteria specified by user #TODO: implement weighted sums 
    """

    min = 10000000000 
    for k in dist:
        node = k
        break

    for n in dist:
        if dist[n] < min: 
            min = dist[n]
            node = n
    
    return [n,min]

def findNbrs(G,next):
    for n in G.adj.items():
        if n[0] == next:
            return n[1] #a dictionary of all the neighbors and associated weights of each edge

def score(edge,weights):
    '''
    Give an edge a weighted sum according to the weights assigned by the user 
    '''
    for i in range(len(weights)):
        score = score + edge[i]*weights[i]

#Testing 
'''G = nx.MultiDiGraph()

olin = ds.LocationNode([1,1])
eliot = ds.LocationNode([0,0])

G.add_node(eliot)
G.add_node(olin)

uberTime = ds.Timing('immediate',15)
uber = ds.TransitEdge(olin,eliot,8,'uber',0,uberTime)'''
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

G.add_weighted_edges_from([(1, 2, 1), (1, 3, 7), (1, 4, 1), (3, 4, 1)])

dijkstra(G,1,3,[1,1,1,1])
    