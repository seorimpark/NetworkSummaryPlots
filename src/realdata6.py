import scipy.io
import igraph as ig
import time
from sample import *
from summary import *
import networkx as nx
import math
#Read data files
y5=[]
y6=[]
y7=[]
y8=[]
y9=[]
y10=[]
y11=[]
y12=[]
y13=[]
with open("../data/reptilia-tortoise-network-fi.edges", 'r') as file:
    p=-math.inf
    for line in file:
        a1,b1,c=line.split(" ")
        a=int(a1)
        b=int(b1)
        year=int(c[0:4])
        if year==2005:
            y5.append((a,b))
        if year==2006:
            y6.append((a,b))
        if year==2007:
            y7.append((a,b))
        if year==2008:
            y8.append((a,b))
        if year==2009:
            y9.append((a,b))
        if year==2010:
            y10.append((a,b))
        if year==2011:
            y11.append((a,b))
        if year==2012:
            y12.append((a,b))
        if year==2013:
            y13.append((a,b))
        if p<a or p<b:
            p=max(a,b)
        
print(y5)
print(p)
g5=ig.Graph()
g5.add_vertices(787)
g5.add_edges(y5)

kmax=7
alpha=0.05
N=21
delta=0.05
size=100
timestart=time.time()
#slist = sample_number(G,kmax,alpha,N,delta)
#timemid=time.time()
tk = Network_summary(g5,[size],kmax,alpha)
timeend=time.time()
violinplot(tk,kmax,"Network summary of the network of tortoise","alpha="+str(alpha)+", nb_vx="+str(g5.vs)+", sub_size="+str(size))

#G=nx.read_edgelist("../data/data6.txt")
#g = ig.Graph.from_networkx(G)
#m=g.get_adjacency()
#M=np.array(m.data)
#Data preprocessing: make it as an undirected graph without self loops and no multiple edges on two vertices. 
# for i in range(len(M)):
#     for j in range(len(M)):
#         if M[i,j]>0:
#             M[i,j]=1
#         if M[i,j]<0:
#             M[i,j]=0
#         if M[i,j]!=M[j,i]:
#             if max(M[i,j],M[j,i])>0:
#                 M[i,j]=1
#                 M[j,i]=1
#             else:
#                 M[i,j]=0
#                 M[j,i]=0
#         if M[i,i]!=0:
#             M[i,i]=0

# kmax=7
# alpha=0.05
# N=21
# delta=0.05
# size=500
# G=ig.Graph.Adjacency(M.tolist())
# timestart=time.time()
# #slist = sample_number(G,kmax,alpha,N,delta)
# #timemid=time.time()
# tk = Network_summary(G,[size],kmax,alpha)
# timeend=time.time()

# #print(timemid-timestart)
# #print(timeend-timemid)
# print(timeend-timestart)
# violinplot(tk,kmax,"Network summary of the network of tortoise","alpha="+str(alpha)+", nb_vx="+str(len(M))+", sub_size="+str(size))