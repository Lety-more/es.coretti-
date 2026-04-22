# es preparazione verifica: analisi statistica temperature settimanali
import random # Importa la libreria per generare numeri casuali
#import matplotlib.pyplot as plt

# Funzione per riempire la lista di un giorno con 24 temperature (una per ora)
def registro_tempertature(giorno):
    for i in range(0, 24): # Esegue il ciclo per 24 volte
        # Genera un numero intero casuale tra -3 e 25 e lo aggiunge alla lista
        giorno.append(random.randint(-3, 25))

def media_giornalira(giorno, nome_giorno):
    """
    questa funzione calcola la media di un distribuzione numerica
    :parms liste: lista contenete un giorno di misurazioni
    :parms: nome del giorno
    """
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
 
def crea_istogramma(dati, num_bins=10, titolo="Istogramma", colore="skyblue"):
    """
    Crea e visualizza un istogramma a partire da una lista o array di numeri.
 
    :param dati: Lista o array di valori numerici
    :param num_bins: Numero di intervalli (bins) dell'istogramma
    :param titolo: Titolo del grafico
    :param colore: Colore delle barre
    """
    plt.figure(figsize=(8, 5))
    plt.hist(dati, bins=num_bins, color=colore, edgecolor="black", alpha=0.7)
    plt.title(titolo)
    plt.xlabel("Valori")
    plt.ylabel("Frequenza")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
 
def covarianza(giorno1,giorno2):
    calcolo=0
    for i in range(0,24):
        calcolo=calcolo+(giorno1[i]-(sum(giorno1) / len(giorno1)))*(giorno2[i]-(sum(giorno2) / len(giorno2)))
    calcolo=calcolo/24
    return calcolo

def correlazione(cov, dev_std1, dev_std2, nome_confronto):
    if dev_std1 * dev_std2 != 0:
        risultato = cov / (dev_std1 * dev_std2)
    else:
        risultato = 0
    print(f"La correlazione di {nome_confronto} è: {risultato:.2f}")
    if risultato > 0:
        print(f"Nel confronto di {nome_confronto}: al crescere della prima cresce anche la seconda")
    elif risultato < 0:
        print(f"Nel confronto di {nome_confronto}: al crescere della prima decresce la seconda")
    else:
        print(f"Nel confronto di {nome_confronto}: non c'è relazione tra le due variabili")
    return risultato
