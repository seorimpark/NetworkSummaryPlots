import igraph as ig
import time
from sample import *
from summary import *

kmax = 7
alpha = 0.01
N = 5
delta = 0.05
size = [100]
edges = 4
n = 200

G = ig.Graph.Barabasi(n=n, m=edges, directed=False)
timestart = time.time()
size = sample_number(G, kmax, alpha, N, delta)
timemid = time.time()
print(timemid - timestart)
tk = Network_summary(G, size, kmax, alpha)
timeend = time.time()
print(timeend - timemid)
print(timeend - timestart)
violinplot(
    tk,
    kmax,
    "Network summary of a graph following the Barabási-Albert model",
    "alpha="
    + str(alpha)
    + ", nb_vx="
    + str(n)
    + ", sub_size="
    + str(size)
    + ", m="
    + str(edges),
)
