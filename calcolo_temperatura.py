#si vuole chreare un programma che legendo da un file di testo contenente una serie di valorei
#misurati di tenperatura calcoli la media, la varianza, la mediana della distribuzione.
#sottoproblemi: 1 legere i file riga per riga e creare un lista
#               2 calcola la media
#               3 calcola la varianza
#               4 calcola la media della distribuzione
def leggifile(patinput):
    tenperatura=[]
    with open(patinput) as f:
        for line in f:
            tenperatura.append(int(line.strip()))
            #elemento=int(ine.strip()
            #tenperatura.append(elemento
    return(tenperatura)

lista=leggifile("temperatura.csv")



media uso for
def media(lista):
    for i in range (0,lan(lista)):
        somma= somma+ lista[i]
    media_c= somma/len(lista)
    print(media_c)
"""
#media uso iteratore 
def media_itereitor(lista):
    somma=0
    for elemment in lista:
        somma= somma+elemnt
    media_c= somma/len(lista)
    print(media_c)
"""
def varianza(media,lista):
    n=lan(lista)
    
lista=leggifile("temperatura.csv") # richiamo la funzione 
media(lista)# richiamo la procedura
#media(lista)
#media(media_itereitor)