#generi una lista di nueri casuli conpreti tra uno e cento  che rapresentano misurazioni di intenzita di un segnale il progrqamma dopo
# generato la lista deve essere modificata in questa maniera qulli di indice pari devono essere azerati doppo la modifica si vuole contare
#il numero di elementi sopra una soglia numerica
#sottoproblemi:1)genera una lista di numeri conpresi tra 1 e 100 2)modificare la lista con la regol sopra 3)contare il numeri di elementi sopra soglia
import random
from kallax import *
def creaLista(lista):
    nUno=input("Inserire il primo estremo: ")
    nUno=int(nUno)
    nDue=input("Inserire il secondo estremo: ")
    nDue=int(nDue)
    for i in range (0,10):
        if nDue>nUno:
            elemento=random.randint(nUno,nDue)
        else:
            elemento=random.randint(nDue,nUno)
        lista.append(elemento)
        
def media(lista):
    sommaElementi=0
    for elemento in lista:
        sommaElementi = sommaElementi + elemento
    mediaElementi = sommaElementi / len(lista)
    return mediaElementi

def massimoLista(lista):
    massimo=lista[0]
    for i in range(l,len(lista)):
        if lista[i]>massimo:
            massimo=lista[i]
            return(massimo)
        
def calcolaSoglia(lista):
    massimo=massimoLista(lista)
    soglia = massimo - 10
    return soglia

def contaSopraSoglia(lista, soglia):
    contatore = 0
    for elemento in lista:
        if elemento > soglia:
            contatore = contatore + 1
    print(contatore)


if __name__=="__main__":
    listaM = []
    creaLista(listaM)
    mediaValori = media(listaM)
    sogliaValori = calcolaSoglia(listaM)
    print(listaM)
    contaSopraSoglia(listaM, sogliaValori)
    
