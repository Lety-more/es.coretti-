#. Definisci una funzione quadrato che prende un numero e restituisce il suo quadrato. Chiamala con 4 e stampa il risultato.
def quadrato(numero):
    numero_quadrato=numero*numero
    return numero_quadrato
num=3
numQuadrato = quadrato(num)
print(numQuadrato)



#2. Crea una funzione stampa_nome che prende un nome e stampa "Benvenuto, [nome]!". Chiamala con il tuo nome.
def stampa_nome(nome):
    print(f"Benvenuta, {nome}!")
    
mio_nome=("letizia")
stampa_nome(mio_nome)


#3. Modifica somma per sommare tre numeri. Chiamala con 1, 2, 3.
def somma(a, b, c):
    Somma3Num=a+b+c
    return Somma3Num
    
num1=1
num2=2
num3=3
sommaNum=somma(num1,num2,num3)
print(sommaNum)

#4. Scrivi una funzione massimo che prende due numeri e restituisce il maggiore (usa if).
def Massimo2Num(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

numero1=4
numero2=8
numeroMassimo=Massimo2Num(numero1,numero2)
print(numeroMassimo)
#5. Create una funzione che calcola l'area di un rettangolo (lunghezza * larghezza). Testatela con valori diversi.
def areaRettangolo(lunghezza,larghezza):
    area=lunghezza * larghezza
    return area
base=5
altezza=7
area_ret=areaRettangolo(base,altezza)
print(area_ret)
