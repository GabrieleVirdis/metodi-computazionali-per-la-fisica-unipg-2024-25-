# Import moduli
import pandas as pd
import numpy as np
import sys, os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import AutoMinorLocator
from scipy import optimize

# Accesso ai dati
url = 'http://opendata.cern.ch/record/5203/files/Jpsimumu.csv'
dataset = pd.read_csv(url)

# Funzione per il calcolo della massa invariante
def F(E1, p1, E2, p2):
    return np.sqrt((E1 + E2) ** 2 - ((p1[0] + p2[0]) ** 2 + (p1[1] + p2[1]) ** 2 + (p1[2] + p2[2]) ** 2))

# Calcolo massa
E1 = dataset['E1']
E2 = dataset['E2']

px1 = dataset['px1']
py1 = dataset['py1']
pz1 = dataset['pz1']

px2 = dataset['px2']
py2 = dataset['py2']
pz2 = dataset['pz2']

# Calcolo della massa invariante per tutti i dati
mC = F(E1, (px1, py1, pz1), E2, (px2, py2, pz2))

# Istogramma numero 1
fig, ax = plt.subplots(figsize=(12,6))
nn, binss, _ = plt.hist(mC, bins=200)
nbw = binss[1] - binss[0]
plt.xlabel(r'$m_{\mu\mu} [GeV]$', fontsize=16)
plt.ylabel('Eventi')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Configurazione globale dei tick (simile a ROOT)
plt.rc('xtick', direction='in')  # Tick verso l'interno
plt.rc('ytick', direction='in')  # Tick verso l'interno
plt.rc('xtick.major', size=10, width=1.2)
plt.rc('xtick.minor', size=5, width=0.8)
plt.rc('ytick.major', size=10, width=1.2)
plt.rc('ytick.minor', size=5, width=0.8)

# Applicazione dei minor ticks e formattazione per i sottogruppi
ax.tick_params(axis="both", which="major", direction="in", length=10, width=1.2)
ax.tick_params(axis="both", which="minor", direction="in", length=5, width=0.8)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))  # 5 minor tick tra i major tick
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.1f}"))

# Istogramma ristretto (intervallo [2.75, 3.75])
ins_ax = ax.inset_axes([.1, .60, .22, .25])  # [x, y, width, height] w.r.t. ax
n, bins, _ = ins_ax.hist(mC, bins=200, color='green', range=(2.8, 3.5))
ins_ax.set_xlabel(r"$m_{\mu \mu} \in [2.8 { , } 3.2][GeV]$ ", fontsize=8)
ins_ax.set_title('Istogramma + focus su massimo', fontsize=8)
ins_ax.set_ylabel('Eventi', fontsize=8)

# Configurazione dei ticks per l'Inset Axes
ins_ax.tick_params(axis="both", which="major", direction="in", length=8, width=1.2)
ins_ax.tick_params(axis="both", which="minor", direction="in", length=4, width=0.8)
ins_ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ins_ax.yaxis.set_minor_locator(AutoMinorLocator(5))

# Funzione di Gauss (con polinomio di primo grado)
def f_g1(x, A, m, s, p1, p0):
    return A * np.exp(-((x - m) ** 2) / (2 * s ** 2)) + p1 * x + p0

# Funzione di doppia Gaussiana
def f_g2(x, m, A1, A2, s1, s2, p0, p1):
    return A1 * np.exp(-((x - m) ** 2) / (2 * s1 ** 2)) + p1 * x + p0 + A2 * np.exp(-((x - m) ** 2) / (2 * s2 ** 2))

# Centro bin
bin_centro = (bins[:-1] + bins[1:]) / 2

# Fit per trovare i parametri
xdata = bin_centro
ydata = n
pstart1 = np.array([1, 1, 1, 1, 1])
pstart2 = np.array([1, 1, 1, 1, 1, 1, 1])
params, params_covariance = optimize.curve_fit(f_g1, xdata, ydata, sigma=np.sqrt(ydata), p0=[pstart1])
paramse, paramse_covariance = optimize.curve_fit(f_g2, xdata, ydata, sigma=np.sqrt(ydata), p0=[pstart2])

# Stampa parametri dei fit
print('--------------------------------------------')
print('parametri Gauss 1:', params)
print('errori Gauss 1:', params_covariance)
print('parametri Gauss 2:', paramse)
print('errori Gauss 2', paramse_covariance)
print('---------------------------------------------')

# Grafico 1 totale
y_fit = f_g1(bin_centro, *params)
y_fit1 = f_g2(bin_centro, *paramse)
fig, ax = plt.subplots(3, 1, figsize=(9, 9), gridspec_kw={'height_ratios': [3, 1, 1]}, sharex=True)
fig.subplots_adjust(hspace=0)

# Grafico subplot 0 (dati e funzione di fit)
ax[0].errorbar(xdata, ydata, yerr=np.sqrt(ydata), fmt='.', color='gold', alpha=0.7)
ax[0].plot(xdata, y_fit1, color='darkorange', label=r'Fit  $\sigma_y$')
ax[0].set_ylabel('Eventi Misurati', fontsize=16)
ax[0].tick_params(axis="y", labelsize=14)
ax[0].legend(fontsize=14, frameon=False)

# Grafico subplot 1 (scarto tra dati e fit)
yerr = np.sqrt(ydata)
ax[1].errorbar(xdata, ydata - y_fit, yerr=np.sqrt(ydata), fmt='.')
ax[1].axhline(y=0, color='darkorange')
ax[1].set_ylabel('Data-Fit')
ax[1].set_ylim(-45, 45)
ax[1].set_yticks(np.arange(-25, 26, 25))
ax[1].grid(True, axis='y')

# Grafico subplot 2 (scarto/errore y)
ax[2].errorbar(xdata, (ydata - y_fit) / np.sqrt(ydata), yerr=1, fmt='.')
ax[2].axhline(y=0, color='darkorange')
ax[2].set_ylabel(r'(Data-Fit)/$\sigma$')
ax[2].set_ylim(-4.5, 4.5)
ax[2].set_yticks(np.arange(-2.5, 2.6, 2.5))
ax[2].grid(True, axis='y')
ax[2].set_xlabel(r'$m_{\mu\mu}$ [GeV]')

# Applicazione dei tick su tutti i subplot
for a in ax:
    a.tick_params(axis="both", which="major", direction="in", length=10, width=1.2)
    a.tick_params(axis="both", which="minor", direction="in", length=5, width=0.8)
    a.xaxis.set_minor_locator(AutoMinorLocator(5))
    a.yaxis.set_minor_locator(AutoMinorLocator(5))
    a.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.1f}"))

fig.align_ylabels()
plt.show()

# Calcolo Chi quadrato
# Valore funzine fit ottimizzata in corrispondneza dei tempi dei dati
yfit = f_g1(xdata, *params)
#yfit1 = f_g2(xdata, *paramse)

# chi2
chi2 =  np.sum( (yfit - ydata)**2 /ydata ) 
#chi21 = np.sum( (yfit1 - ydata) ** 2 / ydata )

# gradi di libertà
ndof = len(xdata)-len(params)
#ndof1 = len(xdata) - len(paramse)
print('Chi2 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi2, ndof, chi2/ndof ) )
#print('Chi2_1 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi21, ndof1, chi21/ndof1 ) )
