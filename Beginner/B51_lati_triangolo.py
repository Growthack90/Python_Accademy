"""Stabilisce se tre numeri possono essere le misure dei lati di un triangolo"""
a = eval(input("Primo lato: "))
b = eval(input("Secondo lato: "))
c = eval(input("Terzo lato: "))

is_a_valido = a > 0 and a < b + c
is_b_valido = b > 0 and b < a + c
is_c_valido = c > 0 and c < a + b

if is_a_valido and is_b_valido and is_c_valido:
    print("I valori possono essere le misure dei lati di un triangolo")
else:
    print("I valori non possono essere le misure dei lati di un triangolo")  
