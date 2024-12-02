# Import moduli
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# Equazione differenziale pendolo
def func(r, t, g, l):
    dthdt = r[1]
    dwdt = - ( g / l ) * np.sin( r[0] )
    drdt = [ dthdt , dwdt ]
    return drdt

# Parametri args
g = 9.81 #m/s^2

l= 0.5 # m
l1 = 1 #m
l2 = 0.5 #m

theta_0 = np.radians(45) # gradi
theta_2 = np.radians(60) # gradi
omega_0 = 0

x0 = [theta_0, omega_0]
x2 = [theta_2, omega_0]

# Calcolo thetha
time = np.linspace(0, 10, 50)
xx = integrate.odeint(func, y0=x0 , t=time, args=(g, l))
xx1 = integrate.odeint(func, y0=x0 , t=time, args=(g, l1))
xx2 = integrate.odeint(func, y0=x2 , t=time, args=(g, l2))

# grafico risultati
fig,ax = plt.subplots(figsize=(9,6))

plt.plot(time, xx[:,0], color = 'green', label=r'$t_1 [s]$')
plt.plot(time, xx[:,1], color = 'green', label=r'$\theta_1 [°]$')
plt.plot(time, xx1[:,0], color = 'blue', label=r'$t_2 [s]$')
plt.plot(time, xx1[:,1], color = 'blue', label=r'$ \theta_2 [°]  $')
plt.plot(time, xx2[:,0], color = 'yellow', label=r'$t_3 [s] $')
plt.plot(time, xx2[:,1], color = 'yellow', label=r'$ \theta [°] $')

plt.legend(fontsize=14)
plt.xlabel(r'$t [s]$', fontsize=14)
plt.ylabel(r'$\theta [°]$', fontsize=14)
plt.show()
