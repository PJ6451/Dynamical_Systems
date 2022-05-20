import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng

rng = default_rng()

s_s_count    = np.array([0])
s_n_count    = np.array([0])
s_dn_count   = np.array([0])
c_count      = np.array([0])
u_s_count    = np.array([0])
u_n_count    = np.array([0])
u_dn_count   = np.array([0])
s_ln_count   = np.array([0])
u_ln_count   = np.array([0])
saddle_count = np.array([0])
unknown      = np.array([0])

n = 10000000
i = np.array([0])
while i < n:
    i += 1
    a,b,c,d = np.random.uniform(-1.,1.,4)

    tra = a + d
    det = a*d - b*c
    dis = tra**2 - 4*det

    if det < 0:
        saddle_count += 1
    elif det > 0:
        if tra > 0:
            if tra > dis:
                u_n_count += 1
            elif tra < dis:
                u_s_count +=1
            else:
                u_dn_count += 1
        elif tra < 0:
            if tra < dis:
                s_n_count += 1
            elif tra > dis:
                s_s_count +=1
            else:
                s_dn_count += 1
        else:
            c_count += 1
    else:
        if tra > 0:
            u_ln_count += 1
        elif tra < 0:
            s_ln_count += 1
        else:
            unknown += 1


data = {'stable spiral' : s_s_count[0]/n,
    'stable nodes':s_n_count[0]/n,
    'stable degen':s_dn_count[0]/n,
    'center':c_count[0]/n,
    'unstable spiral':u_s_count[0]/n,
    'unstable node':u_n_count[0]/n,
    'unstable degen':u_dn_count[0]/n,
    'stable line':s_ln_count[0]/n,
    'unstable line':u_ln_count[0]/n,
    'saddle':saddle_count[0]/n,
    'unknown':unknown[0]/n}

names = list(data.keys())
values = list(data.values())

plt.bar(names, values)
plt.grid(True)
plt.show()