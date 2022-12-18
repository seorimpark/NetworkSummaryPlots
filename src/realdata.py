import scipy.io
import igraph as ig
import time
import datetime
from sample import *
from summary import *

filestart = time.time()

# for data in mtx format:

# mat2= scipy.io.mmread("../data/power.mtx")
# M=mat2.toarray()
# G=ig.Graph.Adjacency(M.tolist(), mode='undirected')

# for txt data containing the list of edges:

G = ig.Graph.Read_Edgelist("data/data2.txt", directed=False)


fileend = time.time()
print(fileend - filestart)

print(datetime.datetime.now())

kmax = 7
alpha = 0.05
delta = 0.05
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
    "Network summary of mouse genes",
    "alpha=" + str(alpha) + ", nb_vx=" + str(len(G.vs)) + ", sub_size=" + str(size),
)
