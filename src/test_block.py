import igraph as ig
import time
from sample import *
from summary import *

kmax=7
alpha=0.5
delta=0.05
size=33
blc_size=[30,70]
pm=[[0.5,0.1],[0.1,0.5]]
n=100
R=math.ceil((1/2/alpha*phi_inv(1-alpha/(2*(kmax-1))))**2)
print(R)

timestart=time.time()
G = ig.Graph.SBM(n=n, pref_matrix=pm, block_sizes=blc_size,directed=False,loops=False)
#slist = sample_number(G,kmax,alpha,N,delta)
#timemid=time.time()
tk = Network_summary(G,[size],kmax,alpha)
timeend=time.time()

#print(timemid-timestart)
#print(timeend-timemid)
print(timeend-timestart)
violinplot(tk,kmax,"Network summary of a graph following the Block model","alpha="+str(alpha)+", nb_vx="+str(n)+", sub_size="+str(size)+", prefmat="+str(pm)+", blc_size="+str(blc_size))