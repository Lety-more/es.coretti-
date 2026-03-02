#1. Scrivi una funzione che prova a modificare una stringa (immutabile). Mostra che non cambia fuori.
def modStringa(stringa):
    stringa=stringa+" Even when the world tries to pull us apart."
    print (f"Dentro la funzone: {stringa}")
frase=("You'are my home, shannon")
modStringa(frase)
print (f"fuori dalla funzone: {frase}")


#2. Crea una funzione che modifica una lista aggiungendo un elemento. Mostra il cambiamento esterno.
def modificaLista(lista):
    lista.append(4)
numeri=[1,2,3]
modificaLista(numeri)
print(numeri)


#3. Spiega perché in incrementa num non cambia, ma in aggiungi la lista sì.
"""
I numeri non cambiano perché sono immutabili:
    quando fai x += 1 la funzione crea un valore nuovo, ma non modifica quello originale.
Le liste invece sono mutabili:
    append() cambia direttamente l’oggetto, quindi la modifica si vede anche fuori dalla funzione.
"""


#4. Scrivi una funzione che "resetta" una lista (lista = [] dentro). Funziona? Perché no? (Suggerimento: usa lista.clear()).
def resetta(lista):
    lista = []   # crea una NUOVA lista invece di svuotarla 
def resetta(lista):
    lista.clear()   # invece questa svuota la lista originale

numeri = [1, 2, 3]
resetta(numeri)
print(numeri)  