# Import dei moduli
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from scipy import integrate

# Funzioni per il calcolo dei potenziali
def V1(x, a):

    return a*x**6

def V2(x, a):

    return a*x**2

def V3(x, a):

    return a*x**4

def V4(x, a):

    return a*np.absolute(x)**(3/2)

# valore parametro della massa
m = 1

# Passo
dx= 0.001

# Array vuoto ampiezza
a = np.empty(0)

# Costante potenziale

d = 1

# Creazione array di integrali
integrali1 = np.empty(0)

integrali2 = np.empty(0)

integrali3 = np.empty(0)

integrali4 = np.empty(0)

# Calcolo integrali
for x0 in np.arange(0.5, 6, 0.1):

    a = np.append(a, x0) # array ampiezza

    xx = np.arange(0, x0, dx) # range di integrazione

    F1 = 1./np.sqrt(V1(x0, d) - V1(xx, d))

    F2 = 1./np.sqrt(V2(x0, d) - V2(xx, d))

    F3 = 1./np.sqrt(V3(x0, d) - V3(xx, d))

    F4 = 1./np.sqrt(V4(x0, d) - V4(xx, d))
    
    integrali_1 = integrate.simpson(F1, dx=0.001)

    integrali_2 = integrate.simpson(F2, dx=0.001)

    integrali_3 = integrate.simpson(F3, dx=0.001)

    integrali_4 = integrate.simpson(F4, dx=0.001)

    integrali1 = np.append(integrali1, np.sqrt(8*m) * integrali_1 )

    integrali2 = np.append(integrali2, np.sqrt(8*m) * integrali_1 )

    integrali3 = np.append(integrali3, np.sqrt(8*m) * integrali_1 )

    integrali4 = np.append(integrali4, np.sqrt(8*m) * integrali_1 )

    
# Grafico V1
plt.plot(a, integrali1, 'o-', color='blue')
plt.xlabel("x0")
plt.ylabel("Periodo T")
plt.title("Periodo dell'oscillatore in funzione di x0")
plt.show()

# Grafico V2
plt.plot(a, integrali2, 'o-', color='blue')
plt.xlabel("x0")
plt.ylabel("Periodo T")
plt.title("Periodo dell'oscillatore in funzione di x0")
plt.show()

# Grafico V3
plt.plot(a, integrali3, 'o-', color='blue')
plt.xlabel("x0")
plt.ylabel("Periodo T")
plt.title("Periodo dell'oscillatore in funzione di x0")
plt.show()

# Grafico V4
plt.plot(a, integrali4, 'o-', color='blue')
plt.xlabel("x0")
plt.ylabel("Periodo T")
plt.title("Periodo dell'oscillatore in funzione di x0")
plt.show()
