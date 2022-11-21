import matplotlib as mpl
import os
import numpy as np
from generate_J2d import generate_data
from tqdm import tqdm
from multiprocessing import Process,Pool
from time import time
from findclusters import findclusters
import order_2d
from os.path import exists
# import logging;
# logging.disable(logging.WARNING)

'''
    : choice2=0 : J=1.0,R=0.2
    : choice2=1 : J=1.0,R=0.5
    : choice2=2 : J=1.0,R=1.0
    : choice2=3 : J=0.5,R=1.0  
'''  
choice2=0

if choice2==0:
    matrix_length=101
    x_start=0.00
    y_start=0.00
    x_stop=x_start+matrix_length*0.01
    y_stop=y_start+matrix_length*0.01
    location=r"/JR2d/matrix/"
    no_of_iterations=100
    ea = 0.5
    er = -0.5


directory=os.getcwd()


def print_func(d=[0.5,ea,er,0.5,0,0]):
    J =d[0]
    ea=d[1]
    er=d[2]
    r =d[3]
    i =d[4]
    j =d[5]
    name=directory+location+"i="+str(i)+"_j="+str(j)+".npy"
    if exists(name):
        print("Haha. Its in here already!")
        return 0
    
    x5=generate_data(J,r,ea,er,N=50,no_of_iterations=no_of_iterations,rk4=True)
    if x5 is None:
        f=open('R.txt','a')
        f.write('%f,' %r)
        f=open('J.txt','a')
        f.write('%f,' %J)
    else:
        x5=np.swapaxes(x5,1,2)
        V=[]
        for t in range(0,10):
            xdata=x5[t:t+1,2:4,:]#
            pdata=x5[t:t+1,0:2,:]#
            V.append(order_2d.state_test(xdata,pdata,fast=True))
        V=np.mean(V,axis=0)
        np.save(name,V)
    return 0
    



if __name__ == "__main__": 
      

    Js = y_start+np.arange(0,matrix_length)*0.01
    rs = x_start+np.arange(0,matrix_length)*0.02
    # U=np.zeros((len(Js),len(eas)))
    
    # U=np.zeros((len(Js),len(eas)))

    procs = []
    proc  = Process(target=print_func)  # declaring process
    procs.append(proc)
    proc.start()


    d_pack=[]
    i=0
    for J in Js:
        j=0
        for r in rs:
            
            d=[J,ea,er,r,i,j]
            d_pack.append(d)
            j=j+1
        i=i+1

    pool = Pool()
    for _ in tqdm(pool.imap_unordered(print_func,d_pack), total=len(d_pack)):
        pass

    print("Completed all programs")


'''


    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(nrows=1,ncols=1,gridspec_kw={'width_ratios': [1]})



    cmap = plt.get_cmap('viridis',10)
    norm = mpl.colors.Normalize(vmin=0, vmax=2)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    

    im1=ax.imshow(V,origin='lower',extent=[0,1,0,1])
    # ax[0].set_xlim((0,1))
    # ax[0].set_ylim((0,1))
    # ax[1].set_xlim((0,1))
    # ax[1].set_ylim((0,1))
    ax.set_title('Number of clusters',fontsize=25)
    ax.set_ylabel(r'$e_r$',fontsize=20)
    ax.set_xlabel(r'$e_a$',fontsize=20)
    # im2=ax[1].imshow(U,origin='upper',extent=[0,1,0,1])
    # ax[1].set_ylabel('J')
    # ax[1].set_xlabel('ea')
    # ax[1].set_title('Variance of X')

    
    # fig.colorbar(im1)
    fig.colorbar(im1)

    plt.show()
'''

