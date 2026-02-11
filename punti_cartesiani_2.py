#dato un inzieme di 20 piunti su un piano cartesiamo,
#random compresi nell'intervallo 0,10. Calcolare il
#punto con ascissa massima e il punto con ordinata minima

import random

x=[]
y=[]
for i in range(0,20):
    y.append(random.randint(0,10))
    x.append(random.randint(0,10))
#acisa masima e minima
#scorere lascisa delle x e savare lindice
#fare print il numero
"""
ind_mas=0
masimo=x[0]
for i in range(0,20):
    if x[i]>masimo:
        masimo=x[i]
        ind_mas=i
print(masimo,y[ind_mas])

ind_min=0
minimo=y[0]
for i in range(0,20):
    if y[i]<minimo:
        minimo=y[i]
        ind_min=i
print(minimo,y[ind_min])
"""
#masimo e minimo della ascisa e ordinata usando la tupla
punti_cartesiano=[]
for i in range(0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)

massimo=punti_cartesiano[0]
for i in range(1,20):
    if punti_cartesiano[i][0]>massimo[0]:
        massimo=punti_cartesiano[i]
print(massimo)

minimo=punti_cartesiano[0]
for i in range(1,20):
    if punti_cartesiano[i][0]<minimo[0]:
        minimo=punti_cartesiano[i]
print(minimo)


# come accedere alla x del primo numero
#print(punti_cartesiano[0][0])
# come accedere alla y del primo numero
#print(punti_cartesiano[0][1])
