from generate_data import generate_data
from plot_data import plot_as_dots
from animate_data import animate_as_dots



x5=generate_data(J=0.9,e_a=0,e_r=-0.1,r=0,N=50,no_of_iterations=10,rk4=True)

# uncomment when needed
# animate_as_dots(x5,name="balaji.mp4",show=True)
plot_as_dots(x5,name="balaji.svg",show=True)
