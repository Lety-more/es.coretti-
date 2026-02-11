"""
un laboratorio campiona 10 parti di un liquido e misura in ph
il ph e misurato tra 1 e 5 interoge
infine associa a oggi campione un colore in base al risultato colore (a piacere)
1 generere un lista di numeri compresi tre un e 5
2 generege una seconda lista di colori associando ad ogni volore di ph il colore corretto usando un dizionario
"""
import random

ph_numero=[]
ph_colori=[]

for i in range (0,10):
    numero = random.randint(1,5)
    ph_numero.append(numero)
    
    
    
    
    
mydict={1:"rosso",2:"blu",3:"verde",4:"giallo",5:"nero"}

for i in range (0,10):
     colore=mydict[ph_numero[i]]
     ph_colori.append(colore)

#contere il numero del corcorrente "verde"
