import igraph as ig
import time
from sample import *
from summary import *

kmax = 7
alpha = 0.01
N = 10
delta = 0.05
size = [150]
neigh = 6
rewiring = 0.05
n = 500


timestart = time.time()
G = ig.Graph.Watts_Strogatz(
    dim=1, size=n, nei=neigh, p=rewiring, loops=False, multiple=False
)
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
    "Network summary of a graph following the Watts-Strogatz model",
    "alpha="
    + str(alpha)
    + ", nb_vx="
    + str(n)
    + ", sub_size="
    + str(size)
    + ", nb_neigh="
    + str(neigh)
    + ", rewiring_prob="
    + str(rewiring),
)
