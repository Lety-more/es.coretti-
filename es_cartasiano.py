# es retta/ coeficente angolare
#dato un insieme di 20 punti su un piano cartesiano,
#random compresi nell'intervallo 0,10. Calcolare il
#punto con ascissa massima o il punto con cordinata minima.

import random

x=[]
y=[]
for i in range(0,20):
    x.append(random.randint(0,10))
    y.append(random.randint(0,10))
    
#ascissa massima?
#scorrere la lista delle x, trovare il massimo e salvare l'indice
#visualizzare poi con un print il numero
    
indice_max=0
massimo=x[0]
for i in range(1,20):
    if x[i]>massimo:
        massimo=x[i]
        indice_max=i
print(massimo,y[indice_max])

indice_min=0
minimo=y[0]
for i in range(1,20):
    if y[i]<minimo:
        minimo=y[i]
        indice_min=i
print(x[indice_min],minimo)


punti_cartesiano=[]
for i in range(0,20):
    punto=(random.randint(0,10), random.randint(0,10))
    punti_cartesiano.append(punto)
    
#come accedere alla x del primo punto il primo è la coppia
#print(punti_cartesiano[0][0])
#come accedere alla y del primo punto il secondo è il punto specifico della coppia
#print(punti_cartesiano[0][1])

massimo=punti_cartesiano[0]
for i in range(1,20):
    if punti_cartesiano[i][0]>massimo[0]:
        massimo=punti_cartesiano[i]
print(massimo)

minimo=punti_cartesiano[0]
for i in range(1,20):
    if punti_cartesiano[1][i]<minimo[1]:
        minimo=punti_cartesiano[i]
print(minimo)


#sottoproblemi
#1)m=.....
#.......