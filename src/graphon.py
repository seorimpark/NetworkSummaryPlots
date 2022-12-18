import igraph as ig
import numpy as np
from summary import *
import time
def graphon(n,f):
    """
    Args:
    - n (int): total number of nodes
    - f (function): function to calculate the probability
    """
    xis=np.random.uniform(size=n)
    G=ig.Graph()
    G.add_vertices(n)
    for i in range(n):
        for j in range(i,n):
            if i!=j:
                xii=xis[i]
                xij=xis[j]
                edge=np.random.binomial(1,f(xii,xij),1)
                if edge[0]==1:
                    G.add_edge(i,j)
    return G


def f1(x,y):
    return abs(x-y)

def f2(x,y):
    return x*y

def f3(x,y):
    return (x+y)/2

def f4(x,y):
    return np.max([x,y])

def f5(x,y):
    return 

func1="abs(x-y)"
func2="x*y"
func3="(x+y)/2"
func4="max(x,y)"
func5=""
G=graphon(500,f1)
kmax=7
alpha=0.05
delta=0.05
size=100
timestart=time.time()
tk = Network_summary(G,[size],kmax,alpha)
timeend=time.time()
print(timeend-timestart)
violinplot(tk,kmax,"Network summary of a generated graph (graphon)","alpha="+str(alpha)+", nb_vx="+str(len(G.vs))+", sub_size="+str(size)+", func="+func1)
        

