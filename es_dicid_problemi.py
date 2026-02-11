import random
def generelista(n):
    list=[]
    for i in range(0,n):
        elemnto=random.randint(0,100)
        list.append(elemento)
    return(lista)
    
def minimoList(lista,n):
    minimo=lista[0]
    for i in lista:
        if lista[i]<minimo:
            minimo=lista[i]
    print(minimo)
    
    
def masimoList(lista,n):
    massimo=lista[0]
    for i in lista:
        if lista[i]>masimo:
            massimo=lista[i]
    print(massimo)
if __name__=="__main__":
    dimenzione=10
    listabella=generelista(dimenzione)
    minimoList=(listabella,dimenzione)
    masimoList=(listabella,dimenzione)