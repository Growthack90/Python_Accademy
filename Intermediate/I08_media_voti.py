def media(valori):
    """Ritorna la media aritmetica di una lista di valori"""
    if len(valori) == 0: # Se la lista è vuota la media è 0. Se proseguisse si avrebbe
        return 0              # alla fine della funzione l'errore di divisione per 0.    
    
    # Altrimenti...
    somma = 0

    for valore in valori:
        somma += valore

    return somma / len(valori)
    
def conta_superiori_media(valori):
    """Ritorna il numero di valori superiori alla media di una lista di valori"""
    contatore = 0
    media_valori = media(valori) # Calcola la media una volta sola

    for valore in valori:
        if valore > media_valori:
            contatore += 1    
    
    return contatore

def conta_in_intervallo(valori, inf, sup):
    """Ritorna il numero di valori di una lista compresi in un intervallo"""
    contatore = 0

    for valore in valori:
        if valore >= inf and valore < sup: # Intervallo [inf, sup)
            contatore += 1    
    
    return contatore

if __name__ == "__main__":
    voti = [5, 7.5, 8, 5, 8, 7, 9.5, 5.5, 7, 7, 6, 4.5, 5, 3.5, 7, 6, 6.5, 4, 8, 7]
    print("N. voti:", len(voti))
    print("Media:", media(voti))
    print("N. voti superiori alla media:", conta_superiori_media(voti))
    print("N. voti insufficienti:", conta_in_intervallo(voti, 0, 6))
