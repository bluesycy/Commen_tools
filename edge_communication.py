
def sum_pairwise_multiplication(data, ax=None):
    if ax==None:
        fig,ax=plt.subplots(1,1,figsize=(5,5))
    nr_sites=data.shape[0]
    summed_edge_communication=0
    for i in trange(nr_sites):
        for j in range(nr_sites):
            summed_edge_communication+=data[i]*data[j]
    ax.plot(summed_edge_communication)
    ax.set_xlabel('frames')
    return summed_edge_communication

def sum_neighbor_multiplication(data,neigh_all,ax=None):
    if ax==None:
        fig,ax=plt.subplots(1,1,figsize=(5,5))
    nr_sites=data.shape[0]
    summed_edge_communication=0
    for i in trange(nr_sites):
        for j in neigh_all[i]:
            summed_edge_communication+=data[i]*data[j]
    ax.plot(summed_edge_communication)
    ax.set_xlabel('frames')
    return summed_edge_communication
