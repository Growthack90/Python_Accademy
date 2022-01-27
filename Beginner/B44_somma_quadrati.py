"""Somma i quadrati da 1 a n"""
n = eval(input("Numero: "))
somma = 0
i = 1

while i <= n:
    somma += i*i
    print(i*i, end=" ")
    i = i + 1

print("\nSomma quadrati: ", somma)
