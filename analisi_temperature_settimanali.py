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
def deviazione_standard(varianza):
    return varianza ** 0.5
def giornata_calda(lun,mer,mer,gio,ven):
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
        giorno_più_caldo="Mercoledi"
        media_più_alta= ven
    if sab>media_più_alta:
        giorno_più_caldo="Sabato"
        media_più_alta= mer
    if dom>media_più_alta:
        giorno_più_caldo="Domenica"
        media_più_alta= dom
    
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
media_lun=media_giornalira(lunedi)
media_mar=media_giornalira(martedi)
media_mer=media_giornalira(mercoledi)
media_gio=media_giornalira(giovedi)
media_ven=media_giornalira(venerdi)
media_sab=media_giornalira(sabato)
media_dom=media_giornalira(domenica)
# variazioni di temperatura 
varianza_lun=varianza_temperature(media_lun,lunedi)
varianza_mar=varianza_temperature(media_mar,martedi)
varianza_mer=varianza_temperature(media_mer,mercoledi)
varianza_gio=varianza_temperature(media_gio,giovedi)
varianza_ven=varianza_temperature(media_ven,venerdi)
varianza_sab=varianza_temperature(media_sab,sabato)
varianza_dom=varianza_temperature(media_dom,domenica)
# la devizione standard 
dev_std_lun=deviazione_standard(varianza_lun)
dev_std_mar=deviazione_standard(varianza_mar)
dev_std_mer=deviazione_standard(varianza_mer)
dev_std_gio=deviazione_standard(varianza_gio)
dev_std_ver=deviazione_standard(varianza_ven)
dev_std_sab=deviazione_standard(varianza_sab)
dev_std_dom=deviazione_standard(varianza_dom)
# giornata più calda
