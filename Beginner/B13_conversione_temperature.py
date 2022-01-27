"""Crea un programma per la conversione di valori di temperatura tra gradi Celsius (o centigradi) e gradi Fahrenheit e Kelvin. Le formule di equivalenza sono:
T(°F) = T(°C) * 1,8 + 32
T(°K) = T(°C) + 273,15
Il programma chiede all'utente di inserire un numero è un carattere che indica l'unità di misura di arrivo ("F" o "K")"""

t_celsius = eval(input("Temperatura in °C: "))
t_fahrenheit = t_celsius * 1.8 + 32
t_kelvin = t_celsius + 273.15

print("Temperatura in °F:", t_fahrenheit)
print("Temperatura in °K:", t_kelvin)
