from random import shuffle

def numeri_casuali(n):
    """Ritorna una lista con i numeri da 1 a n distribuiti casualmente"""
    numeri = [] # Lista da popolare coi numeri da 1 a n
    
    for i in range(1, 9 + 1): # Per es. con n = 3 va da 1 a 9 compresi
        numeri.append(i)

    shuffle(numeri) # Mescola i valori della lista numeri (to shuffle = mescolare)
    return numeri 

def matrice_quadrata(numeri, n):
    """Ritorna una matrice n x n con i valori presenti nella lista numeri"""
    matrice = [] # Matrice da ritornare    

    for riga in range(n): # Scorri le righe
        numeri_riga = []        

        for col in range(n): # Scorri le colonne
            index = riga*n + col # Indice del prossimo valore di numeri
            numeri_riga.append(numeri[index])

        matrice.append(numeri_riga) # Aggiungi alla matrice una riga di valori

    return matrice

def print_matrice(matrice, n):
    """Stampa una matrice n x n"""
    for i in range(n):
        for j in range(n):
            print(matrice[i][j], end="\t")

        print() # Alla fine della riga va a capo

def is_quadrato_perfetto(matrice, n):
    """Verifica se un quadrato è perfetto"""
    is_perfetto = True

    # Controllo se ci sono tutti i numeri da 1 a n**2
    numero = 1
    
    while numero <= n**2 and is_perfetto:
        is_presente = False
        
        for riga in range(n):
            for col in range(n):
                if matrice[riga][col] == numero:
                    is_presente = True

        if not is_presente:
            is_perfetto = False

        numero += 1
        
    return is_perfetto and is_quadrato_magico(matrice, n)

def somma_prima_riga(matrice, n):
    """Ritorna la somma dei valori della prima riga"""
    somma = 0
    
    for col in range(n):
        somma += matrice[0][col]
    return somma

def is_quadrato_magico(matrice, n):
    """Un quadrato è magico se la somma dei numeri fatta per ogni riga,
    per ogni colonna e per le due diagonali dà sempre lo stesso numero"""
    is_magico = True
    costante_magica = somma_prima_riga(matrice, n)

    # Controlla le somme di tutte le righe e delle colonne
    for i in range(n): 
        somma_riga = 0        
        somma_col = 0        

        for j in range(n):
            somma_riga += matrice[i][j] 
            somma_col += matrice[j][i] # Inverto i rif. di riga e colonna

        if somma_riga != costante_magica or somma_col != costante_magica:
            return False

    # Ora controlla le diagonali
    somma_diag1 = 0        
    somma_diag2 = 0        

    for i in range(n): 
        somma_diag1 += matrice[i][i] 
        somma_diag2 += matrice[i][n - i - 1]

    return somma_diag1 == costante_magica and somma_diag2 == costante_magica
        
numeri = numeri_casuali(9)
print(numeri)
matrice = matrice_quadrata(numeri, 3)
print_matrice(matrice, 3)
quadrato_perfetto = [[2, 7, 6],
                     [9, 5, 1],
                     [4, 3, 8]]
print("Costante:", somma_prima_riga(quadrato_perfetto, 3))
print(is_quadrato_perfetto(quadrato_perfetto, 3))

