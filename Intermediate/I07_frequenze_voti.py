from media_voti import conta_in_intervallo

def frequenze(valori, inf, sup):
    """Ritorna un dizionario con le frequenze assolute e relative di una lista di valori.
    Ipotesi: i valori appartengono all'intervallo [inf, sup)"""
    freq = {}
    totale = 0
    n = len(valori)

    for i in range(inf, sup):
        for valore in valori:
            # Calcola e aggiungi al dizionario la frequenza assoluta e relativa
            # dei valori nell'intervallo (inf, sup]
            freq_assoluta = conta_in_intervallo(valori, i, i + 1)
            freq_relativa = int(freq_assoluta / n * 100)
            freq[i] = [freq_assoluta, freq_relativa]

        totale += freq_assoluta

    # Aggiungi all'ultimo intervallo gli eventuali valori rimanenti,
    # che sono uguali a sup e non sono stati considerati nel calcolo precedente
    freq[sup - 1][0] += n - totale
    freq[sup - 1][1] += int((n - totale) / totale * 100)
    
    return freq

if __name__ == "__main__":
    voti = [5, 7.5, 8, 5, 8, 7, 9.5, 5.5, 7, 7, 6, 4.5, 5, 3.5, 7, 6, 6.5, 4, 8, 7]
    freq = frequenze(voti, 0, 10)

    for chiave, valore in freq.items():
        # Stampa ciascuno valore intero (d=decimal) in un campo di 2 caratteri
        freq_a, freq_r = valore
        print("Intervallo {:2d}:{:2d} ({:2d}%)".format(chiave + 1, freq_a, freq_r))
