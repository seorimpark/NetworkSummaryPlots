import igraph as ig
from summary import *


def triadic_closure(G, N):
    """
    Returns


    Args:

    - G (igraph.Graph): The initial graph
    - N (int): Number of repetition of the process

    Returns:
    - igraph.Graph: The final graph
    """
    vx = G.vs
    ind = 0
    for i in range(N):
        samp = np.random.choice(np.arange(0, len(vx)), 3, False)
        e1 = samp[0]
        e2 = samp[1]
        e3 = samp[2]
        p = [(e1, e2), (e2, e3), (e1, e3), (e2, e1), (e3, e2), (e3, e1)]
        l = G.get_eids(p, error=False)
        if l.count(-1) == 2:
            le = []
            ltest = []
            # for i in range(6):
            #     if l[i]!=-1:
            #         le.append(p[i])
            #         ltest.append(i)
            for i in range(6):
                if l[i] == -1:
                    a = p[i]
                else:
                    le.append(p[i])
            print(le)
            print(a)
            G.add_edges([a])
            d = np.random.choice(np.arange(0, len(G.get_edgelist())), 1)
            G.delete_edges(d)
            ind += 1
    print(ind)
    return G


kmax = 7
alpha = 0.01
N = 10000
delta = 0.05
size = 200
n = 512
p = 0.038
G = ig.Graph.Erdos_Renyi(n=n, p=p, directed=False, loops=False)
Gmat = G.get_adjacency()
amat = np.array(Gmat.data)
tri1 = network_profile(amat, 3)[2]
G2 = triadic_closure(G, N)
G2mat = G2.get_adjacency()
a2mat = np.array(G2mat.data)
tri2 = network_profile(a2mat, 3)[2]
tk = Network_summary(G2, [size], kmax, alpha)
violinplot(
    tk,
    kmax,
    "Graph with Triadic closure",
    "alpha="
    + str(alpha)
    + ", nb_vx="
    + str(n)
    + ", sub_size="
    + str(size)
    + ", repeat="
    + str(N)
    + ", p="
    + str(p)
    + ", initial tri="
    + str(tri1)
    + ", final tri="
    + str(tri2),
)
