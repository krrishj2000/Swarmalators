
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://fontmeme.com/permalink/221123/1675da6272264a65c73dfdebf6962a99.png">
  <source media="(prefers-color-scheme: dark)" srcset="https://fontmeme.com/permalink/221123/90b77e413435030e6786f9344b27cec5.png">
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://fontmeme.com/permalink/221123/1675da6272264a65c73dfdebf6962a99.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/99133819/203033578-172946f4-ab48-4c84-88a2-d4d28169924c.jpg">
  <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/99133819/203036317-de3df0fa-7c4a-4c9d-94a3-8d8eac6b7293.png">
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://user-images.githubusercontent.com/99133819/203033578-172946f4-ab48-4c84-88a2-d4d28169924c.jpg">
</picture>


You can access the online simulation of the same model from [here](https://observablehq.com/d/7cca4d73289b5e1e).

## Just note
1. You need to install the following packages first: 
  * **numba**
  * **tqdm**
  * **scipy**
2. The programs are interdependant, so they should be placed in the same folder.
3. You can run main.py for plotting and animating data, and scan_parameter.py to scan parameters.
4. The files will be named according to their parameters itself, so it is easy for you to find them.
5. Thats it, enjoy!

## Sample plots ##

![J=0 90_ea=0 00_er=0 00_r=0 00](https://user-images.githubusercontent.com/99133819/203034764-3727d75d-0b6f-41a7-bf43-1fdcdd97ab91.svg)

## Sample animations ##


https://user-images.githubusercontent.com/99133819/205567923-c8e0a3ac-bfd6-4592-977c-f0efc77df221.mp4



## Pseudocode for generate_Data.py ##
```python
define generate_data(parameters):
    if data for parameters was already generated:
        return already generated data

    Initialise x to N random numbers in [-2,2]
    Initialise theta to N random numbers in [-pi,pi]
    Pack x and theta together into a variable X
    n=1000  # number of iterations
    h=0.01  # step size for RK-4th order method
    

    
    # perform Rk-4th order integration
    Iterate n times:
        k1=df(X)*h
        k2=df(X+k1/2)*h
        k3=df(X+k2/2)*h
        k4=df(X+k3)*h
        X=X+(k1+2*k2+2*k3+k4)/6 
        append this new X to history variable

return the history variable

# dynamical equations of model
define df(X):
    unpack X into x and theta
    initialise x_dot and sigma_dot to zero
    loop i from 0 to N:
        S_x,S_sigma_a,S_sigma_r=0 # initialise summations to zero
        loop j from 0 to N:
            if i same as j:
                skip this loop
            else:
                S_x=S_x+((1+J cos(thetaij))/|xij| -1/|xij|^2)
                if agent j is inside vision radius of agent i
                    N_i=N_i+1
                    S_sigma_a=S_sigma_a+sin(thetaij)/|xij|
                else:
                    S_sigma_r=S_sigma_r+sin(thetaji)/|xij|
        x_dot[i]=S_x/(N-1)
        sigma_dot[i]=e_a*S_sigma_a/(N_i)+e_r*S_sigma_r/(N-N_i-1)
    
    pack x_dot and sigma_dot into X_dot
    return X_dot
   
   ```


