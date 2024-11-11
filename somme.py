import math
# Funzione per la somma
def somma(n):
    """questa funzione fornisce la somma di n(scelti) numeri naturali"""
    somma=0
    for i in range(1, n+1):
        somma=somma+i
    return somma

# Funzione per la somma(RAD)
def sommarad(m):
    """questa funzione fornisce la somma di Rad(n((scelti) numeri naturali"""
    somma1=0
    for i in range(1, m+1):
        somma1=somma1+i**(1/2)
    return somma1

# Funzione somma e prodotto
def sp(n):
    somma=0
    prodotto=1
    for i in range(1, n+1):
        somma=somma+i
        
    for j in range(1, n+1):    
        prodotto=prodotto*j

        return somma, prodotto

# Sommatoria
def sum(n, alfa=1):
    somma=0
    for i in range(1, n+1):
        somma=somma+i**alfa
    return somma

sc=sp(5)
print(sc)
