# Import moduli
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Lettura file
mydf = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv')

# Grafico 1: Flusso nel tempo (linea verde)
plt.figure(figsize=(12, 6))
plt.plot(mydf.loc[ (mydf['TIME']>939.3) & (mydf['TIME']<941.5), 'TIME'], mydf.loc[ (mydf['TIME']>939.3) & (mydf['TIME']<941.5), 'PDCSAP_FLUX'], color='limegreen')
plt.xlabel('T(BJD-2454833)', fontsize=14)
plt.ylabel('$\\phi(e^{-}/s)$', fontsize=14)
plt.grid(True)
plt.show()
# Periodo
T=941.5-939.4
# Grafico 2: Flusso nel tempo e periodo
# Grafico 1: Flusso nel tempo (linea verde)
plt.figure(figsize=(12, 6))
plt.plot(mydf['TIME'].loc[-T/2:T/2], mydf['PDCSAP_FLUX'].loc[-T/2, T/2], color='limegreen')
plt.xlabel('T(BJD-2454833)', fontsize=14)
plt.ylabel('$\\phi(e^{-}/s)$', fontsize=14)
plt.grid(True)
plt.show()

