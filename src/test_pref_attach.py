import igraph as ig
import time
from sample import *
from summary import *
kmax=7
alpha=0.05
N=10
delta=0.05
size=33
edges=1
n=100


timestart=time.time()
G = ig.Graph.Barabasi(n=n, m=edges, directed=False)
#slist = sample_number(G,kmax,alpha,N,delta)
#timemid=time.time()
tk = Network_summary(G,[size],kmax,alpha)
timeend=time.time()

#print(timemid-timestart)
#print(timeend-timemid)
print(timeend-timestart)
violinplot(tk,kmax,"Network summary of a graph following the Barabási-Albert model","alpha="+str(alpha)+", nb_vx="+str(n)+", sub_size="+str(size)+", m="+str(edges))