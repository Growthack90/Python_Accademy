"""Somma i primi n numeri naturali"""
n = eval(input("Numero: "))
somma = 0
i = 1

while i <= n:
    somma += i
    i = i + 1

print("Somma: ", somma)
