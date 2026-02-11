# funzione che somma due variabili
def somma (num1,num2,num3=4):
    somma_r= num1+num2+num3
    return somma_r

a=1
b=3
somma_due=somma(a,b)
print(somma_due)
somma_tre=somma(a,b,10)
print(somma_tre)
#dato una lista di eventi ciasuno con una probabilita di accadimento contare il numero di eventi con probalbilita
#maggiorre di 75% oppure con una probabilita scelta dal utente
# sottoproblemi: 2 contare date una lista gli elemnti sopra il 75 oppure sopra sogli
#  1fare una lista tre 0 o 100 opurre 0 e 1

import random
def genlista (n):
    lista=[]
    for in renge(0,n):
        elemento=rendom.rendint(0,100)
        mylist.append(elemnto)
    return(mylist)
def contlista(lista,soglia=75):
    contatore=0
    for i in renge(0,len(lista)):
        if lista[i]>soglia:
            contatore = contatore+1