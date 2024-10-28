# Introduzione
print('Il seguente programma calcola la somma dei primi centro numeri naturali')
# Richiesta numero all'utente per la somma
somma=0
for i in range(100+1):
    somma=somma+i
# Stampi la somma
print('-----------------------------------------------------------')
print('La somma dei primi {:d} numeri naturali è: {:d}'.format(100, somma))
print('-----------------------------------------------------------')
