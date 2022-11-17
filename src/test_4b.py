import scipy.io
import numpy as np
from parallel import *
from multiprocessing import Pool, Manager, Process, cpu_count
import multiprocessing.managers
import subprocess
from functools import partial
import time

num_cores=cpu_count()
class MyManager(multiprocessing.managers.BaseManager):
    pass
MyManager.register('np_zeros', np.zeros, multiprocessing.managers.ArrayProxy)

def random_sampling_par(G,slist,kmax,alpha):
    #pool=Pool(4)
    #Gur=pool.map(random_sampling_one,(zip(np.full(len(slist),G),slist)))
    #with Manager() as manager:
        #Gur=manager.np.zeros(len(slist))
        #p0=Process(random_sampling_one_par,zip(np.full(len(slist),G),slist))
    R=math.ceil((1/2/alpha*phi_inv(1-alpha/(2*(kmax-1))))**2)
    m=MyManager()
    m.start()
    Gur=m.np_zeros((R,slist[0],slist[0]))
    pool=Pool(num_cores)
    run_list=[]
    for i in range(R):
        run_list.append([G,slist[i],i])
    func=partial(random_sampling_one_par,Gur)
    res=pool.map(func,run_list)
    return Gur


def network_summary_par(G,slist,kmax,alpha):
    R=math.ceil((1/2/alpha*phi_inv(1-alpha/(2*(kmax-1))))**2)
    Gur=random_sampling_par(G,slist,kmax,alpha)
    m=MyManager()
    m.start()
    tk=m.np_zeros((kmax-1,R))
    arg=[]
    for i in range(R):#have to use numpy functions or parallelize for big number of vertices but time taken negligible to the main process for now, allocation problem?
        arg.append([Gur[i],kmax,i])
    pool=Pool(num_cores)
    func=partial(network_summary_sub,tk)
    res=pool.map(func,arg)
    return tk

kmax=7
alpha=0.1
N=10
delta=0.05
R=math.ceil((1/2/alpha*phi_inv(1-alpha/(2*(kmax-1))))**2)
size=1000
slist=np.full(R,size)

mat2= scipy.io.mmread("../data/power.mtx")
M=mat2.toarray()

for i in range(len(M)):
    for j in range(len(M)):
        if M[i,j]>0:#not multiple edges on two vertices
            M[i,j]=1
        if M[i,j]<0:
            M[i,j]=0
        if M[i,j]!=M[j,i]:#sym
            if max(M[i,j],M[j,i])>0:
                M[i,j]=1
                M[j,i]=1
            else:
                M[i,j]=0
                M[j,i]=0
        if M[i,i]!=0:#no self loops
            M[i,i]=0
G=ig.Graph.Adjacency(M.tolist(), mode='undirected')
#G = ig.Graph.Erdos_Renyi(n=1000, p=0.5, directed=False, loops=False)
if __name__=="__main__":
    timestart=time.time()
    #slist = sample_number(G,kmax,alpha,N,delta)
    #timemid=time.time()
    tk = network_summary_par(G,slist,kmax,alpha)
    tkfin=np.array(tk)
    timeend=time.time()
    print(timeend-timestart)
    violinplot(tkfin,kmax,"Network summary of the network of electrical power grid in western US","alpha="+str(alpha)+", nb_vx="+str(len(M))+", sub_size="+str(size))