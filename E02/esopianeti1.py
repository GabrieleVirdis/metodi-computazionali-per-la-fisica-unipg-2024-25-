import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# lettura
mydf = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/moduli_scientifici/ExoplanetsPars_2024.csv', comment='#')
# Stampi il dataframe
print('Le colonne sono:', mydf.columns)
# Sistema solare
ss_orbper  = np.array( [ 88, 225, 365, 687, 4333, 10759, 30687, 60190])
ss_orbsmax = np.array( [ 0.47, 0.73, 1.02, 1.67, 5.45, 10.07, 20.09, 30.32])
ss_bmasse = np.array( [ 0.06, 0.82, 1.0, 0.11, 317.89,  95.17, 14.56, 17.24, ] )
ss_bmassj = ss_bmasse/317.89
# Scatterplot1: M(T) di giove)
plt.figure(figsize=(12,6))
plt.scatter( ss_orbper, ss_bmassj, color='black', label='Sistema solare')
plt.scatter( mydf['pl_orbper'], mydf['pl_bmassj'], color='royalblue', label='Esopianeti')
plt.xlabel(r'T [giorni]', fontsize=14)
plt.ylabel(r'M [Giove]', fontsize=14)
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=14)
plt.show()
# Scatterplot2: max{R*R}/m_star
rapporto = pow(mydf['pl_orbsmax'], 2)/mydf['st_mass'] 
# grafico di rapporto
plt.figure(figsize=(12,6))
plt.scatter( mydf['pl_orbper'], rapporto , color='blue', label='Sistema solare')
plt.scatter( ss_orbper, ss_bmassj, color='black', label='Esopianeti')
plt.xlabel(r'$m_* [Sole]$', fontsize=14)
plt.ylabel(r'${R^{2}}_{max}/m_* $', fontsize=14)
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=14)
plt.show()
# Scatterplot3: distinzione esopianeti
fig, ax = plt.subplots(figsize=(12,6))
plt.scatter( mydf.loc[mydf['discoverymethod']=='Transit', 'pl_orbper'],
             mydf.loc[mydf['discoverymethod']=='Transit', 'pl_bmassj'], color='green', alpha=0.1, label='Transito')
plt.scatter( mydf.loc[mydf['discoverymethod']=='Radial Velocity', 'pl_orbper'],
             mydf.loc[mydf['discoverymethod']=='Radial Velocity', 'pl_bmassj'], color='blue', alpha=0.1, label='Velocità radiale')
plt.scatter( ss_orbper, ss_bmassj, color='black', label='Sistema solare')
plt.xlabel('Period [days]',         fontsize=16)
plt.ylabel(r'Planet Mass [$m_J$]',  fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=14)
plt.show() 
# Scatterplot4: Istogramma
n, bis, p = plt.hist( mydf.loc[mydf['discoverymethod'] == 'Transit', 'pl_bmassj'] , bins=50, range=(-4, 4), color='gold', alpha=0.3, label='Transito')
n, bis, p = plt.hist( mydf.loc[mydf['discoverymethod'] == 'Radial Velocity', 'pl_bmassj'] , bins=50, range=(-4, 4), color='green', alpha=0.3, label='Velocità radiale' )
plt.ylabel('# pianeti', fontsize=14)
plt.xlabel('M [$m_J$] ', fontsize=14)
plt.legend(fontsize=14)
plt.show()
# Scatterplot 5: logaritmo e istogramma
mydf['pl_bmassj']= np.log(mydf['pl_bmassj'])
n, bis, p = plt.hist( mydf.loc[mydf['discoverymethod'] == 'Transit', 'pl_bmassj'], bins=50, range=(0, 4), color='gold', alpha=0.3, label='Transito')
n, bis, p = plt.hist( mydf.loc[mydf['discoverymethod'] == 'Radial Velocity', 'pl_bmassj'] , bins=50, range=(0, 4), color='green', alpha=0.3, label='Velocità radiale' )
plt.xlabel('M [$m_J$] ', fontsize=14)
plt.ylabel('# pianeti', fontsize=14)
plt.legend(fontsize=14)
plt.show()
