import time
#for calculating execution time
from numpy import sin,cos,arctan2,arccos
# required for our model
import numpy as np 
# for all mathematical operators and constants
import matplotlib.pyplot as plt 
# for plotting
from numpy.linalg import norm
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




def animate_as_dots(x5=None,name=None,show=False):
    no_of_iterations=len(x5)
    N=len(x5[0][:,0])
    fig= plt.figure(figsize=(10,10))
    # Hide grid lines
    ax=plt.axes()



    # Hide axes ticks

    x4=x5
# saving precious data for future use



    def animate(i):
        plt.clf() 
        phi=arctan2(x5[i][:,1],x5[i][:,0])
        plt.scatter(x5[i][:,2]-x5[i][:,2].mean(),x5[i][:,3]-x5[i][:,3].mean()
                ,cmap='hsv',c=phi,s=100,edgecolors='black',linewidths=1,vmin=-np.pi,vmax=np.pi)
        plt.gca().set_aspect('equal')
        cbar=plt.colorbar()
        cbar.ax.set_ylabel(r'$\theta$', rotation=0,fontsize=20)
        plt.xlabel(r'$X$',fontsize=20)
        plt.ylabel(r'$Y$',fontsize=20)
        plt.xlim(-2,2)
        plt.ylim(-2,2)  
        return ax
#     # plt.gray()
    # plt.pause(1)

    plt.ioff()
    # print("Done processing frames")
    animation = anim.FuncAnimation(fig,animate,frames=no_of_iterations,interval=1)
    # print("Done making animation object")
    animation.save(filename=name,fps=60)
    # print("Done saving animation.")
    if show:
        plt.show()
