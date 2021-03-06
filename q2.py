# -*- coding: utf-8 -*-
"""sma_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oKn1ezo3gU4hLyzUbc2tZC3VXoj0eB0z
"""

from google.colab import drive
drive.mount('/content/drive')

!cd "/content/drive/MyDrive/Assignment-1/"

from networkx.algorithms.community.modularity_max import greedy_modularity_communities
import time
import networkx as nx
import networkx.algorithms.community as nx_comm

Kara_1 = nx.read_gml('/content/drive/MyDrive/Assignment-1/karate.gml', label = 'id')
Dolo_1 = nx.read_gml('/content/drive/MyDrive/Assignment-1/dolphins.gml')
Jazz_1 = nx.read_weighted_edgelist('/content/drive/MyDrive/Assignment-1/jazz.net')

# Karate DataSet
seconds_old = time.time()

# Communities in the graph
Community_1 = greedy_modularity_communities(Kara_1)

# Nodes in the graph forming Communities
Nodes_1 = (list(sorted(c) for c in Community_1))

print("Clusters in Karate_DatSet : ")
print(Nodes_1)   
print("Number of Clusters : ")
print(len(Nodes_1))  
print("Modularity of Karate DataSet : " + str(nx_comm.modularity(Kara_1, Nodes_1)))
seconds_new = time.time()
print("Time taken for Karate DataSet ", seconds_new - seconds_old)
print("\n**************************************************************************\n")





# Dolphins DataSet
seconds_old = time.time()

# Communities in the graph
Community_2 = greedy_modularity_communities(Dolo_1)

# Nodes in the graph forming Communities
Nodes_2 = (list(sorted(c) for c in Community_2))

print("Clusters in Dolphin DataSet: ")
print(Nodes_2)   
print("Number of Clusters : ")
print(len(Nodes_2))  
print("Modularity of Dolphin DataSet: " + str(nx_comm.modularity(Dolo_1, Nodes_2)))
seconds_new = time.time()
print("Time taken for Dolphin DataSet: ", seconds_new - seconds_old)
print("\n**************************************************************************\n")






# Jazz DataSet
seconds_old = time.time()

# Communities in the graph
Community_3 = greedy_modularity_communities(Jazz_1)

# Nodes in the graph forming Communities
Nodes_3 = (list(sorted(c) for c in Community_3))

print("Clusters of Jazz DataSet: ")
print(Nodes_3)   
print("Number of Clusters : ")
print(len(Nodes_3))  
print("Modularity of Jazz DataSet: " + str(nx_comm.modularity(Jazz_1, Nodes_3)))


seconds_new = time.time()
print("Time taken for Jazz DataSet: ", seconds_new - seconds_old)

