import scipy.io
import igraph as ig
import time
import datetime
from sample import *
from summary import *
import networkx as nx
#Read data files
import matplotlib.pyplot as plt
import numpy as np
import math
import igraph as ig
import scipy.io
from cycle import *
from multiprocessing import Pool, Manager, Process, cpu_count
import multiprocessing.managers
import subprocess
from functools import partial

# num_cores=cpu_count()
# class MyManager(multiprocessing.managers.BaseManager):
#     pass
# MyManager.register('np_zeros', np.zeros, multiprocessing.managers.ArrayProxy)


# def network_summary_sub(tk,listarg):
#     """
#     Builds a list tk of number of occurrences for each scale in several subgrpah of a subgraph G


#     Input:
#     - igraph.Graph object G which is the subgraph
#     - The maximal scale kmax from 2 to the minimum of slist
#     - tk the final list with all the occurrences
#     - r the ID of the subgraph (0=<r<R)


#     Output: a list tk that is an accumulation of the occurrences of the different scales in the explored subgraph
#     """
#     G,s,kmax,r=listarg
#     #G=listarg[0]
#     #kmax=listarg[1]
#     #r=listarg[2]
#     Gur=random_sampling_one(G,s)
#     check=count_case2(Gur)
#     t2=0
#     if check>0:
#         t2=count_case1(Gur)/check
#     tk[0,r]=t2
#     kcycle=network_profile(Gur,kmax)
#     fact=math.factorial(len(Gur))
#     for k in range(2,kmax):
#         nbK=fact/(2*(k+1)*math.factorial(len(Gur)-k-1))
#         tk[k-1,r]=(kcycle[k]/nbK)**(1/(k+1))
#     return

# def network_summary_par(G,slist,kmax,alpha):
#     R=math.ceil((1/2/alpha*phi_inv(1-alpha/(2*(kmax-1))))**2)
#     #Gur=random_sampling_one(G,slist)
#     m=MyManager()
#     m.start()
#     tk=m.np_zeros((kmax-1,R))
#     arg=[]
#     for i in range(R):#have to use numpy functions or parallelize for big number of vertices but time taken negligible to the main process for now, allocation problem?
#         arg.append([G,slist[i],kmax,i])
#     pool=Pool(num_cores)
#     func=partial(network_summary_sub,tk)
#     res=pool.map(func,arg)
#     return tk

# kmax=7
# alpha=0.1
# N=10
# delta=0.05
# size=100
# R=math.ceil((1/2/alpha*phi_inv(1-alpha/(2*(kmax-1))))**2)
# slist=np.full(R,size)

# filestart=time.time()
filestart=time.time()   
G2=nx.read_edgelist("../data/data2.txt")
G = ig.Graph.from_networkx(G2)
# if __name__=="__main__":
#     timestart=time.time()
#     #slist = sample_number(G,kmax,alpha,N,delta)
#     #timemid=time.time()
#     tk = network_summary_par(G,slist,kmax,alpha)
#     tkfin=np.array(tk)
#     timeend=time.time()
#     print(timeend-timestart)
#     violinplot(tkfin,kmax,"Network summary of mouse genes","alpha="+str(alpha)+", nb_vx="+str(len(G.vs))+", sub_size="+str(size)) 
# m=nx.adjacency_matrix(G2)
# M=np.array(m.data)
fileend=time.time()
print(fileend-filestart)
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
print(datetime.datetime.now())

kmax=7
alpha=0.5
delta=0.05
size=10
timestart=time.time()
tk = Network_summary(G,[size],kmax,alpha)
timeend=time.time()
print(timeend-timestart)
print(tk)
#violinplot(tk,kmax,"Network summary of mouse genes","alpha="+str(alpha)+", nb_vx="+str(len(G.vs))+", sub_size="+str(size))
        


