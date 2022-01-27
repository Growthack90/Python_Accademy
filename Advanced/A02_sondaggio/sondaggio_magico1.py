from turtle import *

def sondaggio():
    """Gestisce la votazione, aggiornando e visualizzando il punteggio"""
    global punteggio # Dichiara la variabile perchè viene modificata dalla funzione
    fine = False # "Flag" per segnalare la fine del sondaggio

    while not fine:
        visualizza_risultati()
        prompt = "Qual è il più simpatico? (G)Gandalf, (R)Radagast, (S)Saruman, (0)Fine: "
        scelta = input(prompt).upper() # Converti comunque l'input in maiuscolo
        
        if scelta in "GRS":
            for mago in punteggio:
                if mago[0] == scelta: # mago[0] è l'iniziale del nome del mago
                    punteggio[mago] += 1 # Aumenta il relativo punteggio
        else:
            fine = True # Termina con qualsiasi input diverso da G, R e S

def visualizza_risultati():
    """Disegna i maghi e la percentuale di preferenze ottenuta"""
    tot_voti = sum(punteggio.values()) # Conta i voti registrati
    x = -500 # Distanza tra la posizione di un mago e l'altro
    clear()  # Pulisce il canvas, cancellando i disegni fatti finora
    penup()
    for mago in ("Gandalf", "Radagast", "Saruman"):
        register_shape(mago +".gif")
        shape(mago +".gif")
        goto(x, 0)
        showturtle()
        stamp()
        hideturtle()
        if tot_voti == 0: # Il controllo serve per evitare una divisione per 0
            perc_voti = 0
        else:
            perc_voti = int(punteggio[mago] / tot_voti * 100)
        goto(x, -310) # La posizione della percentuale è sotto la figura del mago
        write(str(perc_voti) +"%", font=("Arial", 40), align="center")
        x += 500 # Spostamento a destra

if __name__ == "__main__":
    setup(1440, 650) # Imposta la larghezza e l'altezza della finestra
    title("Il mago più simpatico della Terra di mezzo (2017)")
    punteggio = {"Gandalf":0, "Radagast":0, "Saruman":0}
    sondaggio()
