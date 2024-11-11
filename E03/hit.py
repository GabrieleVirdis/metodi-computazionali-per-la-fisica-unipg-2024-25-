import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import reco

# DATASHEET
file_path0 = "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M0.csv"
file_path1 = "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M1.csv"
file_path2 = "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M2.csv"
file_path3 = "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/classi/hit_times_M3.csv"

# Carica i DataFrame

df0 = pd.read_csv(file_path0)
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)
df3 = pd.read_csv(file_path3)

print('----------------------------------')
print(f'Modulo 1 - Lunghezza: {df0.shape}')
print(f'Modulo 2 - Lunghezza: {df1.shape}')
print(f'Modulo 3 - Lunghezza: {df2.shape}')
print(f'Modulo 4 - Lunghezza: {df3.shape}')
print('------------------------------------')

# Unione dei Dataframe

df_tot = pd.concat([df0, df1, df2, df3], ignore_index=True)

print('Dati combinati - Lunghezza:', df_tot.shape)
print('-------------------------------------')

# Istogramma del primo modulo (df0)

sec = df0['hit_time'] * (10**(-9))  # Converte il tempo in secondi

# Istogramma numero 1
n, bis, p = plt.hist(sec, bins=50, range=(0, 2), color='gold', alpha=0.7)
plt.xlabel('t [s]', fontsize=14)
plt.ylabel('Numero di hit', fontsize=14)
plt.title('Istogramma dei Tempi di Hit per il Modulo 1', fontsize=16)
plt.show()

# Istogramma numero 2

diff_t = np.log(df0['hit_time'])

n, bis, p = plt.hist(diff_t, bins=50, range=(0, 100), color='gold', alpha=0.7)
plt.xlabel(r'$log_{10}{(\Delta_{t})} [ns]$', fontsize=14)
plt.ylabel('Numero di hit', fontsize=14)
plt.title('Istogramma della differenza dei tempi di Hit per il Modulo 1', fontsize=16)
plt.show()

# Istogramma numero 3

# tutti hit
tutti_hit = []

for i in range(len(df_tot)):
    mod_id = df_tot['mod_id'][i]
    det_id = df_tot['det_id'][i]
    hit_time = df_tot['hit_time'][i]
    hit = reco.hit(mod_id, det_id, hit_time)
    tutti_hit.append(hit)

# hit ordinati temporalmente e differenze temporali
tutti_hit.sort()
diff_temp= []
for j in range(1, len(tutti_hit)):
    new_diff=tutti_hit[j]-tutti_hit[j-1]
    diff_temp.append(new_diff)
    
plt.hist(diff_temp, bins=50, range=(0, 50), color='blue', alpha=0.7)
plt.xlabel('Differenza di Tempo [ns]', fontsize=14)
plt.ylabel('Numero di hit', fontsize=14)
plt.title('Differenze di tempo tra Hit Consecutivi di tutti i moduli', fontsize=16)
plt.show()


# Soglia della finestra temporale (in ns)
finestra_temp = 20  # in ns

eventi = []
evento_corrente = [tutti_hit[0]]

for k in range(1, len(tutti_hit)):
    differenza_temp = tutti_hit[k] - tutti_hit[k - 1]
    if differenza_temp <= finestra_temp:
        evento_corrente.append(tutti_hit[k])
    else:
        eventi.append(evento_corrente)
        evento_corrente = [tutti_hit[k]] 

if evento_corrente:
    eventi.append(evento_corrente)
print(f"Numero totale di eventi distinti: {len(eventi)}")

