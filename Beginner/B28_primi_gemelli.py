"""Stampa le coppie di primi gemelli minori di 100"""
import primalita

def print_gemelli(n):
    for i in range(3, n, 2): # Considero solo i numeri dispari >= 3
        if primalita.is_primo(i) and primalita.is_primo(i + 2):
            print(i, i + 2, end=",  ")

print_gemelli(100)
