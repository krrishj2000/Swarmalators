import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os
from tqdm import tqdm
from matplotlib import colors

choice=1
if choice==0:
    title="No. of clusters"
elif choice==1:
    title="Synchronisation parameter"
elif choice==2:
    title="Orientation parameter"
elif choice==3:
    title="Hollowness parameter"
elif choice==4:
    title="Kinetic energy"
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
    y_stop=y_start+matrix_length*0.02
    location=r"/JR2d/matrix/"
    no_of_iterations=400
    ea = 0.5
    er = -0.5
    
directory=os.getcwd()
fp1=directory+location
if not os.path.exists(fp1):
    os.makedirs(fp1)
V=np.zeros((matrix_length,matrix_length))
max=0
for i in tqdm(range(0,matrix_length)):
    for j in range(0,matrix_length):
        name=directory+location+"i="+str(i)+"_j="+str(j)+".npy"
        x=np.load(name)
        # if choice!=0:
        #     if x[0]>1 or x[2]<0.2:
        #         V[i,j]=-13
        #         continue
        V[i,j] =x[choice]
        if max<V[i,j]:
            max=V[i,j]
            #    print("Max:",i,j)
        # print(i,j)

# if choice!=0:
#     V=np.ma.masked_where((V==-13),V)
    
    

import matplotlib
matplotlib.rcParams.update({'font.size': 20})

fig,ax=plt.subplots(nrows=1,ncols=1,gridspec_kw={'width_ratios': [1]},figsize=(10,10))



# cmap = colors.ListedColormap(['navy','lavender','lightskyblue'])
# bounds=[0.5,1.5,2.5,3.5]
# norm = colors.BoundaryNorm(bounds, cmap.N)
# ticks=[1, 2, 3]

cmap = plt.get_cmap('viridis')
norm = mpl.colors.Normalize(vmin=0, vmax=1)
# sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
# sm.set_array([])
bounds=None
ticks=None

im1=ax.imshow(V.T,origin='lower',extent=[x_start,x_stop,y_start,y_stop],cmap=cmap,norm=norm,aspect=0.5)
plt.colorbar(im1, cmap=cmap, norm=norm, boundaries=bounds, ticks=ticks)

# ax[0].set_xlim((0,1))
# ax[0].set_ylim((0,1))
# ax[1].set_xlim((0,1))
# ax[1].set_ylim((0,1))
# ax.set_title(title,fontsize=25)
ax.set_ylabel(r'$r$',fontsize=25)
ax.set_xlabel(r'$J$',fontsize=25)
# im2=ax[1].imshow(U,origin='upper',extent=[0,1,0,1])
# ax[1].set_ylabel('J')
# ax[1].set_xlabel('ea')
# ax[1].set_title('Variance of X')


# fig.colorbar(im1)
# fig.colorbar(im1)


line_x=np.linspace(0,0.505,100)
line_y1=1/(1-line_x)
# line_y2=1/(1+line_x)
plt.plot(line_x,line_y1,linewidth=2,color='red')
# plt.plot(line_x,line_y2,linewidth=2,color='blue')
plt.xlim(0,1)
plt.ylim(0,2)
plt.show()



# import plotly.express as pty
# fig=pty.imshow(V,range_color=[0,1])
# fig.show()

