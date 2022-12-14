from __future__ import generator_stop
import scipy.io
import igraph as ig
import time
import datetime
from sample import *
from summary import *

filestart = time.time()

# # for data in mtx format:

# mat2 = scipy.io.mmread("../data/polblogs.mtx")
# M = mat2.toarray()
# for i in range(len(M)):
#     for j in range(len(M)):
#         if M[i, j] > 0:
#             M[i, j] = 1
#         if M[i, j] < 0:
#             M[i, j] = 0
#         if M[i, j] != M[j, i]:
#             if max(M[i, j], M[j, i]) > 0:
#                 M[i, j] = 1
#                 M[j, i] = 1
#             else:
#                 M[i, j] = 0
#                 M[j, i] = 0
#         if M[i, i] != 0:
#             M[i, i] = 0
# G = ig.Graph.Adjacency(M.tolist())
# G = G.simplify(multiple=True, loops=True, combine_edges="ignore")

# # for txt data containing the list of edges:

G = ig.Graph.Read_Edgelist("../data/datarob.txt", directed=True)

# l = []
# p = -math.inf
# with open("../data/plant.csv", "r") as file:
#     for line in file:
#         a1, b1 = line.split(",")
#         a = int(a1)
#         b = int(b1)
#         l.append((a, b))
#         if p < a or p < b:
#             p = max(a, b)
# print(p)

# g = ig.Graph()
# g.add_vertices(p + 1)
# g.add_edges(l)

m = G.get_adjacency()
M = np.array(m.data)

# Data preprocessing: make it as an undirected graph without self loops and no multiple edges on two vertices.
for i in range(len(M)):
    for j in range(len(M)):
        if M[i, j] > 0:
            M[i, j] = 1
        if M[i, j] < 0:
            M[i, j] = 1
        if M[i, j] != M[j, i]:
            if max(M[i, j], M[j, i]) > 0:
                M[i, j] = 1
                M[j, i] = 1
            else:
                M[i, j] = 0
                M[j, i] = 0
        if M[i, i] != 0:
            M[i, i] = 0
G = ig.Graph.Adjacency(M.tolist())

kmax = 7
alpha = 0.05
N = 21
delta = 0.05
size = 700
G = G.simplify(multiple=True, loops=True, combine_edges="ignore")
print("Number of vertices: " + str(len(G.vs)))
print("Number of edges: " + str(len(G.es)))
print("Edge density: " + str(G.density()))
print("Mean degree: " + str(np.mean(G.degree(list(G.vs), mode="all", loops=False)) / 2))
print("Assortativity: " + str(G.assortativity_degree(directed=False)))
print("Diameter: " + str(G.diameter(directed=False, unconn=True, weights=None)))
fileend = time.time()
print(fileend - filestart)

print(datetime.datetime.now())

kmax = 7
alpha = 0.01
delta = 0.05
# size = [2500]
times = time.time()
size = sample_number(G, kmax, alpha, 5, delta)
timestart = time.time()
print(timestart - times)
tk = Network_summary(G, size, kmax, alpha)
timeend = time.time()
print(timeend - timestart)
violinplot(
    tk,
    kmax,
    "Network summary plot of the network of voles (rob)",
    "alpha=" + str(alpha) + ", nb_vx=" + str(len(G.vs)) + ", sub_size=" + str(size),
)
