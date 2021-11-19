# -*- coding: utf-8 -*-
"""SMA3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13X_PUMk_Ieo9tOIivN9oISdCwvtEhZil
"""

from google.colab import drive
drive.mount('/content/drive')

!cd "/content/drive/MyDrive/Assignment-1/"

from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt
from numpy import random
import time
import networkx as nx
import networkx.algorithms.community as nx_comm

Kara_1 = nx.read_gml('/content/drive/MyDrive/Assignment-1/karate.gml', label = 'id')
Dolo_1 = nx.read_gml('/content/drive/MyDrive/Assignment-1/dolphins.gml')
Jazz_1 = nx.read_weighted_edgelist('/content/drive/MyDrive/Assignment-1/jazz.net')

# Karate_DataSet

adjacency_matrix = nx.to_numpy_matrix(Kara_1)
seconds_old = time.time()
S_C = SpectralClustering(n_clusters=4, affinity='precomputed', n_init=100)

# Communities in the graph
S_C.fit(adjacency_matrix)

seconds_new = time.time()
print("Time taken for Karate DataSet: ", seconds_new - seconds_old)

# Nodes in the communities
labels = S_C.labels_

ls = [[] for i in range(4)]

i = 1
for x in labels:
    if(x == 0):
        ls[0].append(i)
        i += 1
    elif(x == 1):
        ls[1].append(i)
        i += 1
    elif(x == 2):
        ls[2].append(i)
        i += 1
    elif(x == 3):
        ls[3].append(i)
        i += 1
        
print("Number of Clusters in Karate DataSet: ")
print(len(ls))
print("Clusters in Karate DataSet: ")
print(ls)
 
print("Modularity : " + str(nx_comm.modularity(Kara_1, ls)))
print("#################################################################################")


# Dolphins DataSet

adjacency_matrix = nx.to_numpy_matrix(Dolo_1)

# Converting into List
lsg2 = list(Dolo_1)

seconds_old = time.time()

S_C = SpectralClustering(n_clusters=4, affinity='precomputed', n_init=100)

# Communities in the graph
S_C.fit(adjacency_matrix)

seconds_new = time.time()
print("Time taken for Dolphins DataSet : ", seconds_new - seconds_old)

# find the nodes forming the communities
labels = S_C.labels_

ls = [[] for i in range(4)]

i = 0
for x in labels:
    if(x == 0):
        ls[0].append(lsg2[i])
        i += 1
    elif(x == 1):
        ls[1].append(lsg2[i])
        i += 1
    elif(x == 2):
        ls[2].append(lsg2[i])
        i += 1
    elif(x == 3):
        ls[3].append(lsg2[i])
        i += 1
        
print("Number of Clusters in Dolphins DataSet  : ")
print(len(ls)) 
print("Clusters in Dolphins DataSet : ")
print(ls)

print("Modularity : " + str(nx_comm.modularity(Dolo_1, ls)))
print("#################################################################################")


# Jazz DataSet

adjacency_matrix = nx.to_numpy_matrix(Jazz_1)

seconds_old = time.time()

S_C = SpectralClustering(n_clusters=4, affinity='precomputed', n_init=100)

# Communities in the graph
S_C.fit(adj_matrix)

seconds_new = time.time()
print("Time taken for Jazz DataSet: ", seconds_new - seconds_old)

# Nodes in Communities
labels = S_C.labels_

ls = [[] for i in range(4)]

i = 1
for x in labels:
    if(x == 0):
        ls[0].append(str(i))
        i += 1
    elif(x == 1):
        ls[1].append(str(i))
        i += 1
    elif(x == 2):
        ls[2].append(str(i))
        i += 1
    elif(x == 3):
        ls[3].append(str(i))
        i += 1
        
print("Number of Clusters in Jazz DataSet: ")
print(len(ls)) 
print("Clusters in Jazz DataSet : ")
print(ls)

print("Modularity : " + str(nx_comm.modularity(Jazz_1, ls)))
print("#################################################################################")