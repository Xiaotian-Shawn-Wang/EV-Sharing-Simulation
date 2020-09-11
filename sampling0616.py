# sampling distance matrix and demand over the horizon
import numpy as np

def distance_s(n_s,l_low,l_high,seed):
    # n_s: number of stations
    # l_low, l_high
    # return: distance[i,j] distance from i to j, evaluated in time steps.
    np.random.seed(seed)
    distance={}
    for i in range(n_s):
        for j in range(n_s):
            if i==j:
                distance[i, j] =0
            else:
                distance[i,j] =np.round(np.random.uniform(l_low,l_high))
    return distance

def demand_s(n_s,n_tau,d_mean,seed):
    # n_s: number of stations
    # n_tau: number of time step
    # d_mean[i,j,k]: mean demand from i to j at step k
    # return: demand_m[i,j,k]: demand from i to j at time step k;
    #         d_period: list of demand appearing time
    #         d_ori: list of demand origin
    #         d_des: list of demand destination
    np.random.seed(seed)
    d_period=[]
    d_ori=[]
    d_des=[]
    demand_m={}
    for k in range(n_tau):
        for i in range(n_s):
            for j in range(n_s):
                if i==j:
                    demand_m[i,j,k] =0
                else:
                    demand_m[i, j, k] = np.random.poisson(d_mean[i, j, k])
                    n = 1
                    while n<=demand_m[i, j, k]:
                        d_period.append(k)
                        d_ori.append(i)
                        d_des.append(j)
                        n=n+1
    return [demand_m,d_period,d_ori,d_des]