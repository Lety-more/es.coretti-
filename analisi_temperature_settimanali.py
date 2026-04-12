# es preparazione verifica: analisi statistica temperature settimanali
import random # Importa la libreria per generare numeri casuali

# Funzione per riempire la lista di un giorno con 24 temperature (una per ora)
def registro_tempertature(giorno):
    for i in range(0, 24): # Esegue il ciclo per 24 volte
        # Genera un numero intero casuale tra -3 e 25 e lo aggiunge alla lista
        giorno.append(random.randint(-3, 25))

# Funzione per calcolare la media aritmetica delle temperature di un giorno
def media_giornalira(giorno, nome_giorno):
    somma = 0 # Inizializza il contenitore per la somma totale
    for i in giorno: # Esamina ogni temperatura registrata nella lista
        somma = i + somma # Aggiunge il valore corrente alla somma totale
    media = somma / 24 # Divide la somma per il numero di ore (24)
    # Stampa il risultato con 2 decimali usando la formattazione .f2
    print(f"{nome_giorno} - Media: {media:.2f}°C")
    return media # Restituisce il valore calcolato per usarlo in altre funzioni

# Funzione per calcolare la varianza (necessaria per calcolare lo sbalzo)
def varianza_temperature(media, giorno):
    calcolo = 0 # Variabile temporanea per il calcolo della differenza
    varianza = 0 # Accumulatore per la somma dei quadrati
    for i in range(0, len(giorno)): # Cicla su tutte le temperature del giorno
        # Calcola la differenza tra la temperatura e la media, elevandola al quadrato
        calcolo = (giorno[i] - media) ** 2
        varianza = calcolo + varianza # Somma il quadrato ottenuto al totale
    # Divide la somma dei quadrati per il numero totale di misurazioni
    varianza = varianza / len(giorno)
    return varianza # Restituisce la varianza (numero tecnico di passaggio)

# Funzione per calcolare lo sbalzo medio reale (Deviazione Standard)
def deviazione_standard(varianza, nome_giorno):
    # Calcola la radice quadrata della varianza per tornare all'unità di misura originale
    risultato = varianza ** 0.5
    # Stampa lo sbalzo medio, che indica quanto variano le temperature in quel giorno
    print(f"{nome_giorno} - Sbalzo medio di temperatura: {risultato:.2f}°C")
    return risultato # Restituisce lo sbalzo per calcoli futuri

# Funzione per trovare la temperatura che si è ripetuta più spesso (Moda)
def calcola_moda(giorno, nome_giorno):
    frequenze = {} # Crea un dizionario per contare quante volte appare ogni numero
    for temp in giorno: # Cicla ogni temperatura nella lista giornaliera
        if temp in frequenze: # Se la temperatura è già presente nel dizionario
            frequenze[temp] += 1 # Aumenta il suo contatore di 1
        else: # Se è la prima volta che incontra questa temperatura
            frequenze[temp] = 1 # Crea la voce nel dizionario e inizia a contare
    
    temperatura_moda = giorno[0] # Variabile per memorizzare la temperatura più frequente
    conteggio_massimo = 0 # Variabile per memorizzare il numero di ripetizioni
    
    for temp in frequenze: # Cicla i risultati salvati nel dizionario
        if frequenze[temp] > conteggio_massimo: # Se trova una temperatura con più ripetizioni
            conteggio_massimo = frequenze[temp] # Aggiorna il record di frequenza
            temperatura_moda = temp # Salva quale temperatura è
    # Stampa la temperatura moda e quante volte è stata registrata
    print(f"{nome_giorno} - Moda: {temperatura_moda}°C (ripetuta {conteggio_massimo} volte)")
    return temperatura_moda, conteggio_massimo # Restituisce entrambi i valori

# Funzione per calcolare l'errore standard (precisione della media)
def errore_standard(dev_std):
    n = 24 # Definisce il numero di campioni (le ore del giorno)
    # L'errore standard si ottiene dividendo lo sbalzo per la radice quadrata di n
    risultato = dev_std / (n ** 0.5)
    return risultato # Restituisce il valore dell'errore calcolato

# Funzione per determinare quale giorno della settimana ha avuto la media più alta
def giornata_calda(lun, mar, mer, gio, ven, sab, dom):
    giorno_più_caldo = "Lunedi" # Imposta Lunedì come valore iniziale di confronto
    media_più_alta = lun # Prende la media di Lunedì come riferimento
    
    if mar > media_più_alta: # Controlla se Martedì è più caldo
        giorno_più_caldo = "Martedi"
        media_più_alta = mar
        
    if mer > media_più_alta: # Controlla se Mercoledì è più caldo
        giorno_più_caldo = "Mercoledi"
        media_più_alta = mer
        
    if gio > media_più_alta: # Controlla se Giovedì è più caldo
        giorno_più_caldo = "Giovedi"
        media_più_alta = gio
        
    if ven > media_più_alta: # Controlla se Venerdì è più caldo
        giorno_più_caldo = "Venerdi"
        media_più_alta = ven
        
    if sab > media_più_alta: # Controlla se Sabato è più caldo
        giorno_più_caldo = "Sabato"
        media_più_alta = sab
        
    if dom > media_più_alta: # Controlla se Domenica è più caldo
        giorno_più_caldo = "Domenica"
        media_più_alta = dom
    # Stampa finale del risultato del confronto settimanale
    print(f"La giornata più calda è {giorno_più_caldo} con media di {media_più_alta:.2f}°C")

