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
"""
crea_istogramma(lunedi)
crea_istogramma(martedi)
crea_istogramma(mercoledi)
crea_istogramma(giovedi)
crea_istogramma(venerdi)
crea_istogramma(sabato)
crea_istogramma(domenica)
"""
# covarianza lunedi
lun_mar_cov=covarianza(lunedi,martedi)
lun_mer_cov=covarianza(lunedi,mercoledi)
lun_gio_cov=covarianza(lunedi,giovedi)
lun_ven_cov=covarianza(lunedi,venerdi)
lun_sab_cov=covarianza(lunedi,sabato)
lun_dom_cov=covarianza(lunedi,domenica)
# covarianza martedi
mar_mer_cov=covarianza(martedi,mercoledi)
mar_gio_cov=covarianza(martedi,giovedi)
mar_ven_cov=covarianza(martedi,venerdi)
mar_sab_cov=covarianza(martedi,sabato)
mar_dom_cov=covarianza(martedi,domenica)
# covarianza mercoledi
mer_gio_cov=covarianza(mercoledi,giovedi)
mer_ven_cov=covarianza(mercoledi,venerdi)
mer_sab_cov=covarianza(mercoledi,sabato)
mer_dom_cov=covarianza(mercoledi,domenica)
# covarianza giovedi
gio_ven_cov=covarianza(giovedi,venerdi)
gio_sab_cov=covarianza(giovedi,sabato)
gio_dom_cov=covarianza(giovedi,domenica)
# covarianza venerdi
ven_sab_cov=covarianza(venerdi,sabato)
ven_dom_cov=covarianza(venerdi,domenica)
# covarianza sabato
sab_dom_cov=covarianza(sabato,domenica)


# corelazione lunedi
lun_mar_cor=correlazione(lun_mar_cov,dev_std_lun,dev_std_mar,"Lunedi-Martedi")
lun_mer_cor=correlazione(lun_mer_cov,dev_std_lun,dev_std_mer,"Lunedi-Mercoledi")
lun_gio_cor=correlazione(lun_gio_cov,dev_std_lun,dev_std_gio,"Lunedi-Giovedi")
lun_ven_cor=correlazione(lun_ven_cov,dev_std_lun,dev_std_ven,"Lunedi-Venerdi")
lun_sab_cor=correlazione(lun_sab_cov,dev_std_lun,dev_std_sab,"Lunedi-Sabato")
lun_dom_cor=correlazione(lun_dom_cov,dev_std_lun,dev_std_dom,"Lunedi-Domenica")
# corelazione martedi
mar_mer_cor=correlazione(mar_mer_cov,dev_std_mar,dev_std_mer,"Martedi-Mercoledi")
mar_gio_cor=correlazione(mar_gio_cov,dev_std_mar,dev_std_gio,"Martedi-Giovedi")
mar_ven_cor=correlazione(mar_ven_cov,dev_std_mar,dev_std_ven,"Martedi-Venerdi")
mar_sab_cor=correlazione(mar_sab_cov,dev_std_mar,dev_std_sab,"Martedi-Sabato")
mar_dom_cor=correlazione(mar_dom_cov,dev_std_mar,dev_std_dom,"Martedi-Domenica")
# corelazione mercoledi
mer_gio_cor=correlazione(mer_gio_cov,dev_std_mer,dev_std_gio,"Mercoledi-Giovedi")
mer_ven_cor=correlazione(mer_ven_cov,dev_std_mer,dev_std_ven,"Mercoledi-Venerdi")
mer_sab_cor=correlazione(mer_sab_cov,dev_std_mer,dev_std_sab,"Mercoledi-Sabato")
mer_dom_cor=correlazione(mer_dom_cov,dev_std_mer,dev_std_dom,"Mercoledi-Domenica")
# corelazione giovedi
gio_ven_cor=correlazione(gio_ven_cov,dev_std_gio,dev_std_ven,"Giovedi-Venerdi")
gio_sab_cor=correlazione(gio_sab_cov,dev_std_gio,dev_std_sab,"Giovedi-Sabato")
gio_dom_cor=correlazione(gio_dom_cov,dev_std_gio,dev_std_dom,"Giovedi-Domenica")
# corelazione venerdi
ven_sab_cor=correlazione(ven_sab_cov,dev_std_ven,dev_std_sab,"Venerdi-Sabato")
ven_dom_cor=correlazione(ven_sab_cov,dev_std_ven,dev_std_dom,"Venerdi-Domenica")
