# algoritmo notevole specifico: di ordinamento
from kallax import *
lista = [5, 3, 8, 1, 2]

for i in range(0, len(lista) - 1):
    minimo = minimolista(lista[i:])
    indice_minimo = lista[i:].index(minimo) + i
    lista[indice_minimo], lista[i] = lista[i], lista[indice_minimo]

print(lista)
