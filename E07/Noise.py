# Import Moduli
import numpy as np
import pandas as pd

from scipy import constants, fft
from scipy import optimize

import matplotlib.pyplot as plt

# Lettura dati
df1 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/data_sample1.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/data_sample2.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/data_sample3.csv')

# Stampa i dati
print('---------------------------------')
print('Primo dataset:' , df1)
print('Secondo dataset:' , df2)
print('Terzo dataset:', df3)
print('----------------------------------')

# Plot dei tre segnali in ingresso
plt.plot(df1['time'], df1['meas'], 'o', color='black', alpha= 0.7, label='White Noise')
plt.plot(df2['time'], df2['meas'], 'o', color='pink', alpha=0.7 , label='Pink Noise')
plt.plot(df3['time'], df3['meas'], 'o', color='red', alpha=0.7 , label='Red Noise')

plt.xlabel(r'$t [s]$', fontsize=14)
plt.ylabel('Ampiezza', fontsize=14)

plt.legend()

plt.show()

# Trasformata di Fourier
ffts1 = fft.fft(df1['meas'].values)
ffts2 = fft.fft(df2['meas'].values)
ffts3 = fft.fft(df3['meas'].values)

# Calcolo delle frequenze
nyquist = 0.5 #(1/2) delle frequenze
freqs1 =  nyquist * fft.fftfreq(len(ffts1), d=1)
freqs2 =  nyquist * fft.fftfreq(len(ffts2), d=1)
freqs3 =  nyquist * fft.fftfreq(len(ffts3), d=1)

# Fit in funzione di 1/f^beta
def f(x, a, beta):
    return a*(1/(x**beta))

pstart = np.array([100, 1])
x1= freqs1[1:len(ffts1)//2]
y1= np.absolute(ffts1[1:len(ffts1)//2])**2 
x2= freqs2[1:len(ffts2)//2]
y2= np.absolute(ffts2[1:len(ffts2)//2])**2 
x3= freqs3[5:len(ffts3)//2]
y3= np.absolute(ffts3[5:len(ffts3)//2])**2 

params1, params1_covariance = optimize.curve_fit(f, x1, y1, p0=pstart)
params2, params2_covariance = optimize.curve_fit(f, x2, y2, p0=pstart)
params3, params3_covariance = optimize.curve_fit(f, x3, y3, p0=pstart)
                              
print('beta: dataset1:', params1 )
print('beta: dataset2:', params2 )
print('beta: dataset3:', params3 )

# Plot fit
ftest1= f(x1, *params1)
ftest2= f(x2, *params2)
ftest3= f(x3, *params3)

# Grafico dello spettro di potenza
plt.plot(freqs1[:len(ffts1)//2], np.absolute(ffts1[:len(ffts1)//2])**2, color='pink', alpha=0.7 , label='White Noise' )
plt.plot(x1, ftest1, color='black', alpha=0.7 , label=r'$White Noise fit \beta=0$')
plt.plot(freqs2[:len(ffts2)//2], np.absolute(ffts2[:len(ffts2)//2])**2, color='red', alpha=0.7 , label='Red Noise')
plt.plot(x2, ftest2, color='pink', alpha=0.7 , label=r'$Pink Noise fit: \beta= 1 $')
plt.plot(freqs3[:len(ffts3)//2], np.absolute(ffts3[:len(ffts3)//2])**2, color='pink', alpha=0.7 , label='Red Noise')
plt.plot(x3, ftest3, color='red', alpha=0.7 , label=r'$Red Noise fit: \beta = 2')
plt.xlabel('Freq. [Hz]')
plt.ylabel(r'$\left| c_k \right|^2$')
plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.show()






