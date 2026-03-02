#1. Definisci una funzione potenza che prende base e esponente (default=2). Restituisce base^esponente. Chiamala con 3 (output:9) e con 3,3 (output:27).
def  fun_potenza(base,esponente=2):
    potenza=base ** esponente
    return potenza
base1=3
base2=3.3
potenza_base1=fun_potenza(base1)
print(potenza_base1)
potenza_base2=fun_potenza(base2)
print(potenza_base2)
    


#2. Crea benvenuto con parametri nome (obbligatorio) e eta (default=18). Stampa "Benvenuto [nome], hai [eta] anni.". Chiamala in entrambi i modi.
def benvenuto(nome,eta=18):
    print(f"Benvenuto {nome}, hai {eta} anni.")
    
name=("Johnny")
age=("17")
benvenuto(name,age)
benvenuto(name)

#3. Modifica calcola per avere a default=1. Chiamala senza argomenti.
def calcola(a=1,b=2,c=3):
    return a * b + c
print(calcola(5))
print(calcola(5, 4))
print(calcola()) # Chiamala senza argomenti

#4. Scrivi una funzione media per due numeri, con secondo opzionale=0. Calcola (a + b)/2.
def mediaNum(a,b=0):
    media=(a + b)/2
    return media

num1=10
num2=4
mediaTot=mediaNum(num1)
print(mediaTot)


#5. Simulate un "calcolatore IVA": funzione con prezzo e iva (default=22%). Restituisce prezzo + IVA. Discutete casi d'uso.
def calcolatore_IVA(prezzo,iva=0.22):
    somma=prezzo + iva
    return somma
prezzo=(100)
iva=(0.30)
calcolatore=calcolatore_IVA(prezzo)  #iva in default 
print(calcolatore) 

calcolatore=calcolatore_IVA(prezzo,iva) # non usiamo iva default ma gliela diamo 
print(calcolatore)
