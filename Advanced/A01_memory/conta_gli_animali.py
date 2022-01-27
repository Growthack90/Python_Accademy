"""Memory game: Ricordati quante volte era apparso un animale"""
from turtle import *
from random import randint
from time import sleep

def quadro_di_gioco(animale):
    """Primo scenario: sceglie a caso 28 costumi, li dispone sul canvas
    secondo una griglia e ritorna quante volte l'animale specificato è apparso."""
    contatore = 0 # Inizializzo a 0 il contatore dei costumi dell'animale da indovinare
    title("Conta gli animali")
    setup(600, 360) # Dimensiona e posiziona la finestra al centro dello schermo
    penup()
    speed(0)

    for costume in costumi: # Registra i costumi degli animali
        register_shape(costume)
        
    distanza = 85           # Distanza tra gli animali sullo schermo
    righe, colonne = 4, 7   # Numero di righe e di colonne (4 x 7 = 28 animali)
    sety(130)               # Parte a disegnare vicino al bordo superiore

    for riga in range(righe):
        setx(-255)          # Ogni riga parte vicino al bordo sinistro

        for colonna in range(colonne): # Stampa una riga di costumi casuali
            indice = randint(0, len(costumi) - 1) # Indice di un costume a caso
            costume = costumi[indice] # ...e relativo costume
            shape(costume)
            stamp()

            if costume == animale:
                contatore += 1  # Aumenta il numero dell'animale da indovinare
                
            forward(distanza)   # Spostati a destra per il costume successivo

        sety(ycor() - distanza) # Spostati in basso per la riga successiva

    return contatore

def quiz(animale, n_da_indovinare):
    """Secondo scenario: sipario con l'animale scelto, in cui chiede all'utente
    quante volte l'animale è apparso e dà un feedback sulla risposta data."""
    sleep(5) # Tempo per imprimersi nella memoria la scena prima che...
    sipario = Turtle() # ...cali il sipario
    register_shape("sipario.gif")
    sipario.shape("sipario.gif")
    sprite_animale = Turtle() # Uso il gergo degli "arcade": sprite invece di tartaruga
    sprite_animale.shape(animale) # Visualizza l'animale da indovinare
    n = numinput("Conta gli animali", "Quante volte è apparso questo animale?")
    sleep(1)
    sipario.hideturtle() # Togli il sipario
    sprite_animale.hideturtle() # e l'animale da indovinare
    goto(0, -40)
    messaggio = "COMPLIMENTI!" if n == n_da_indovinare else "RIPROVA!"
    write(messaggio, font=('Arial', 50), align="center")

if __name__ == "__main__":
    # L'istruzione seguente, essendo molto lunga, viene spezzata su due righe con "\"
    costumi = "elephant.gif", "giraffe.gif", "hippo.gif", "monkey.gif", "panda.gif", \
              "parrot.gif", "penguin.gif", "pig.gif", "rabbit.gif", "snake.gif"
    indice = randint(0, len(costumi) - 1) # Indice dell'animale da indovinare
    animale = costumi[indice] # ...e relativo costume
    n_da_indovinare = quadro_di_gioco(animale)
    quiz(animale, n_da_indovinare)
