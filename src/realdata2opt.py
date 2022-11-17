import pandas as pd
import numpy as np
import time
from summary import *
import igraph as ig
#import networkx as nx
kmax=7
R=10

def sample(listedges,samp):
    l=[]
    for a,b in listedges:
        if (a in samp) and (b in samp):
            l.append((a,b))
    return np.array(l)

def random_sample(vxlen,size):
    sampl=np.random.choice(np.arange(0,vxlen),size,False)
    return sampl

def network_summary_sample(mat,kmax):
    tk=np.zeros([kmax-1])
    check=count_case2(mat)
    t2=0
    if check>0:
        t2=count_case1(mat)/check
    tk[0]=t2
    kcycle=network_profile(mat,kmax)
    fact=math.factorial(len(mat))
    for k in range(2,kmax):
        nbK=fact/(2*(k+1)*math.factorial(len(mat)-k-1))
        tk[k-1]=(kcycle[k]/nbK)**(1/(k+1))
    return tk
    
def network_summary_final(totedges,vxlen,size,R):
    tk=np.zeros([kmax-1,R])
    for i in range(R):
        sampl=random_sample(vxlen,size)
        l=sample(totedges,sampl)
        #print(l)
        Gsamp=ig.Graph(l)
        mat=Gsamp.get_adjacency()
        amat=np.array(mat.data)
        tkr=network_summary_sample(amat,kmax)
        tk[:,i]=tkr
    return tk

kmax=7
alpha=0.05
N=10
delta=0.05
size=10
p=0.5
n=300

G=ig.Graph.Erdos_Renyi(n=n, p=p, directed=False, loops=False)
listG=G.get_edgelist()
tk=network_summary_final(listG,n,size,R)
print(tk)
violinplot(tk,kmax,"Network summary of a graph following the Erdős–Rényi model","alpha="+str(alpha)+", nb_vx="+str(n)+", sub_size="+str(size)+", p="+str(p))
        