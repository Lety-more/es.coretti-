#scrivere un funzione conta_maggiori che riceve una lista di numeri e una soglia (valore perdefino 0)
#e restitusce quanti numeri sono magiori della soglia
def conta_maggiori (lista,sogli=0):
    contatore=0
    for i in range (0,len(lista)):
        if lista[i] > soglia:
            contatore=contatore+1
            
    return(contatore)

"""def conta_maggiori (lista,sogli=0):
    contatore=0
    for element in list
        if elemnt > soglia
            contatore=contatore+1
            
    return(contatore)
"""

lista=[1,3,5,7,8]
maggiori=conta_maggiori(lista)

mggiore_bho=conta_maggiori(lista,4)