"""Stabilisce il massimo tra tre numeri interi inseriti dall'utente (seconda versione)"""
a = eval(input("Primo numero: "))
b = eval(input("Secondo numero: "))
c = eval(input("Terzo numero: "))

if a > b and a > c: # Variazione rispetto alla prima versione
    massimo = a
else:
    # Certamente "a" non è il massimo, ci concentriamo quindi solo su "b" e "c"
    if b > c:
        massimo = b
    else:
        massimo = c

print("Il massimo è", massimo) # Rispetto alla prima versione, stampa solo alla fine
