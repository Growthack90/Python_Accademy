"""Stampa tabulata della tavola pitagorica"""
for i in range(1, 11):          # Scorre le righe
    for j in range(1, 11):      # Scorre le colonne
        print(i * j, end="\t")   # Usa la tabulazione come separatore tra loro i valori

    print() # Alla fine di ogni riga va a capo
