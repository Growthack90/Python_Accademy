"""Due modi equivalenti per stampare il testo di un'operazione e il suo risultato"""
# 1° modo: usa un'unica istruzione per stampare l'operazione e il risultato
print("2^8 =", 2 ** 8)

# 2° modo: usa due istruzioni per stampare l'operazione e il risultato
print("2^8 =", end=" ") # Dopo la stampa non va a capo, ma stampa uno spazio
print(2 ** 8)
