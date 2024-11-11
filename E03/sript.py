import sys,os
sys.path.append('MCF/E03')
import somme
s=somme.somma(5)
sr=somme.sommarad(5)
sp1, sp2=somme.sp(5)
su=somme.sum(5, 2)
print('le somma dei primi 5 numeri naturali:', s)
print('le somma dei primi 5 numeri naturali:', sr)
print('le somma dei primi 5 numeri naturali e prodotto:', sp1)
print('il prodotto dei primi 5 numeri naturali e:', sp2)
print('le sommatoria con alfa esponente:', su)
