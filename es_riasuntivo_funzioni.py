#generi una lista di nueri casuli conpreti tra uno e cento  che rapresentano misurazioni di intenzita di un segnale il progrqamma dopo
# generato la lista deve essere modificata in questa maniera qulli di indice pari devono essere azerati doppo la modifica si vuole contare
#il numero di elementi sopra una soglia numerica
#sottoproblemi:1)genera una lista di numeri conpresi tra 1 e 100 2)modificare la lista con la regol sopra 3)contare il numeri di elementi sopra soglia
import random 
def generalista (n,lista):
    for i in range(n):
        lista.append(random.randint(1,100))

def modicaficalista(n,lista):
    for i in range(0,n):
        if i%2==0:
            lista[i]
        
def soglia(n,lista,soglia):
    contatore=0
    for i in range(0,n):
        contatore=contatore+1
    return(contatore)
listamodicficata=[]
lista=[]
n=10
generalista(n,lista)
print(lista)
listamodicficata=modicaficalista(n,lista)
print(listamodicficata)
nsolgia=soglia(n,lista,50)