# es preparazione verifica:  analisi temperature settimanali
import random 
def registro_tempertature(giorno):
    for i in range(0,24):
        giorno.append(random.randint(-3,25))

def media_giornalira(giorno):
    somma=0
    for i in giorno:
        somma=i+somma
    media=somma/24
    return media
def varianza_temperature(media,giorno):
    calcolo=0
    varianza=0
    for i in range(0,len(giorno)):
        calcolo=(giorno[i]-media)**2
        varianza=calcolo+varianza
    varianza=varianza/len(giorno)
    return varianza
lunedi = []
martedi = []
mercoledi = []
giovedi = []
venerdi = []
sabato = []
domenica = []
registro_tempertature(lunedi)
registro_tempertature(martedi)
registro_tempertature(mercoledi)
registro_tempertature(giovedi)
registro_tempertature(sabato)
registro_tempertature(venerdi)
registro_tempertature(domenica)
media_lun=media_giornalira(lunedi)
media_mar=media_giornalira(martedi)
media_mer=media_giornalira(mercoledi)
media_gio=media_giornalira(giovedi)
media_ven=media_giornalira(venerdi)
media_sab=media_giornalira(sabato)
media_dom=media_giornalira(domenica)
varianza_lun=varianza_temperature(media_lun,lunedi)
varianza_mar=varianza_temperature(media_mar,martedi)
varianza_mer=varianza_temperature(media_mer,mercoledi)
varianza_gio=varianza_temperature(media_gio,giovedi)
varianza_ven=varianza_temperature(media_ven,venerdi)
varianza_sab=varianza_temperature(media_sab,sabato)
varianza_dom=varianza_temperature(media_dom,domenica)