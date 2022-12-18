from summary import *
import time
n=1000
size=100
kmax=7
alpha=0.01

B=ig.Graph.Random_Bipartite(500,500,p=0.5,directed=False)
timestart=time.time()
tk = Network_summary(B,[size],kmax,alpha)
timeend=time.time()
print(timeend-timestart)
violinplot(tk,kmax,"Network summary of a bipartite graph","alpha="+str(alpha)+", nb_vx="+str(n)+", sub_size="+str(size))