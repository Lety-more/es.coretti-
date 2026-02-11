#creazione di un dizionario

tom={}

#inzerire un ellemento nel dizionario

tom["primo"]=2
tom["secondo"]=4

#creazione di un secondo dizzionario con inizializazione 

sem={"primo":6,"secondo":8}

#accedere ai elementi del dizionario

tom["primo"]+sem["primo"]

#scorere i elementi di un dizionario
for key,value in tom.items():
    print("la chiave è: " +key)
    print("il valore corrispondente è: " + str(value))
