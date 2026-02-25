#1. Data città = ["Roma", "Milano", "Napoli", "Torino"], usa un ciclo con range(len(città)) per stampare ogni città con il suo indice.
città=["Roma", "Milano", "Napoli", "Torino"]
for i in range(len(città)):
    print(f"indice città {i}: {città[i]}")


#2. Crea una lista di 5 numeri. Usa un ciclo per raddoppiare ciascun numero e stampa la lista modificata.
lista=[1,2,3,4,5]
for i in range(len(lista)):
    lista[i]=lista[i] * 2
print(lista)

#3. In una lista di stringhe, usa un ciclo per aggiungere "!" alla fine di ciascuna (es. "ciao" -> "ciao!").
ciao=["pokemon","inazuma eleven","god of war","chopper"]
for i in range(len(ciao)):
    ciao[i]=ciao[i]+"!"
print(ciao)

#4. Crea una lista vuota, poi usa un ciclo con range(5) per aggiungere numeri da 1 a 5 con append.
vuota=[]
for i in range(5):
    vuota.append(i)
print(vuota)
