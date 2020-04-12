#!/usr/bin/env python3
import matplotlib.pyplot as plt
import networkx as nx


G = nx.DiGraph()
G.add_node('Olin')
G.add_node('Eliot')

G.add_edge('Olin', 'Eliot', length = 3)
G.add_edge('Eliot', 'Olin', length = 8)

pos = nx.spring_layout(G)

edge_labels=dict([((u,v,),d['length']) for u,v,d in G.edges(data=True)])

nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=7)

plt.style.use("cyberpunk")

plt.show()