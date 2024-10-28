# Moduli Datetime
import datetime
from datetime import datetime, timedelta

# Intro
print('Questo programma fornisce la tua data di nascita in anni, giorni e secondi!')

# Inserisci la data di nascita
datamia = input('Inserisci la tua data di nascita (gg-mm-aaaa): ')

# Categorizza la data di nascita
datamiaf = datetime.strptime(datamia, "%d-%m-%Y")

# Determina la data attuale
dataora = datetime.now()

# Stampa la data attuale
print('La data attuale è: {:02d}-{:02d}-{:d}'.format(dataora.day, dataora.month, dataora.year))

# Definisci gli anni dalla differenza tra dataora e datamia
age_years = dataora.year - datamiaf.year

# Correggi l'età se la data attuale è prima del compleanno di quest'anno
if dataora.month < datamiaf.month or (dataora.month == datamiaf.month and dataora.day < datamiaf.day):
    age_years -= 1

# Definisci una differenza generica tra le date non categorizzata
datediff = dataora - datamiaf

# Definisci la differenza dei secondi (con funzione apposita)
datediff_sec = datediff.total_seconds()

# Trasforma in int la differenza dei secondi
age_secs = int(datediff_sec)

# Trasforma secondi in ore dividendo per 60*60
age_hours = int(datediff_sec / (60 * 60))

# Stampa dei risultati
print('-------------------------------------------------------')
print('  Data di nascita  {:02d}-{:02d}-{:d}'.format(datamiaf.day, datamiaf.month, datamiaf.year))
print('  Data attuale     {:02d}-{:02d}-{:d}'.format(dataora.day, dataora.month, dataora.year))
print()
print('  Età    [anni]: {:>12d}'.format(age_years))
# Età in ore e in khr (dividi per 1000)
print('  Età     [ore]: {:>12d} - {:>6d} khr'.format(age_hours, int(age_hours/1000)))
# Età in secondi e in Ms (dividi per un milione per i Ms)
print('  Età [secondi]: {:>12d} - {:>6d} Ms'.format(age_secs, int(age_secs/1e6)))
print('-------------------------------------------------------')
