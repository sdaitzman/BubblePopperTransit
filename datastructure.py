#!/usr/bin/env python3
import matplotlib.pyplot as plt
import networkx as nx

class LocationNode:
    '''
    LocationNode class
    Represents a node along the map, a location with some TransitEdges in/out
    self.name: [string] Name of this node
    self.coords: [enum: (lat, lon)] Location
    '''
    def __init__(self, name=None, coords=None):
        self.name = name     # name of this node
        self.coords = coords # (lat, lon)

class TransitEdge:
    '''
    TransitEdge class
    @Dhara: for now, implement with self.timing [number] as number of minutes
        to traverse an edge only, no Timing implementation here yet.


    Stores data about the time a transit mode takes
    self.start: [LocationNode] TransitNode at beginning of pathway
    self.to: [LocationNode] TransitNode at end of pathway
    self.cost: [number] Cost in USD to follow this path
    self.type: [string] Type of transit, e.g. redline, greenline, car, walk,
        bike, bus, commuterrail, lyft
    self.calories: [number] Number of calories burned in traversing this mode
    self.timing: [Timing || number] Time to traverse this edge. If a number is
        passed, it will be converted to a constant time traversal Timing object
        with a traversal time in minutes.
    '''
    def __init__(self, start=None, to=None, cost=0, type=None, calories=0, timing=None):
        self.start = start
        self.to = to
        self.cost = cost
        self.type = type
        self.calories = calories
        self.timing = timing

class Timing:
    '''
    Timing class
    Stores the time it takes to traverse an edge
    '''
    def __init__(self, timingType='immediate', averageTime=0, etd=0):
        self.timingType = timingType
        self.averageTime = averageTime
        self.etd = etd

# --- UTILITY METHODS --- #
def dist(start, to):
    '''
    dist function
    Calculates the distance between one position and another
    start: [enum: (lat, lon)] one node
    to: [enum: (lat, lon)] another node
    '''
    # TODO: implement
    print(start.coords)
    print(to.coords)


G = nx.MultiDiGraph()

olin = LocationNode([1,1])
eliot = LocationNode([0,0])

G.add_node(eliot)
G.add_node(olin)

G.add_edge(olin, eliot, length = 3)


print(G.edges)

pos = nx.spring_layout(G)
edge_labels=dict([((u,v,),d['length']) for u,v,d in G.edges(data=True)])
nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=7)


# plt.show()