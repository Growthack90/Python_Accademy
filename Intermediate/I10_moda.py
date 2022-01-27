def moda(valori):
    """Ritorna la moda di una lista di valori"""
    valore_moda = None
    freq_moda = 0

    for valore1 in valori: # Scorre gli elementi della lista...
        contatore = 0
        
        for valore2 in valori: #...e li confronta con ciascun valore della lista
            if valore1 == valore2:
                contatore += 1

        if contatore > freq_moda: # Controlla se ha trovato una nuova moda
            freq_moda = contatore
            valore_moda = valore1

    return valore_moda

def input_valori():
    """Ritorna la lista di valori inseriti dall'utente"""
    valori = []
    is_fine = False
    
    while not is_fine:
        valore = eval(input("Valore (0=Fine): "))
        if valore != 0:
            valori.append(valore)
        else:
            is_fine = True
        
    return valori

if __name__ == "__main__":
    voti = [5, 7.5, 8, 5, 8, 7, 9.5, 5.5, 7, 7, 6, 4.5, 5, 3.5, 7, 6, 6.5, 4, 8, 7]
    print("Moda:", moda(voti))
    valori = input_valori()
    # valori = [41, 2, 23, 11, 53, 23, 11, 98, 23, 3, 17, 41]
    print("Moda:", moda(valori))
