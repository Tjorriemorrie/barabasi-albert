''' Networks project 
    Imperial College 2014
    Vojtech Havlicek '''

import os
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Seed 
random.seed(10)

# Checking the betweeness centrality
# graph = nx.Graph()
# 
# graph.add_node("Euclid")
# graph.add_node("Galileo")
# graph.add_node("Mersenne")
# graph.add_node("Newton")
# graph.add_node("Huygens")
# 
# graph.add_edge("Euclid","Galileo")
# graph.add_edge("Euclid","Newton")
# graph.add_edge("Galileo","Mersenne")
# graph.add_edge("Newton","Huygens")
# graph.add_edge("Huygens", "Mersenne")
# graph.add_edge("Newton", "Galileo")
# graph.add_edge("Huygens", "Galileo")
# 
# nx.draw(graph, pos = nx.spring_layout(graph), with_labels = True)
# 
# print nx.betweenness_centrality(graph,  normalized = False)
# print nx.edge_betweenness_centrality(graph, normalized = False)
# print nx.clustering(graph)
# print nx.average_clustering(graph)

def generate_barabasi_albert(N, m):
  ''' Returns networkx.Graph object. Generates a Barabasi Albert
      graph of nx.nodes'''
  graph = nx.Graph()
  nodes_to_add = 0;             

  while nodes_to_add < N :
    to_connect = []                # List of nodes to connect to newly added
    
    counter = 0                     
    while counter < m :                # For each branch to be connected
        rnd = random.random()          # generate a random number
        
        nodes = nx.nodes_iter(graph)   # Iterate over all nodes of the graph
        temp = 0.0                     # create a temp variable
        edges = len(graph.edges())     

        # Populate to_connect
        for node in nodes : 
            if len(graph.edges()) == 0 : 
               # If no edge is present in graph, avoid divergence
               temp = 1.0
            else :
               # Otherwise increase value of temp proportionaly
               temp += float(len(graph.neighbors(node)))/float(2*edges) 

            if temp > rnd :
               # If temp is larger than rnd, add the BA node
               to_connect.append(node)
               break
        counter += 1

    # Connect the new node
    graph.add_node(nodes_to_add)
    for node in to_connect :
        graph.add_edge(node, nodes_to_add)

    nodes_to_add += 1

  return graph

G = generate_barabasi_albert(50, 2)
nx.draw(G, pos=nx.spring_layout(G))

plt.draw()
plt.show()


