
    # -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 02:53:51 2022

@author: krish
"""
''' WARNING: you might need to install scipy package'''

import os
from os.path import exists
import time
#for calculating execution time
from numpy import sin,cos 
# required for our model
import numpy as np 
# for all mathematical operators and constants
# for plotting
from numpy.linalg import norm
# required for our model
from numba import njit,prange
# to automatically convert python code to machine language and increase speed drastically
from tqdm import tqdm
# to display progressbar during execution


directory=os.getcwd()


def generate_data(J,r,e_a,e_r,N,no_of_iterations,rk4=True,dontmakenew=False,makenew=False):

    name="J="+str('{:.2f}'.format(J))+"_ea="+str('{:.2f}'.format(e_a))+"_er="+str('{:.2f}'.format(e_r))+"_N="+str(N)+"_r="+str('{:.2f}'.format(r))+"_iter="+str(no_of_iterations)+".npy"
    fp_1=directory+r'/2druns/'

    if not os.path.exists(fp_1):
      os.makedirs(fp_1)
      
    fp=fp_1+name
    file_exists = exists(fp)
    if (file_exists or dontmakenew) and not makenew:
      # print("File found. Taking from previous run...")
      x5=np.load(fp)
      return x5 

    # v_i=np.random.uniform(low=-2,high=2,size=(2,))
    v_i=0
    # intrinsic velocity each swarmalator has without any interaction
    h=0.1

    @njit()
    def df(x1=np.array([[[[]]]])):
    # takes a fully packed state vector x1 and calculates its value at next time step
        x_dot=np.zeros((N,2))
        # The change in position vector
        sigma_dot=np.zeros((N,2))
        # The change in phase vector
        x=x1[:,2:4]
        # Unpacking the position vector from the passed over x1 vector
        sigma=x1[:,0:2]
        sigma=np.ascontiguousarray(sigma)
        for i in prange(0,N):
          
          # update[i]=np.mean(np.delete(x,i,axis=0),axis=0)-x[i]
          S_x=np.array([float(0),float(0)])
          # The summation term in the spatial interaction
          N_i=0
          # The number of swarmalators inside vision circle of i'th swarmalator
          S_sigma_1=np.array([float(0),float(0)])
          # The summation term of attractive phase interactions
          S_sigma_2=np.array([float(0),float(0)])
          # The summation term of repulsive phase interactions
                          
          # Now find the value of N_i and define xji vector

              

          for j in prange(0,N):
            if i==j:
              continue
            xji=x[j]-x[i]
            if norm(xji)<=r:
              N_i+=1
            xji=np.array([float(xji[0]),float(xji[1])])
            costerm=float(np.dot(sigma[i],sigma[j]))
           
            sinterm=(sigma[j]-np.dot(sigma[j],sigma[i])*sigma[i])

            S_x+=xji/norm(xji)*(1+J*costerm)-xji/np.power((norm(xji)),2)
            # The spatial interaction summation term

            if norm(xji)<=r:
              S_sigma_1+=sinterm/norm(xji)
            else:
              S_sigma_2+=sinterm/norm(xji)
            # The phase interaction summation term
            

          # Find x_dot_i and sigma_dot_i
          x_dot[i]=v_i+S_x/(N-1)
          if N_i!=0:
            sigma_dot[i]+=(e_a*S_sigma_1)/(N_i) 
          if N_i!=N-1:
            sigma_dot[i]+=(e_r*S_sigma_2)/(N-1-N_i)

        x2=np.zeros((N,4)) 
        # Create a vector to pack x and sigma together
        for j in prange(0,N):
          x2[j,0:2]=sigma_dot[j]
          # Update sigma 
          x2[j,2:4]=x_dot[j]
        # Update x
        return x2 # Return new sigma and x in the packed form

    # RUN this part in colab

    # the time before execution started

    def init_state(n,N):
      l=0
      stop=1
      start=-1
      data=np.zeros((N,3),dtype='float64')
      for i in range(0,n):
        for j in range(0,n):
          for k in range(0,n):
            data[l,0]=(stop-start)*i/n+start+np.random.random()*0.5
            data[l,1]=(stop-start)*j/n+start+np.random.random()*0.5
            data[l,2]=(stop-start)*k/n+start+np.random.random()*0.5
            l+=1
      return data
    
    # x1=init_state(int(N**(1/3)),N)
    # x1=np.array(x1).reshape((N,3))
    x1=np.random.uniform(-1,1,(N,2))
    # Initialise positions randomly inside a square
    # theta=np.random.uniform(low=0,high=np.pi,size=(N,1))
    # Initialise theta component of phase vector sigma to unif. random numbers
    phi=np.random.uniform(low=np.pi,high=-np.pi,size=(N,1))
    # Initialise phi component of phase vector sigma to unif. random numbers

    # Create sigma unit vector from the above theta and phi using spherical coordinates
    sigma=np.zeros((N,2))
    for i in range(N):
        sigma[i,0]=cos(phi[i])
        sigma[i,1]=sin(phi[i])

        
    # Create W matrix

    x=np.zeros((N,4))
    # x is the state vector, where position and state vectors are taken together.
    x[:,0:2]=sigma.reshape((N,2)) # packing phase vector inside state vector
    x[:,2:4]=x1 # packing position vector inside state vector


    x5=[]
    # x5 is the history of all x at each time step
    for i in tqdm(prange(0,no_of_iterations)):

        norm_sigma=norm(sigma,axis=1)
        denominator=np.zeros((N,2))
        denominator[:,0]=norm_sigma
        denominator[:,1]=norm_sigma
        sigma=sigma/denominator
        x[:,0:2]=sigma
        k1=df(x)*h     # RK 4th method
        k2=df(x+k1/2)*h
        k3=df(x+k2/2)*h
        k4=df(x+k3)*h
        x=x+(k1+2*k2+2*k3+k4)/6
        
        
        
        sigma=x[:,0:2]

        x5.append(x)


    np.save(fp,x5)
    return x5
  
# generate_data(1,1,1,1,N=50,no_of_iterations=10,rk4=True,makenew=True)
