#1. Scomponi: Funzione per sommare lista, funzione per contare elementi >5. Integra per lista voti.
def somma(lista):
    tot=0
    for i in lista:
        tot=tot+1
    return tot
def contaMaggioreDi5(lista):
    cont=0
    for i in lista:
        if i>5:
            cont=cont+1
    return cont

voti = [4,7,8,5,9]
print (somma(voti))
print (contaMaggioreDi5(voti))
    
#2. Problema: Converti gradi Celsius a Fahrenheit. Crea funzioni per conversione e per stampa risultato.
def converitore(Celsius):
    Fahrenheit=Celsius* 9/5 + 32
    print(f"{Celsius} °C = {Fahrenheit} °F")
converitore(20)


#3. Scomponi un calcolatore BMI: Funzioni per input (altezza, peso), calcolo BMI, classificazione (sottopeso/normale).
def calcola_bmi(peso, altezza):
    return peso / (altezza ** 2)
def classifica_bmi(bmi):
    if bmi < 18.5:
        return "Sottopeso"
    elif bmi < 25:
        return "Normale"
    else:
        return "Sovrappeso"
b = calcola_bmi(60, 1.65)
print(classifica_bmi(b))

#4. Crea un programma per indovinare numero: Funzioni per generare numero random, confrontare guess, gestire tentativi.
import random

def gioca():
    segreto = random.randint(1, 10)

    tentativo = 0
    while tentativo != segreto:
        tentativo = int(input("Indovina un numero da 1 a 10: "))
        if tentativo < segreto:
            print("Troppo basso")
        elif tentativo > segreto:
            print("Troppo alto")

    print("Giusto!")

gioca()