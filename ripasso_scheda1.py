#1. Crea una lista chiamata numeri con i numeri da 1 a 5. Stampa il terzo elemento (indice 2).
numeri= [1,2,3,4,5]
print(numeri[2])


#2. Modifica il secondo elemento di numeri in 10. Stampa la lista aggiornata.
numeri[1]=10
print(numeri)


#3. Aggiungi il numero 6 alla fine della lista usando append. Stampa la lunghezza della lista.
numeri.append(6)
print(numeri)


#4. Crea una lista mista con 3 stringhe e 2 numeri. Stampa l'ultimo elemento (usa len per calcolarlo).
lista=["ciao","bho","pokemon",10,69]
print(lista[len(lista)-1])