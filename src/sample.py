import numpy as np
import math
from summary import *
from scipy.stats import norm

def sample_number(G,kmax,alpha,N,delta):
    """ 
    Automatic selection routine for network subsampling sizes: 
    Creates a set of sizes of subgraphs from the graph G for the final plotting


    Args: 
    - G (igraph.Graph): the initial graph
    - kmax (int): maximum length of cycles to count (between 3 and 9)
    - alpha (float): probability of type II error for one of the values for each tk[r] (between 0 and 1)
    - N (int): the number of subgraph to be sampled from G
    - delta (float): the increment size


    Returns:
    - list: A list of length N of sizes of the subgraphs to be sampled from the initial graph G
    """
    slist=[]
    n=G.vcount()
    smax=n
    R=math.ceil((1/2/alpha*phi_inv(1-alpha/(2*(kmax-1))))**2)
    sstar=min(max(kmax+1,min(math.floor(n/4),3*(kmax+1))),n)/(1+delta)
    Kstar=np.arange(3,kmax+1)
    for i in range(1,math.ceil(np.log(n)/np.log(1+delta))):
        pl=[]
        newK=[]
        sstar=min(round((1+delta)*sstar),n)
        tk=Network_summary(G,[sstar],kmax,alpha)
        for i in range(len(Kstar)):
            k=Kstar[i]
            tkp=np.sum(tk[k-2][:])
            if tkp>0:
                denum=math.sqrt(np.abs(1/(R-1)*np.sum(tk[k-2][:]**2)-1/(R-1)/(R)*(tkp**2)))
                pk=1-norm.cdf(1/R*tkp/denum)
            else:
                pk=1/2
            pl.append(pk)
            if pk<1/2:
                newK.append(k)
        p=max(pl)
        if (p<=alpha/(kmax-1)) or (sstar>=smax):
            if smax==math.floor(0.8*n):
                for i in range(N):
                    if N>1:
                        interval=0.2*sstar/(N-1)
                        slist.append(round(0.9*sstar+i*interval))
                    else:
                        slist.append(round(0.9*sstar))
                break
            sstar=min(max(kmax+1,min(math.floor(n/4),3*(kmax+1))),n)/(1+delta)
            Kstar=newK
            smax=math.floor(0.8*n)
    return slist

