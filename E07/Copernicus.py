# Import Moduli
import numpy as np
import pandas as pd

from scipy import constants, fft
from scipy import optimize

import matplotlib.pyplot as plt

# Lettura dati
df= pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/copernicus_PG_selected.csv')
print('il dataframe :', df)

# Plot della concentrazione di inquinanti
plt.plot(df['date'], df['mean_co_ug/m3'], color='black', alpha= 0.7, label=r'$co$')
plt.plot(df['date'], df['mean_nh3_ug/m3'],  'o ', color='orange', alpha= 0.7, label=r'$nh3$')
plt.plot(df['date'], df['mean_no2_ug/m3'], 'o', color='green', alpha= 0.7, label=r'$no2$')
plt.plot(df['date'], df['mean_o3_ug/m3'], 'o', color='yellow', alpha= 0.7, label=r'$o3$')
plt.plot(df['date'], df['mean_pm10_ug/m3'], 'o', color='pink', alpha= 0.7, label=r'$pm10$')
plt.plot(df['date'], df['mean_pm2p5_ug/m3'], 'o', color='red', alpha= 0.7, label=r'$pm2p5$')
plt.plot(df['date'], df['mean_so2_ug/m3'], 'o', color='blue', alpha= 0.7, label=r'$so2$')

plt.xlabel(r'$Data$', fontsize=14)
plt.ylabel(r'Concentrazione [ug/m3]', fontsize=14)

plt.legend()

plt.show()

# Trasformata di Fourier della serie temporale
ffts = fft.fft(df['mean_co_ug/m3'].values)
nyquist = 0.5 #
freqs =  nyquist * fft.fftfreq(len(ffts), d=1)

# Grafico dello spettro di potenza rispetto alla frequenza
plt.plot(freqs[:len(ffts)//2], np.absolute(ffts[:len(ffts)//2])**2, color='pink' )
plt.xlabel('Freq. [Hz]')
plt.ylabel(r'$\left| c_k \right|^2$')
plt.yscale('log')
plt.xscale('log')
plt.show()

# Grafico dello spettro di potenza rispetto alla frequenza
plt.plot(1/freqs[1:len(ffts)//2], np.absolute(ffts[1:len(ffts)//2])**2, color='pink' )
plt.xlabel(r'$T [Hz^{-1}]$')
plt.ylabel(r'$\left| c_k \right|^2$')
plt.yscale('log')
plt.xscale('log')
plt.show()

# Grafico filtrato
# Applico maschera per filtrare frequenze meno imporatanti sulla base del PS
fftmask1 = np.absolute(ffts)**2 < 2e7

# deep copy di csun
filtered_ffts1 = ffts.copy()
filtered_ffts1[fftmask1] = 0

# Trasformata FFT inversa con coefficienti filtrati 
filtered_ffts11 = fft.irfft(filtered_ffts1, n=len(df['mean_co_ug/m3']))

# Grafico dati originali e filtrati
plt.subplots(figsize=(11,7))
plt.plot(df['date'], df['mean_co_ug/m3'], color='gold',      label='Dati Originali')
plt.plot(df['date'], filtered_ffts11,     color='limegreen', label='Filtro')

plt.legend(fontsize=13)

plt.xlabel('Data')
plt.ylabel('Concentrazione di Co2')

plt.show()

