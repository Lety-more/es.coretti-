def aggiungi_voto(registro, voto):
    registro.append(voto)
    pass

def media_registro(registro, arrotonda_a=0):
    somma=0
    for voto in registro:
        somma=somma+voto
    media=somma/len(registro)
    media=round(media,1)
    return media
    pass

def solo_sufficenti(registro):
    solo_suff=[]
    for i in range(0,len(registro)):
        if registro[i]>=6:
            solo_suff.append(registro[i])
    return solo_suff
def stampa_esito(registro):
    for element in registro:
        if element>=6:
            print("sufficiente")
        else:
            print("insufficiente – recupera!")

classe = [6, 7, 5, 8]
aggiungi_voto(classe, 9)
print(media_registro(classe, 1))
#media_del_registro=media_registro(arrotonda_a=1,registro=classe) si puo fare anche cosi
sufficenze=solo_sufficenti(classe)
print(sufficenze)
stampa_esito(classe)