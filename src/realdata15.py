import scipy.io
import igraph as ig
import time
import math
from sample import *
from summary import *
import networkx as nx
#Read data files
l=[]
p=-math.inf
with open ("../data/plant.csv","r") as file:
    for line in file:
        a1,b1=line.split(",")
        a=int(a1)
        b=int(b1)
        l.append((a,b))
        if p<a or p<b:
            p=max(a,b)
print(p)

g=ig.Graph()
g.add_vertices(p+1)
g.add_edges(l)

m=g.get_adjacency()
M=np.array(m.data)

#Data preprocessing: make it as an undirected graph without self loops and no multiple edges on two vertices. 
for i in range(len(M)):
    for j in range(len(M)):
        if M[i,j]>0:
            M[i,j]=1
        if M[i,j]<0:
            M[i,j]=1
        if M[i,j]!=M[j,i]:
            if max(M[i,j],M[j,i])>0:
                M[i,j]=1
                M[j,i]=1
            else:
                M[i,j]=0
                M[j,i]=0
        if M[i,i]!=0:
            M[i,i]=0
print(M)
kmax=7
alpha=0.05
N=21
delta=0.05
size=700
G=ig.Graph.Adjacency(M.tolist())
timestart=time.time()
#slist = sample_number(G,kmax,alpha,N,delta)
#timemid=time.time()
tk = Network_summary(G,[size],kmax,alpha)
timeend=time.time()

#print(timemid-timestart)
#print(timeend-timemid)
print(timeend-timestart)
violinplot(tk,kmax,"Network summary of plants and pollinators from southwestern Illinois","alpha="+str(alpha)+", nb_vx="+str(len(M))+", sub_size="+str(size))