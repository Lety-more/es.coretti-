#scrivere un programma per il calcolo delle radici di 2 grando
import math
def calcoloDelta(a,b,c):
    delta=(b*b)-(4*a*c)
    return(delta)
def controllaDelta(a,b,delta):
    if delta<0:
        print("inpossibile")
    elif delta==0:
        calcoloUnaRadice(a,b)
    else:
        calcoloDueRadici(a,b,delta)
def calcoloUnaRadice(a,b):
    soluzione1=-b/2*a
    print(soluzione1)
    
def calcoloDueRadici(a,b,delta):
    soluzione1=(-b+math.sqrt(delta))/2+a
    print(soluzione1)
    soluzione2=(-b-math.sqrt(delta))/2+a
    print(soluzione2)
if __name__=="__main__":
    a=input("inserisci il coeficente a ")
    a=float(a)
    b=input("inserisci il coeficente b ")
    b=float(b)
    c=input("inserisci il coeficente c ")
    c=float(c)
    delta=calcoloDelta(a,b,c)
    print(delta)
    controllaDelta(a,b,delta)

