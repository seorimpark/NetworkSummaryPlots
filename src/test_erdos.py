import numpy as np
import math
from sample import *
from summary import *
import time
kmax=7
alpha=0.05
N=10
delta=0.05
R=math.ceil((1/2/alpha*phi_inv(1-alpha/(2*(kmax-1))))**2)
size=100
p=0.5
n=300


timestart=time.time()
G = ig.Graph.Erdos_Renyi(n=n, p=p, directed=False, loops=False)
#slist = sample_number(G,kmax,alpha,N,delta)
#timemid=time.time()
tk = Network_summary(G,[size],kmax,alpha)
timeend=time.time()

#print(timemid-timestart)
#print(timeend-timemid)
print(timeend-timestart)
violinplot(tk,kmax,"Network summary of a graph following the Erdős–Rényi model","alpha="+str(alpha)+", nb_vx="+str(n)+", sub_size="+str(size)+", p="+str(p))