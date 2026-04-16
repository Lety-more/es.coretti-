from jarvis import *
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
#istogramma
crea_istogramma(lunedi)
