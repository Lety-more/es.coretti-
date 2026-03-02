#1. Scrivi una procedura stampa_pari che prende un numero n e stampa i numeri pari da 0 a n.
def elementiPari(numero):
    for i in range(0,numero+1,2):
        print(i)

elementiPari(5)
#2. Trasforma stampa_pari in funzione che restituisce una lista di pari invece di stamparli.
def listaPari(numero):
    pari=[]
    for i in range(0,numro+1,2):
        pari.append(i)
    return pari
#3. Crea una procedura disegna_rettangolo che stampa un rettangolo di asterischi (altezza, larghezza come parametri).
def disegna_rettangolo(altezza,larghezza):
    for i in range(altezza):
        print("*" * larghezza)
        
disegna_rettangolo(3,4)

#4. Scrivi una funzione fattoriale che calcola e restituisce il fattoriale di n (usa ciclo).
def fattoriale(n):
    tot=1
    for i in range(1,n+1):
        tot=tot*i
    return tot
print(fattoriale(5))
#5. Create una procedura per stampare un menu (es. opzioni di un gioco) e una funzione per calcolare un punteggio. Integratele.
def stampaMenu():
    print("""
   1)tornado di fuoco
   2)mano di luce
   3)passa la palla 
""")
    
def calcolaPunteggio(scelta):
    if scelta==1:
        return 30
    elif scelta == 2:
        return 20
    else:
        return 0

        

