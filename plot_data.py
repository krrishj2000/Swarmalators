"""
Created on Sat Jun  4 21:14:44 2022

@author: krish
"""
import matplotlib
import time
#for calculating execution time
from numpy import sin,cos ,arccos,arctan
# required for our model
import numpy as np 
# for all mathematical operators and constants
import matplotlib.pyplot as plt 
# for plotting
from numpy.linalg import norm as norm
# required for our model
from numba import njit,prange
# to automatically convert python code to machine language and increase speed drastically
# to capture snapshots of plots in each time step and convert into an animation
from tqdm import tqdm
# to display progressbar during execution
import matplotlib.colors as col
# to define custom colormap
import matplotlib.animation as anim
# to convert output of celluloid camera into video animation
import time
#for calculating execution time
from numpy import sin,cos ,arccos,arctan,arctan2
# required for our model
import numpy as np 
# for all mathematical operators and constants
import matplotlib.pyplot as plt 
# for plotting
from numpy.linalg import norm as norm
# required for our model
# to display progressbar during execution


def plot_as_dots(x5=None,name=None,show=False):
    if x5 is None:
        print("No data passed.")
        return
    no_of_iterations=len(x5)
    # number of time integration steps

    # v_i=np.random.uniform(low=-2,high=2,size=(2,))
    v_i=0
    # intrinsic velocity each swarmalator has without any interaction
    i=no_of_iterations-1

    fig,ax=plt.subplots(figsize=(10, 10))
    ax.set_aspect(1)
    plt.xlabel(r'$X$',fontsize=20)
    plt.ylabel(r'$Y$',fontsize=20)
    # ax_1.set_title("J="+str(J)+"_ea="+str(e_a)+"_er="+str(e_r)+"_N="+str(N)+"_r="+str(r)+"_iter="+str(no_of_iterations))
    phi=arctan2(x5[i][:,1],x5[i][:,0])

    plt.scatter(x5[i][:,2]-x5[i][:,2].mean(),x5[i][:,3]-x5[i][:,3].mean()
                ,cmap='hsv',c=phi,s=100,edgecolors='black',linewidths=1,vmin=-np.pi,vmax=np.pi)
    # ax.scatter(x5[i][:,3]-x5[i][:,3].mean(),x5[i][:,4]-x5[i][:,4].mean(),x5[i][:,5]-x5[i][:,5].mean(),color="white")
    plt.xlim(-2,2)
    plt.ylim(-2,2)

    cbar=plt.colorbar()
    cbar.ax.set_ylabel(r'$\theta$', rotation=0,fontsize=20)
    plt.savefig(name)
    if show:
        plt.show()
    #plt.show()






