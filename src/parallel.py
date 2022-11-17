import numpy as np
from cycle import *
from summary import *

def random_sampling_one_par(Gur,listarg):
    """Creates a subsample in adjacency matrix from the graph G. The subsampling is
    done uniformly at random without replacement with the size equal to each element of S.


    Input: a igraph.Graph object G, a list of sizes S

    
    Output: A list of adjacency matrices (in np.ndarray) of the graph G
    """
    G,s,r=listarg
    mat=G.get_adjacency()
    amat=np.array(mat.data)
    vx=G.vs
    samp=np.random.choice(np.arange(0,len(vx)),s,False)
    samp=np.sort(samp)
    sampmat=amat[np.ix_(samp,samp)]
    Gur[r]=sampmat
    return

def network_summary_sub(tk,listarg):
    """
    Builds a list tk of number of occurrences for each scale in several subgrpah of a subgraph G


    Input:
    - igraph.Graph object G which is the subgraph
    - The maximal scale kmax from 2 to the minimum of slist
    - tk the final list with all the occurrences
    - r the ID of the subgraph (0=<r<R)


    Output: a list tk that is an accumulation of the occurrences of the different scales in the explored subgraph
    """
    G,kmax,r=listarg
    check=count_case2(G)
    t2=0
    if check>0:
        t2=count_case1(G)/check
    tk[0,r]=t2
    kcycle=network_profile(G,kmax)
    fact=math.factorial(len(G))
    for k in range(2,kmax):
        nbK=fact/(2*(k+1)*math.factorial(len(G)-k-1))
        tk[k-1,r]=(kcycle[k]/nbK)**(1/(k+1))
    return