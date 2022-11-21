import numpy as np
from findclusters import findclusters
def state_test(xData,pData,fast=False):
    '''
    Arguments: xData [3xN] format, pData [3xN] format 
    Returns: [No. of Clusters, Sync, Orient.,Hollowness, K.E.]  
    '''
    # list of properties of state [Nc,]
    prop = [] 
    T,_,N = np.shape(xData)
    # data should be from COM frame
    com=np.mean(xData,axis=2)
    xcData = xData*0
    for i in range(N):
        xcData[:,:,i] = xData[:,:,i]-com
    xData = xcData
    # final snapshot
    t=-1 
    x = xData[t,0,:] 
    y = xData[t,1,:]
    u = pData[t,0,:] 
    v = pData[t,1,:]

   
    # combining data in vector form
    X = np.zeros((2,N))#
    P = np.zeros((2,N))#
    X[0,:] = x ; X[1,:] = y 
    P[0,:] = u ; P[1,:] = v 
    x5 = np.concatenate((X,P),axis=0).transpose()
    # cheak the number of clusters 
    if fast==False:
        Nc,_,_ = findclusters(x5,threshold=10,troubleshoot=False)
    else:
        Nc=1
    prop.append(Nc) 

    # synchronization parameter
    par1 = np.mean(P,axis=1)
    par1= np.linalg.norm(par1)
    prop.append(par1)

    # orientation parameter 
    par2 = 0
    for i in range(0,N):
        par2 = par2 + np.dot(X[:,i],P[:,i])/(np.linalg.norm(X[:,i])*np.linalg.norm(P[:,i]))
    par2 = par2/N
    prop.append(par2)
    
    # Hollowness parameter
    rad = np.linalg.norm(X,axis=0)
    hist=np.histogram(rad,bins=10)
    bins = hist[1]
    Nr = hist[0]
    par3 =np.mean(rad)  # the hollow radius
    prop.append(par3)
    # motion parameter with dt= 0.5
    par4 = 0 
    for i in range(0,T-1):
        vData = (xData[i+1,:,:] -xData[i,:,:])/0.5  
        KE = np.sum((np.linalg.norm(vData,axis=0))**2) # kinetic energy of system
        par4 = par4 + KE
    if T!=1:
        par4 = par4/(T) # averaging for time frames
    prop.append(par4/N)   
    
    # elif Nc > 1:
    #     prop.append(0) #sync
    #     prop.append(0) #orientation
    #     prop.append(0) #hollowness
    #     # motion parameter with dt= 0.5
    #     par4 = 0 
    #     for i in range(0,T-1):
    #         vData = (xData[i+1,:,:] -xData[i,:,:])/0.5  
    #         KE = np.sum((np.linalg.norm(vData,axis=0))**2) # kinetic energy of system
    #         par4 = par4 + KE
    #     par4 = par4/(T-1) # averaging for time frames
    #     prop.append(par4)   
    return prop

# from generate_J import generate_data
# x5=generate_data(J=0.31,r=0.22,e_a=1,e_r=-1,N=200,no_of_iterations=400,rk4=True)
# # V[i,j]=(x@sigma.T).mean()
# # V[i,j]=np.linalg.norm(sigma.mean(axis=0))
# x5=np.swapaxes(x5,1,2)
# xdata=x5[:,3:6,:]
# pdata=x5[:,0:3,:]
# print(state_test(xdata,pdata))