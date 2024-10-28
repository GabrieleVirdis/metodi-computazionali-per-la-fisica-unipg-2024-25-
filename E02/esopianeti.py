# Import moduli
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Lettura file
mydf = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv')

# Stampa nome colonne del dataframe
print('Le colonne del datasheet sono:', mydf.columns)
print(mydf)

# Grafico 1: Flusso nel tempo (linea verde)
plt.figure(figsize=(12, 6))
plt.plot(mydf['TIME'], mydf['PDCSAP_FLUX'], color='limegreen')
plt.xlabel('T(BJD-2454833)', fontsize=14)
plt.ylabel('$\\phi(e^{-}/s)$', fontsize=14) 
plt.grid(True)
plt.show()

# Grafico 2: Flusso nel tempo (scatter plot rosso)
plt.figure(figsize=(12, 6))
plt.plot(mydf['TIME'], mydf['PDCSAP_FLUX'], 'o', color='red')  
plt.xlabel('T(BJD-2454833)', fontsize=14)
plt.ylabel('$\\phi(e^{-}/s)$', fontsize=14)  
plt.grid(True)
plt.show()

# Grafico 3: Flusso con barre d'errore
plt.figure(figsize=(12, 6))
plt.errorbar(mydf['TIME'], mydf['PDCSAP_FLUX'], yerr=mydf['PDCSAP_FLUX_ERR'], color='orange') 
plt.xlabel('T(BJD-2454833)', fontsize=14)
plt.ylabel('$\\phi(e^{-}/s)$', fontsize=14)  
plt.grid(True)
plt.savefig('flussoerrore.png')
plt.show()

# Grafico 4: Flusso con barre d'errore in un range limitato di tempo
plt.figure(figsize=(12, 6))
plt.errorbar( mydf.loc[ (mydf['TIME']> 947.9) & (mydf['TIME']< 948.35), 'TIME'],
                 mydf.loc[ (mydf['TIME']> 947.9) & (mydf['TIME']< 948.35), 'PDCSAP_FLUX'],
                 yerr=mydf.loc[ (mydf['TIME']> 947.9) & (mydf['TIME']< 948.35), 'PDCSAP_FLUX_ERR'], color='green') 
plt.xlabel('T(BJD-2454833)', fontsize=14)
plt.ylabel('$\\phi(e^{-}/s)$', fontsize=14) 
plt.grid(True)
plt.show()

# Grafico 5: Flusso con riquadro minimo
fig, ax = plt.subplots(figsize=(12,6))
plt.errorbar(mydf['TIME'], mydf['PDCSAP_FLUX'], yerr=mydf['PDCSAP_FLUX_ERR'], fmt='.', color='cornflowerblue' )
plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(1.012e6, 1.030e6)

# Inset 
ins_ax = ax.inset_axes([.65, .62, .32, .32])  # [x, y, width, height] w.r.t. ax
ins_ax.errorbar(      mydf.loc[ (mydf['TIME']> 947.9) & (mydf['TIME']< 948.35), 'TIME'],
                      mydf.loc[ (mydf['TIME']> 947.9) & (mydf['TIME']< 948.35), 'PDCSAP_FLUX'],
                 yerr=mydf.loc[ (mydf['TIME']> 947.9) & (mydf['TIME']< 948.35), 'PDCSAP_FLUX_ERR'], fmt='.',  color='royalblue')
plt.show()
