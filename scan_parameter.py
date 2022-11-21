import numpy as np
from generate_data import generate_data
from tqdm import tqdm
from multiprocessing import Process,Pool
from time import time
from animate_data import animate_as_dots
from plot_data import plot_as_dots

def print_func(d=[0.5,0.5,-0.5,5]):
    J=d[0]
    ea=d[1]
    er=d[2]
    r=d[3]
    name_video="J="+str('{:.2f}'.format(J))+"_ea="+str('{:.2f}'.format(ea))+"_er="+str('{:.2f}'.format(er))+"_r="+str('{:.2f}'.format(r))+".mp4"
    name_photo="J="+str('{:.2f}'.format(J))+"_ea="+str('{:.2f}'.format(ea))+"_er="+str('{:.2f}'.format(er))+"_r="+str('{:.2f}'.format(r))+".svg"
    x5=generate_data(J,r,ea,er,N=50,no_of_iterations=20,rk4=True)
    animate_as_dots(x5=x5,name=name_video)
    plot_as_dots(x5=x5,name=name_photo)
    return 0
    

if __name__ == "__main__":  # confirms that the code is under main function

    Js    = [0.6,0.3]
    eas   = [0.5,0.6]
    ers   = [-0.5,-0.3]
    rs    = [5]
    procs = []
    proc  = Process(target=print_func)  # declaring process
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    d_pack=[]
    for J in Js:
        for r in rs:
            for ea in eas:
                for er in ers:
                    d=[J,ea,er,r]
                    d_pack.append(d)
                    

# complete the processes

# Put processes as number of cores in your cpu 
# (leaving it blank, as in Pool() is also fine.)
    pool = Pool(processes=8)
    for _ in tqdm(pool.imap_unordered(print_func,d_pack), total=len(d_pack),ascii='░▒█',colour='Magenta'):
        pass

    print("Completed all programs")
