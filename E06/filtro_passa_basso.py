# Import moduli
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from scipy import optimize
from scipy import integrate

# array tempi 
time = np.linspace(0, 10, 30)

def vin(t):
    if np.isscalar(t):
        if int(t)%2 == 0:
            return 1
        else:
            return -1
    else:
        v = np.ones(len(time))  
        odd_mask = time.astype(int) %2 != 0
        v[odd_mask] = -1
        return v

# funzione filtro passa basso
def func(x, t, RC):
    return (vin(t) - x)/(RC)


# condizione iniziale
x0 = 0

# Args
ReC1 = 4
ReC2 = 1
ReC3 = 0.25

xx1 = integrate.odeint(func, y0=x0, t=time, args=( ReC1,))
xx2 = integrate.odeint(func, y0=x0, t=time, args=( ReC2,))
xx3 = integrate.odeint(func, y0=x0, t=time, args=( ReC3,))

# Grafico delle soluzioni
fig,ax = plt.subplots(figsize=(9,6))
plt.title('scipy.integrate.odeint ', color='slategray', fontsize=14)
plt.plot(time, xx1, color='blue', label = r'$RC=4 [\Omega F]$')
plt.plot(time, xx2, color='green', label = r'$RC=1 [\Omega F]$' )
plt.plot(time, xx3, color='yellow', label = r'$RC=0.25 [\Omega F]$')
plt.xlabel('$t [s]$', fontsize=14)
plt.ylabel(r'$V_{OUT} [V]$', fontsize=14)
plt.legend(loc='lower right', fontsize=14)
plt.show()

# Dataframe
d = {
    't': time,
    'Vin(t)': vin(time),
    'Vout1(t)': xx1,
    'Vout2(t)': xx2,
    'Vout3(t)': xx3
}

# Creazione del DataFrame
df = pd.DataFrame(data=d)

# Visualizzazione del DataFrame (opzionale)
print(df)

# Salvataggio del DataFrame in formato CSV
df.to_csv('output.csv', index=False)
