"""chiede all’utente di inserire un numero e stampa se è positivo, zero o negativo"""
numero = eval(input("Numero: "))

if numero > 0:
    print("Positivo")
elif numero < 0:    
    print("Negativo")
else:
    print("Zero")
