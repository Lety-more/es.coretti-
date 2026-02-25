#1. Crea una lista di 10 numeri casuali (usa range per generarli). Calcola la somma con un ciclo.
import random
lista=[]
for i in range(10):
    lista.append(random.randint(0,100))
somma = 0
for i in range(len(lista)):
    somma = somma + lista[i]
print(somma) 

#2. Filtra una lista: data [10, 15, 20, 25, 30], crea una nuova lista solo con numeri > 20 usando un ciclo e if.
num=[10, 15, 20, 25, 30]
Filtra=[]
for i in range(len(num)):
    if num[i] > 20:
        Filtra.append(num[i])
        
print(Filtra)
       
#3. Genera una lista di quadrati da 1 a 10 (es. [1, 4, 9, ...]) con range e append.
quadrati=[]
for i in range(1,11):
    quadrati.append(i*i)
    
print(quadrati)

#4. In una lista di nomi, usa un ciclo per stampare solo quelli che iniziano con "A" (usa if e slicing).
nomi=["Johnny Kavanagh", "Shannon Lynch","Joey Lynch", "Aoife Molloy", "Gibsie Gibson", " Claire Biggs:", "Hughie Biggs", "Lizzie Young", "AJ Lynch"]
for i in range(len(nomi)):
    if nomi[i]=="A":
        print(nomi[i])
        
    "non funziona"    
#Attività pratica (progetto):

#· Livello base: Scrivi un programma che genera una lista di multipli di un numero dato (es. multipli di 5 fino a 50).
multipli = []
for i in range(5,51,5):
    multipli.append(i)

print(multipli)



#· Livello avanzato: Simula un registro di classe: lista di nomi studenti, usa ciclo per assegnare voti casuali (con range) e calcola la media classe
import random
studenti=["Johnny Kavanagh", "Shannon Lynch","Joey Lynch", "Aoife Molloy", "Gibsie Gibson", " Claire Biggs:", "Hughie Biggs", "Lizzie Young", "AJ Lynch"]
voti = []
somma_totale = 0 
for nome in studenti:
    voto = random.randint(1, 10)
    voti.append(voto)
    somma_totale = somma_totale + voto
    print(f"{nome}: {voto}")
media = somma_totale / len(studenti)
print(f"\nSomma totale dei voti: {somma_totale}")
print(f"Media della classe: {media}")








