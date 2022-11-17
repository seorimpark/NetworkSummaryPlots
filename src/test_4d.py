import igraph as ig
from summary import *

def triadic_closure(G,N):
    """
    Returns 


    Args:

    - G (igraph.Graph): The initial graph
    - N (int): Number of repetition of the process

    Returns:
    - igraph.Graph: The final graph
    """
    vx=G.vs
    for i in range(N):
        samp=np.random.choice(np.arange(0,len(vx)),3,False)
        a=[(samp[0],samp[1]),(samp[1],samp[2]),(samp[0],samp[2])]
        l=G.get_eids(a,error=False)
        if l.count(-1)==1:
            G.add_edges([a[l.index(-1)]])
            d=np.random.choice(np.arange(0,len(G.get_edgelist())),1)
            G.delete_edges(d)
    return G
kmax=7
alpha=0.05
N=10000
delta=0.05
size=100
n=512
p=0.038
G = ig.Graph.Erdos_Renyi(n=512, p=0.038, directed=False, loops=False)
print(len(G.es))
Gmat=G.get_adjacency()
amat=np.array(Gmat.data)
tri1=network_profile(amat,3)[2]
G2=triadic_closure(G,10000)
print(len(G2.es))
G2mat=G2.get_adjacency()
a2mat=np.array(G2mat.data)
tri2=network_profile(a2mat,3)[2]
tk=Network_summary(G2,[size],kmax,alpha)
violinplot(tk,kmax,"Graph with Triadic closure","alpha="+str(alpha)+", nb_vx="+str(n)+", sub_size="+str(size)+", repeat="+str(N)+", p="+str(p)+", initial tri="+str(tri1)+", final tri="+str(tri2))