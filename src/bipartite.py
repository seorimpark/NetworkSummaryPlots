from sample import *
from summary import *
import time

n = 1000
size = 100
kmax = 7
alpha = 0.01
delta = 0.05
N = 5
p = 200
B = ig.Graph.Random_Bipartite(p, n - p, p=0.5, directed=False)
timestart = time.time()
# size = sample_number(B, kmax, alpha, N, delta)
timemid = time.time()
tk = Network_summary(B, [size], kmax, alpha)
timeend = time.time()

print(timemid - timestart)
print(timeend - timemid)
print(timeend - timestart)
violinplot(
    tk,
    kmax,
    "Network summary of a bipartite graph",
    "alpha="
    + str(alpha)
    + ", nb_vx="
    + str(n)
    + ", community_size="
    + str(p)
    + ", sub_size="
    + str(size),
)
