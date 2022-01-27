"""Stabilisce il massimo tra tre numeri inseriti dall'utente (prima versione)"""
a = eval(input("Primo numero: "))
b = eval(input("Secondo numero: "))
c = eval(input("Terzo numero: "))

if a > b:
    # Certamente "b" non è il massimo, ci concentriamo quindi solo su "a" e "c"
    if a > c:
        print("Il massimo è", a)
    else:
        print("Il massimo è", c)
else:
    # Certamente "a" non è il massimo, ci concentriamo quindi solo su "b" e "c"
    if b > c:
        print("Il massimo è", b)
    else:
        print("Il massimo è", c)
