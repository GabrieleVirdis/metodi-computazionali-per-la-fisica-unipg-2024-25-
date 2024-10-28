# Richiesta numero all'utente per la somma
n=input('inserisci il numero')
# Conversione input stringa in intero
nintero = int(n)
# Ciclo for per la somma
somma=0

for i in range(1, nintero+1):
    somma=somma+i
# Stampi la somma
print('-----------------------------------------------------------')
print('La somma dei primi {:d} numeri naturali è: {:d}'.format(nintero, somma))
print('-----------------------------------------------------------')