# Funzione per determinare quale giorno della settimana ha avuto la media più bassa
def giornata_fredda(lun, mar, mer, gio, ven, sab, dom):
    giorno_più_freddo = "Lunedi" # Imposta Lunedì come valore iniziale di confronto
    media_più_bassa = lun # Prende la media di Lunedì come riferimento
    
    if mar < media_più_bassa: # Controlla se Martedì è più freddo
        giorno_più_freddo = "Martedi"
        media_più_bassa = mar
        
    if mer < media_più_bassa: # Controlla se Mercoledì è più freddo
        giorno_più_freddo = "Mercoledi"
        media_più_bassa = mer
        
    if gio < media_più_bassa: # Controlla se Giovedì è più freddo
        giorno_più_freddo = "Giovedi"
        media_più_bassa = gio
        
    if ven < media_più_bassa: # Controlla se Venerdì è più freddo
        giorno_più_freddo = "Venerdi"
        media_più_bassa = ven
        
    if sab < media_più_bassa: # Controlla se Sabato è più freddo
        giorno_più_freddo = "Sabato"
        media_più_bassa = sab
        
    if dom < media_più_bassa: # Controlla se Domenica è più freddo
        giorno_più_freddo = "Domenica"
        media_più_bassa = dom
    # Stampa finale del risultato del confronto settimanale
    print(f"La giornata più fredda è {giorno_più_freddo} con media di {media_più_bassa:.2f}°C")

# ESECUZIONE DEL PRAGRAMMA

# Creazione delle liste che conterranno le temperature per ogni giorno
lunedi = []
martedi = []
mercoledi = []
giovedi = []
venerdi = []
sabato = []
domenica = []

# Riempimento automatico delle liste con dati casuali
registro_tempertature(lunedi)
registro_tempertature(martedi)
registro_tempertature(mercoledi)
registro_tempertature(giovedi)
registro_tempertature(venerdi)
registro_tempertature(sabato)
registro_tempertature(domenica)

# Calcolo e stampa immediata delle medie giornaliere
media_lun = media_giornalira(lunedi, "Lunedi")
media_mar = media_giornalira(martedi, "Martedi")
media_mer = media_giornalira(mercoledi, "Mercoledi")
media_gio = media_giornalira(giovedi, "Giovedi")
media_ven = media_giornalira(venerdi, "Venerdi")
media_sab = media_giornalira(sabato, "Sabato")
media_dom = media_giornalira(domenica, "Domenica")

# Calcolo della varianza per ogni giorno (necessaria come passaggio tecnico)
varianza_lun = varianza_temperature(media_lun, lunedi)
varianza_mar = varianza_temperature(media_mar, martedi)
varianza_mer = varianza_temperature(media_mer, mercoledi)
varianza_gio = varianza_temperature(media_gio, giovedi)
varianza_ven = varianza_temperature(media_ven, venerdi)
varianza_sab = varianza_temperature(media_sab, sabato)
varianza_dom = varianza_temperature(media_dom, domenica)

# Calcolo e stampa degli sbalzi (Deviazione Standard)
dev_std_lun = deviazione_standard(varianza_lun, "Lunedi")
dev_std_mar = deviazione_standard(varianza_mar, "Martedi")
dev_std_mer = deviazione_standard(varianza_mer, "Mercoledi")
dev_std_gio = deviazione_standard(varianza_gio, "Giovedi")
dev_std_ven = deviazione_standard(varianza_ven, "Venerdi")
dev_std_sab = deviazione_standard(varianza_sab, "Sabato")
dev_std_dom = deviazione_standard(varianza_dom, "Domenica")

# Calcolo e stampa della moda (la temperatura che si ripete di più)
calcola_moda(lunedi, "Lunedi")
calcola_moda(martedi, "Martedi")
calcola_moda(mercoledi, "Mercoledi")
calcola_moda(giovedi, "Giovedi")
calcola_moda(venerdi, "Venerdi")
calcola_moda(sabato, "Sabato")
calcola_moda(domenica, "Domenica")

# Calcolo degli errori standard (salvati in variabili)
err_sta_lun = errore_standard(dev_std_lun)
err_sta_mar = errore_standard(dev_std_mar)
err_sta_mer = errore_standard(dev_std_mer)
err_sta_gio = errore_standard(dev_std_gio)
err_sta_ven = errore_standard(dev_std_ven)
err_sta_sab = errore_standard(dev_std_sab)
err_sta_dom = errore_standard(dev_std_dom)

# Confronto finale per trovare la giornata più calda e la più fredda della settimana
giornata_calda(media_lun, media_mar, media_mer, media_gio, media_ven, media_sab, media_dom)
giornata_fredda(media_lun, media_mar, media_mer, media_gio, media_ven, media_sab, media_dom)

