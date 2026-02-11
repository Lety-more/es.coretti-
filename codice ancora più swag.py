import pygame
import random
import math

# --- Inizializzazione ---
pygame.init()
LARGHEZZA, ALTEZZA = 600, 400
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Colpisci i cerchi")
clock = pygame.time.Clock()

# --- Variabili ---
punteggio = 0
raggio = 25

c1 = [150, 50, (255,0,0), raggio]
c2 = [200, 100, (0,255,0), raggio]
c3 = [250, 150, (0,0,255), raggio]

cerchi = [c1, c2, c3]   # lista di cerchi: [x, y, colore, raggio]


# --- Funzioni ---
def disegna_cerchi(lista):
    """Disegna tutti i cerchi"""
    for c in lista:
        pygame.draw.circle(schermo, c[2],(c[0],c[1]),c[3]) 
    # TODO: ciclo for per disegnare i cerchi con pygame.draw.circle


def muovi_cerchi(lista, speed):
    """Aggiorna posizione verticale"""
    global punteggio
    for c in lista:
        c[1] = c[1]+speed
        if c[1]-c[3] > ALTEZZA:
            c[1] = 0-c[3]
            punteggio = punteggio -1
            print(punteggio)
    # TODO: far scendere i cerchi
    # TODO: se un cerchio tocca il fondo, riportarlo in alto e togliere 1 punto


def aggiungi_cerchio(lista_cerchi):
    """Aggiunge un nuovo cerchio in alto con valori casuali"""
    # TODO: posizione x casuale tra 0 e LARGHEZZA, y=0
    x = random.randint(0, LARGHEZZA)
    y = 0
    # TODO: colore casuale
    colore = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    # TODO: raggio fisso (es. 25)
    # TODO: aggiungerlo alla lista
    lista_cerchi.append([x,y,colore,raggio])


def clic_su_cerchi(lista, pos_mouse):
    """Controlla se il clic è dentro un cerchio"""
    print("x: ",pos_mouse[0], " y: ",pos_mouse[1])
    
    global punteggio
    # TODO: calcolare distanza mouse-centro
    # TODO: se distanza <= raggio → punteggio +1 e rimuovere il cerchio


# --- Ciclo principale ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clic_su_cerchi(cerchi, event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                aggiungi_cerchio(cerchi)

    muovi_cerchi(cerchi, 2)

    schermo.fill((255,255,255))
    disegna_cerchi(cerchi)

    # Mostra punteggio
    font = pygame.font.SysFont(None, 40)
    testo = font.render(f"Punteggio: {punteggio}", True, (0,0,0))
    schermo.blit(testo, (10,10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
