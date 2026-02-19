lista=[12,11,13,5,6]
print(lista)
#toorder contiene lelemento da ordinare
toorder=lista[1]
if lista[1]<lista[0]:
    lista[1]=lista[0]
    lista[0]=toorder
print(lista)

for i in range (0,2):
    if lista[i]>lista[0]:
        lista[i]=lista[0]
        lista[0]

print(lista)