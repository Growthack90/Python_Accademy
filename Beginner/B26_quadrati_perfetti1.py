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
        
numeri = numeri_casuali(9)
print(numeri)
matrice = matrice_quadrata(numeri, 3)
print_matrice(matrice, 3)

