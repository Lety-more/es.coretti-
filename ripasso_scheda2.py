#1. Data la lista colori = ["rosso", "blu", "verde", "giallo", "nero"], estrai i primi due colori con slicing.
lista=["rosso", "blu", "verde", "giallo", "nero"]
print(lista[0:2])


#2. Estrai gli ultimi tre colori.
print(lista[2:5])


#3. Inserisci "bianco" all'indice 1. Stampa la lista.
lista.insert(1,"bianco")
print(lista)


#4. Rimuovi "verde" e stampa la lunghezza della lista aggiornata.
lista.remove("verde")
print(lista)