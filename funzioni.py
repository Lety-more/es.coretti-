"""lista1=[1,2,3,4]

somma=0
for element in lista1:
    somma=somma+element
print(somma)

lista2=[2,3,4,5]

somma=0
for element in lista2:
    somma=somma+element
print(somma)
"""
#funzione:pezzo di codice generico che viene eseguito al variare di parametri (la prima lettera minuscola)
#prima la definizione:
def sommalista (lista):
    somma=0#si chiama locale
    for element in lista:
        somma=somma+element
    print(somma)

#e poi la richiami  
lista=[1,2,3,4]
sommalista(lista) #si chiama parmetro

lista2=[1,2,3,5]
sommalista(lista2) #si chiama parmetro
#qusta funzioe si chiama procedura


#es: scrivere una funzione che data una lista che stampia a video il numero degli elementi pari in %

def numpari(lista):
    contatore=0
    for element in lista:
        if element % 2 == 0:
            cotatore=contatore+1
    print(contatore)

numpari(lista)
#non torna da rifare




#es:scrivere una procedura che data una lista e un numero chiamato alfa stampi
#a video il numero dei elementi in una lista piu grandi di alfa

def contamagiorealfa(lista,alfa):
    conatore=0
    for element in lista:
        if element<alfa:
            contatore= contatore+1
    print(contatore)


alfa=4
contamagiorealfa(lista,alfa)

#non torna da coregere