#data una lista di 10 elementi random interi nell'intervallo -10,+10
#calcolre il numero di elenmenti pari a quelli dispari
#1) calcolare una lista di 10 elementi random
#2) calcolare data una lista alcolare i elementi pare e dispari
import random
def generaLista(lista): #la lista vine passata per riferimento 
    for i in range(0,10):
        n=random.randint(-10,10)
        lista.append(n)
        
def calcolaNumeri(lista):
    pari=0
    dispari=0
    for element in lista:
        if element/2==0:
            pari=pari+1
        else:
            dispari=dispari+1
            
    print(pari)
    print(dispari)
        
        
def generaliata2(lista):
    while contatore>10:
        n1=random.randint(-10,10)
        lista.append(n1)
        contatore=contatore+1
if __name__=="__main__":
    mylist=[]
    generaLista(mylist)
    calcolaNumeri(mylist)
    generaliata2(mylist)
    
    
def generaliata2(lista):
    while contatore>10:
        n1=random.randint(-10,10)
        
        
        
        
#prendere una lista che restirtuisce un disionari di numeri pari  e dipari 
        