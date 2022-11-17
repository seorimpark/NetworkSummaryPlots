import matplotlib.pyplot as plt
import numpy as np
import math
import igraph as ig
from scipy.stats import norm
from cycle import *

def Network_summary(G,slist,kmax,alpha):
    """
    Network summarization routine used in the main text
    Builds a list tk representing the scale of occurrences for each tree/type of cycles for each sampled subgraphs of graph G


    Args:
    - G (igraph.Graph): the initial graph
    - slist (list): the list of chosen sizes of subgraphs (between 1 and number of vertices in G)
    - kmax (int): maximum length of cycles to count (between 3 and 9)
    - alpha (float): probability of type II error for one of the values for each tk[r] (between 0 and 1)


    Returns: 
    - np.ndarray: a list tk of shape (kmax-1,R) that shows the network summary for each samples
    """
    R=math.ceil((1/2/alpha*phi_inv(1-alpha/(2*(kmax-1))))**2)
    tk=np.zeros([kmax-1,R])
    for r in range(R):
        if len(slist)>1:
            size=slist[math.ceil(len(slist)*r/R)-1]
        elif len(slist)==1:
            size=int(slist[0])
        Gur=random_sampling_one(G,size)
        check=count_case2(Gur)
        t2=0
        if check>0:
            t2=count_case1(Gur)/check
        tk[0][r]=t2
        kcycle=network_profile(Gur,kmax)
        fact=math.factorial(len(Gur))
        for k in range(2,kmax):
            nbK=fact/(2*(k+1)*math.factorial(len(Gur)-k-1))
            tk[k-1][r]=(kcycle[k]/nbK)**(1/(k+1))
    return tk

def count_case1(G):
    """Counts the number of cases when we have three nodes, the number of connecting edges is two in a graph G
    
    
    Args: 
    - G (np.ndarray): adjacency matrix of the graph G
    
    
    Returns: 
    - int: number of such cases
    """
    n=0
    for i in range(len(G)):
        degree=np.sum(G[i])
        n+=degree*(degree-1)
    return 1/2*n

def count_case2(G):
    """Counts the number of cases when we have three nodes, the number of connecting edges is one in a graph G
    
    
    Args: 
    - G (np.ndarray): adjacency matrix of the graph G
    
    
    Returns: 
    - int: number of such cases
    """
    n=0
    for i in range(len(G)):
        n+=np.sum(G[i])
    return (len(G)-2)/2*n

def violinplot(tk,kmax,title,notes):
    """Creates a violin plot out of the values of tk retrieved by the function Network_summary
    
    
    Args: 
    -tk (np.ndarray): results from Network_summary of graph G
    -kmax (int): maximum length of cycles that was counted (between 3 and 9)
    -notes (str): text to add as a reference (i.e to show the parameters)
    
    Returns: 
    -matplotlip.pyplot (): A violin plot from the results
    """
    data=tk.T
    fig,ax=plt.subplots()
    vp=ax.violinplot(data,np.arange(2,kmax+1))
    plt.title(title)
    plt.xlabel(notes)
    plt.ylabel("Occurrences")
    plt.show()

def phi_inv(n):
    return norm.ppf(norm.cdf(n))

def random_sampling_one(G,s):
    """Creates a subgraph of size s as a form of an adjacency matrix from the initial graph G. The vertices of the subsample are
    drawn uniformly at random without replacement s times.


    Args:
    - G (igraph.Graph): the initial graph
    - s (int): size of the subsample

    
    Returns:
    - np.ndarray: the adjacency matrix of the subsample
    """
    mat=G.get_adjacency()
    amat=np.array(mat.data)
    vx=G.vs
    samp=np.random.choice(np.arange(0,len(vx)),s,False)
    samp=np.sort(samp)
    sampmat=amat[np.ix_(samp,samp)]
    return sampmat

def random_sampling_adj(mat,s):
    """Creates a subgraph of size s as a form of an adjacency matrix from the initial graph G. The vertices of the subsample are
    drawn uniformly at random without replacement s times.


    Args:
    - G (np.ndarray): the initial graph as adjacency matrix
    - s (int): size of the subsample

    
    Returns:
    - np.ndarray: the adjacency matrix of the subsample
    """
    #amat=np.array(mat.data)
    samp=np.random.choice(np.arange(0,len(mat)),s,False)
    samp=np.sort(samp)
    sampmat=mat[np.ix_(samp,samp)]
    return sampmat
