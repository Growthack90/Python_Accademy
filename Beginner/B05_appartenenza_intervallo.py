"""Appartenenza di un numero a un intervallo"""
n = eval(input("Numero: "))
a = eval(input("Estremo inferiore: "))
b = eval(input("Estremo superiore: "))

if n > a and n < b:
    print(n, " è interno a [", a, ", ", b, "]", sep="")
elif n == a or n == b:
    print(n, " coincide con un estremo di [", a, ", ", b, "]", sep="")
else:
    print(n, " è esterno a [", a, ", ", b, "]", sep="")
