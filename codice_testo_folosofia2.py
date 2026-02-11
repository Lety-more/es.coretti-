import string
from collections import Counter

#Parole da escludere
stopwords = ['il', 'la', 'lo', 'i', 'gli', 'le', 'un', 'una', 'uno','di', 'a', 'da', 'in', 'con', 'su', 'per', 'tra', 'fra','e', 'o', 'ma', 'che', 'non', 'più', 'come', 'anche', 'se']

#Lettura del testo dal file
with open("testo_meraviglia.txt", "r", encoding="utf-8") as file:
    testo = file.read()

#Pulizia del testo: minuscole + rimozione punteggiatura
testo_pulito = testo.lower()
for carattere in string.punctuation:
    testo_pulito = testo_pulito.replace(carattere, '')

# Conteggio parole significative
#test_diviso=testo_pulito.split()
parole = [parola for parola in testo_pulito.split() if parola not in stopwords]
conteggio = Counter(parole)

# Estrazione delle 5 parole più frequenti
top_5 = conteggio.most_common(5)

#Stampa dei risultati
print("Le 5 parole più frequenti:")
for parola, frequenza in top_5:
    print(f"- {parola}: {frequenza}")

# Associazioni concettuali
concetti = {'filosofia': 'conoscenza','meraviglia': 'origine','sapere': 'epistemologia','desiderio': 'motivazione','conoscenza': 'fine in sé'}

print("\nAssociazioni concettuali:")
for parola, concetto in concetti.items():
    print(f"- {parola} → {concetto}")
