def massimoLista(lista):
    massimo=lista[0]
    for i in range(0,len(lista)):
        if lista[i]>massimo:
            massimo=lista[i]
            return(massimo)
        
def minimolista(lista):
    minimo=lista[0]
    for i in range(0,len(lista)):
        if lista[i]<minimo:
            minimo=lista[i]
            return(minimo)
