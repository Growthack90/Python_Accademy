"""utilizza un ciclo "while" per stampare tutti i numeri divisibili per 3 e 5 minori di "n", dove quest'ultimo è inserito dall'utente"""
n = int(input("Numero: "))

i = 1

while i < n:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
    i += 1    
