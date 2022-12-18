import scipy.io
import numpy as np
from parallel import *
from multiprocessing import Pool, Manager, Process, cpu_count
import multiprocessing.managers
import subprocess
from functools import partial
import time


# parallel version of Network_summary, tests should be run directly on this file

num_cores = cpu_count()


class MyManager(multiprocessing.managers.BaseManager):
    pass


MyManager.register("np_zeros", np.zeros, multiprocessing.managers.ArrayProxy)


def random_sampling_par(G, slist, kmax, alpha):
    R = math.ceil((1 / 2 / alpha * phi_inv(1 - alpha / (2 * (kmax - 1)))) ** 2)
    m = MyManager()
    m.start()
    Gur = m.np_zeros((R, slist[0], slist[0]))
    pool = Pool(num_cores)
    run_list = []
    for i in range(R):
        run_list.append([G, slist[i], i])
    func = partial(random_sampling_one_par, Gur)
    res = pool.map(func, run_list)
    return Gur


def network_summary_par(G, slist, kmax, alpha):
    R = math.ceil((1 / 2 / alpha * phi_inv(1 - alpha / (2 * (kmax - 1)))) ** 2)
    Gur = random_sampling_par(G, slist, kmax, alpha)
    m = MyManager()
    m.start()
    tk = m.np_zeros((kmax - 1, R))
    arg = []
    for i in range(R):
        arg.append([Gur[i], kmax, i])
    pool = Pool(num_cores)
    func = partial(network_summary_sub, tk)
    res = pool.map(func, arg)
    return tk


kmax = 7
alpha = 0.01
N = 10
delta = 0.05
R = math.ceil((1 / 2 / alpha * phi_inv(1 - alpha / (2 * (kmax - 1)))) ** 2)
size = 100
slist = np.full(R, size)

G = ig.Graph.Erdos_Renyi(n=1000, p=0.5, directed=False, loops=False)

if __name__ == "__main__":
    timestart = time.time()
    tk = network_summary_par(G, slist, kmax, alpha)
    tkfin = np.array(tk)
    timeend = time.time()
    print(timeend - timestart)
    violinplot(
        tkfin,
        kmax,
        "",
        "alpha=" + str(alpha) + ", nb_vx=" + str(len(G.vs)) + ", sub_size=" + str(size),
    )
