"""Scrivi un programma che dato un anno verifica se è bisestile
Un anno è bisestile se è divisibile per 4 e non è divisibile
per cento oppure è divisibile per 400. Quindi il 1900 non è bisestile,
mentre il 2000 lo è.
"""
anno = eval(input("Anno: "))

# Le parentesi sono necessarie, perchè prima deve essere eseguito l'"or", poi l'"and"
if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
    print("Il", anno, "è bisestile")
else:
    print("Il", anno, "non è bisestile")

'''        
Anno: 1900
Il 1900 non è bisestile
>>> ================================ RESTART ================================
>>> 
Anno: 2000
Il 2000 è bisestile
'''
