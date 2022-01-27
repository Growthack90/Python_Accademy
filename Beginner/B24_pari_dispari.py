"""Controlla se un numero intero inserito dall'utente è pari o dispari"""
n = int(input("Numero: "))

if n % 2 == 0:          # Se il resto della divisione di n per 2 è uguale a 0 allora...
    print("Il numero", n, "è pari")
else:                         # ...altrimenti
    print("Il numero", n, "è dispari")
