# es preparazione verifica:  analisi temperature settimanali
import random 
def registro_tempertature(giorno):
    for i in range(0,24):
        giorno.append(random.randint(-3,25))

def media_giornalira(giorno,nome_giorno):
    somma=0
    for i in giorno:
        somma=i+somma
    media=somma/24
    print(f"{nome_giorno} - Media: {media:.2f}°C")
    return media

def varianza_temperature(media,giorno):
    calcolo=0
    varianza=0
    for i in range(0,len(giorno)):
        calcolo=(giorno[i]-media)**2
        varianza=calcolo+varianza
    varianza=varianza/len(giorno)
    return varianza

def deviazione_standard(varianza,nome_giorno):
    risultato = varianza ** 0.5
    print(f"{nome_giorno} - Sbalzo medio di temperatura: {risultato:.2f}°C")
    return risultato

def calcola_moda(giorno,nome_giorno):
    frequenze = {}
    for temp in giorno:
        if temp in frequenze:
            frequenze[temp] += 1
        else:
            frequenze[temp] = 1
    
    # Inizializziamo le variabili per trovare il massimo
    temperatura_moda = giorno[0]
    conteggio_massimo = 0
    
    for temp in frequenze:
        if frequenze[temp] > conteggio_massimo:
            conteggio_massimo = frequenze[temp]
            temperatura_moda = temp
    print(f"{nome_giorno} - Moda: {temperatura_moda}°C (ripetuta {conteggio_massimo} volte)")
    return temperatura_moda, conteggio_massimo

def errore_standard(dev_std):
    # n è il numero di ore (24)
    n = 24
    risultato = dev_std / (n ** 0.5)
    return risultato

def giornata_calda(lun,mar,mer,gio,ven,sab,dom):
    giorno_più_caldo="Lunedi"
    media_più_alta= lun
    if mar>media_più_alta:
        giorno_più_caldo="Martedi"
        media_più_alta= mar
    if mer>media_più_alta:
        giorno_più_caldo="Mercoledi"
        media_più_alta= mer
    if gio>media_più_alta:
        giorno_più_caldo="Giovedi"
        media_più_alta= gio
    if ven>media_più_alta:
        giorno_più_caldo="Venerdi"
        media_più_alta= ven
    if sab>media_più_alta:
        giorno_più_caldo="Sabato"
        media_più_alta= sab
    if dom>media_più_alta:
        giorno_più_caldo="Domenica"
        media_più_alta= dom
    print(f"la giornata più calda e {giorno_più_caldo} con temperatura media di {media_più_alta:.2f}")

def giornata_fredda(lun,mar,mer,gio,ven,sab,dom):
    giorno_più_freddo="Lunedi"
    media_più_bassa= lun
    if mar<media_più_bassa:
        giorno_più_freddo="Martedi"
        media_più_bassa= mar
    if mer<media_più_bassa:
        giorno_più_freddo="Mercoledi"
        media_più_bassa= mer
    if gio<media_più_bassa:
        giorno_più_freddo="Giovedi"
        media_più_bassa= gio
    if ven<media_più_bassa:
        giorno_più_freddo="Venerdi"
        media_più_bassa= ven
    if sab<media_più_bassa:
        giorno_più_freddo="Sabato"
        media_più_bassa= sab
    if dom<media_più_bassa:
        giorno_più_freddo="Domenica"
        media_più_bassa= dom
    print(f"la giornata più calda e {giorno_più_freddo} con temperatura media di {media_più_bassa:.2f}")
lunedi = []
martedi = []
mercoledi = []
giovedi = []
venerdi = []
sabato = []
domenica = []
# inserimento delle temperature nei giorni
registro_tempertature(lunedi)
registro_tempertature(martedi)
registro_tempertature(mercoledi)
registro_tempertature(giovedi)
registro_tempertature(sabato)
registro_tempertature(venerdi)
registro_tempertature(domenica)
# media giornate
media_lun=media_giornalira(lunedi,"Lunedi")
media_mar=media_giornalira(martedi,"Martedi")
media_mer=media_giornalira(mercoledi,"Mercoledi")
media_gio=media_giornalira(giovedi,"Giovedi")
media_ven=media_giornalira(venerdi,"Venerdi")
media_sab=media_giornalira(sabato,"Sabato")
media_dom=media_giornalira(domenica,"Domenica")
# variazioni di temperatura 
varianza_lun=varianza_temperature(media_lun,lunedi)
varianza_mar=varianza_temperature(media_mar,martedi)
varianza_mer=varianza_temperature(media_mer,mercoledi)
varianza_gio=varianza_temperature(media_gio,giovedi)
varianza_ven=varianza_temperature(media_ven,venerdi)
varianza_sab=varianza_temperature(media_sab,sabato)
varianza_dom=varianza_temperature(media_dom,domenica)
# la devizione standard 
dev_std_lun=deviazione_standard(varianza_lun,"Lunedi")
dev_std_mar=deviazione_standard(varianza_mar,"Martedi")
dev_std_mer=deviazione_standard(varianza_mer,"Mercoledi")
dev_std_gio=deviazione_standard(varianza_gio,"Giovedi")
dev_std_ver=deviazione_standard(varianza_ven,"Venerdi")
dev_std_sab=deviazione_standard(varianza_sab,"Sabato")
dev_std_dom=deviazione_standard(varianza_dom,"Domenica")
# calcolo moda
moda_lun=calcola_moda(lunedi,"Lunedi")
moda_mar=calcola_moda(martedi,"Martedi")
moda_mer=calcola_moda(mercoledi,"Mercoledi")
moda_gio=calcola_moda(giovedi,"Giovedi")
moda_ven=calcola_moda(venerdi,"Venerdi")
moda_sab=calcola_moda(sabato,"Sabato")
moda_dom=calcola_moda(domenica,"Domenica")
# errore standar
err_sta_lun=errore_standard(dev_std_lun)
err_sta_mar=errore_standard(dev_std_mar)
err_sta_mer=errore_standard(dev_std_mer)
err_sta_gio=errore_standard(dev_std_gio)
err_sta_ven=errore_standard(dev_std_ver)
err_sta_sab=errore_standard(dev_std_sab)
err_sta_dom=errore_standard(dev_std_dom)
# giornata più calda/fredda
giornata_calda(media_lun,media_mar,media_mer,media_gio,media_ven,media_sab,media_dom)
giornata_fredda(media_lun,media_mar,media_mer,media_gio,media_ven,media_sab,media_dom)
