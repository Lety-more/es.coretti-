#algoritmo notevole specifico: di ordinamento
from kallax import *
lista=[5,3,8,1,2]
#print(lista[1:]) stampa una lista senza il primo numero
for i in range(0,len(lista)-1):
    #trovo il minimo
    minimo=minimolista(lista)
    #trovo lindice del minimo
    indice_minimo=lista.index(minimo)
    #sambio
    lista[indice_minimo]=lista[i]
    lista[i]=minimo
    
print(lista)
