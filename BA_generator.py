import random
import networkx as nx
import networkx.utils as utils
import matplotlib.pyplot as plt
import numpy as np

def generate_barabasi_albert_nicer(N, m):                                              
     ''' Generates BA graph in a bit nicer fashion starting from                        
     complete graph of m nodes following the suggestions in the labscript'''            
     edge_weighted_list = [] # list of all vertices, occuring k-times                   
                                                                                        
     # Prepare the initial graph (complete graph)                                       
     # such that the edge number satisfies the                                          
     # BA invariant at any time                                                         
     # Graph of m+1 nodes => each node has degree m                                     
     graph = nx.complete_graph(m + 1)                                                   
     nodes = nx.nodes_iter(graph)                                                       
                                                                                        
     # Insert the nodes m times in the list
     for node in nodes :                                                                
         edge_weighted_list.extend([node] * m) # append the node m x

     for time in xrange(m+1, N) : # Here is the issue! 
         graph.add_node(time)                                                           
         
         # Prepare the edges
         targets = []
         for edges in xrange(0,  m) :                                                   
            # Pick a target at random for each edge
            
            # Avoid attaching edge to the same node twice
            edge_attached = False
            while edge_attached == False:
                 target = edge_weighted_list[random.randint(0, len(edge_weighted_list) - 1)] 
                 if graph.has_edge(time, target) == False:
                   break

            graph.add_edge(time, target)                                                
            targets.append(target)
        
         # Insert the graph
         edge_weighted_list.extend([time]*m)                                             
         
          # Append nodes which have been gifted an edge
         edge_weighted_list.extend(targets) 
    
     
     return graph                                                                       

def degree_distribution(G):
    '''Returns a degree distribution of a graph as a numpy array'''
    N = G.number_of_nodes()
    distribution = np.zeros(N) # The highest possible degree in BA is N   
    for node in G.nodes_iter() :                                          
      distribution[len(G[node])] += 1  # Increment the distribution by 1  
                                                                          
    distribution /= float(N) # Normalize the distribution                 

    return distribution

def theoretical_probability_distribution(k, m):
    ''' Returns a theoretical probability distribution. 
        Supply k as a numpy array of degrees of interest
        (x axis)'''
    m = float(m)
    p = np.zeros(len(k))
    r = k[m:] # accept only relevant degrees

    p[m:] = 2*(m+1)*m/(r*(r+1)*(r+2))

    return p

def cumulative_distribution(G) :
     ''' Returns a cumulative distribution from a Graph nodes
         Plot the first row against the second'''
     nodes = G.nodes()
     degrees = G.degree().values()
     degrees.sort(None, None, True)

     rank = range(1, len(degrees) + 1)
     
     return rank, degrees


     

     
     


