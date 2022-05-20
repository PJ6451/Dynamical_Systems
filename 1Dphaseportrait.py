#written by Joseph Diaz, SDSU 2022

import numpy as np
import matplotlib.pyplot as plt

def phase_portrait_1D(func, x_fine, x_fixed, filename, ylim=None, tol=1e-6, color='black', stability=None, figsize=(10, 5), ds_label="\\dot{{x}} = f(x)", dyn_var='x'):
    
    fig, ax = plt.subplots(figsize=figsize)
    stab_dict = {'stable':'full',
                 'unstable': 'none',
                 'left_stable':'left',
                 'right_stable':'right',
                 '?':'top'}

    average_points = x_fine[0]*np.ones(shape=(x_fixed.size+2,))
    average_points[-1] = x_fine[-1]
    average_points[1:-1] = x_fixed
    average_points = .5*(average_points[1:] + average_points[:-1])

    # print(ds_label, average_points)

    x_local, y_local = np.meshgrid(average_points, np.array([0]))
    arrows = func(x_local)
    arrows = .5*np.where(np.abs(arrows) > tol, arrows/np.abs(arrows), arrows)

    ax.quiver(x_local, y_local, arrows, y_local, pivot='mid', headwidth=5,
                width=.0025, headaxislength=10, headlength=10)

    ax.plot(x_fine, func(x_fine), color=color, label=f"${ds_label}$")

    if stability is None:
        ax.plot(x_fixed, np.zeros(x_fixed.size), 'ok', ms=12.5, label="Fixed points")
    else:
        for fp, stab in zip(x_fixed, stability):
            ax.plot([fp], [0], marker='o', fillstyle=stab_dict[stab], ms=12.5, 
                      color=color, label=f"$x^* = {fp:.4f}$")
        pass

    ax.axhline(y=0, color='k', lw=.75)
    ax.axvline(x=0, color='k', lw=.75)

    ax.grid(True, which='both')
    ax.set_xlabel(f"${dyn_var}$", size=20)
    ax.set_ylabel(f"$\\dot{{{dyn_var}}}$", size=20)
    if ylim is not None:
        ax.set_ylim(*ylim)
    ax.set_xlim(*x_fine[[0, -1]])
    ax.tick_params(axis='both', labelsize=15)
    ax.legend(fontsize=15, framealpha=1)
    ax.set_title(f"Phase plane of ${ds_label}$", size=25)
    fig.tight_layout()

    fig.savefig(filename, dpi=200)
    plt.close(fig)

def func(x):
    a = 3
    h = (1/4)*(a+1)^2
    return x*(1-x) - h*(x/(a+x))

x_fine = np.linspace(-2,2,100)

a = 3
h = (1/4)*(a+1)^2

x1=(a-1 + np.sqrt((a-1)**2 + 4*(a-h)))/(-2) 
x2=(a-1 - np.sqrt((a-1)**2 + 4*(a-h)))/(-2) 

x_fixed = np.array([0,x1,x2])
#x_fixed = np.array([0])

filename = '2fixedpnts_hpos_apos.jpg'

stability = ['unstable','left_stable']
ylim=[-2,2]
tol=1e-6
color='black'
phase_portrait_1D(func, x_fine, x_fixed, filename, ylim, tol, color ,stability)