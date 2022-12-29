# Network summary plots

This is the git repository containing the source code for producing network summary plots out of a generated graph or a given network data. The implementation is coded in python, using the `igraph` library. 

## Structure

### Algorithms 
Three files contain the basic algorithms for the production of the plots:
  - `cycle.py` contains the cycle counting algorithm
  - `summary.py` contains the algorithm 1 of the article (Subsampling, computing the occurrences of trees/cycles for each subgraph, and creating violin plots)
  - `sample.py` contains the algorithm 2 of the article (Retrieving the adequate sizes of the subgraphs to sample)

### Production of plots with generated data
Several files (`bipartite.py`, `graphon.py`, `test_block.py`, `test_erdos.py`, `test_pref_attach.py`, `test_ws.py`) contain the codes to use the algorithms to different kinds of generated graphs. 

### Production of plots with real data
The algorithms can be tested on real data by importing the data file to `realdata.py`. Both mtx files containing the adjacency matrix and txt files containing the list of existing edges can be imported. 

> **Note**  
> If the given dataset is too big, it is possible to use the parallelised version of the algorithm 1 by modifying the code `summary_par.py`

## Reference:

"Topology reveals universal features for network comparison", Maugis, Pierre-André G. and Olhede, Sofia C. and Wolfe, Patrick J., 2017, arXiv, 10.48550/ARXIV.1705.05677, https://arxiv.org/abs/1705.05677
