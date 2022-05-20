#written by Shashwat Sharan, SDSU

import numpy as np
import matplotlib.pyplot as plt

def func(r, x):
    return r-x**2

def bifunc(func, r_min, r_max, num_pts=1000, ini=0.5, tol=100, col ='blue'):
    R_val = [] #array to store the parameter values
    X_val = [] #array to store the function  values
    R = np.linspace(r_min, r_max, num_pts)
    for r in R: #for all parameter values do the following
        x = ini #initial condition
        for iterations in range(num_pts+1):
            x = func(r, x) #iterating the function
            if iterations > tol: #append if total iterations > tolerance
                R_val.append(r)
                X_val.append(x)
    plt.plot(R_val, X_val, color = col, ls='', marker= '.', markersize=0.04)
    plt.xlim([r_min, r_max])
    plt.show()

#THE PAREMETERS
r_min = 0; r_max = 2; num_pts = 3000; ini = 0.1231; tol = 1000

bifunc(func, r_min, r_max, num_pts, ini, tol, 'black')