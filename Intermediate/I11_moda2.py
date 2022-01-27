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
    """Ritorna la lista di valori inseriti dall'utente
    chiedendogli preventivamente quanti valori vuole inserire"""
    valori = []
    n = int(input("Numero di valori: "))
    
    for i in range(n):
        valore = eval(input("Valore: "))
        valori.append(valore)
        
    return valori

if __name__ == "__main__":
    valori = input_valori()
    print("Moda:", moda(valori))
