#dati quatto numeri g interi generati random creare una tupla che contenga il magiore dei primi due e il minore dei secondi
#sotto problemi: trovare il magiore di due numeri 
#                torvare il minore di due numeri
import random
def magg(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
    
def mino(num3,num4):
    if num3<num4:
        return num3
    else:
        return num4
    
uno=input("inserire il primo numero")
uno=int(uno)
due=input("inserire il secondo numero")
due=int(due)

    
tre=input("inserire il terzo numero")
tre=int(tre)
quatro=input("inserire il quatro numero")
quatro=int(quatro)

risultato1=magg(uno,due)
print(risultato1)

risultato2=mino(tre,quatro)
print(risultato2)

tot=(risultato1,risultato2)
print(tot)