# Nom i cognoms: Victor Girones De Asix
# Data: 04/11/2025
# Descripció:
# Especificació de la tasca: Escriu una funció factorial(n) que calculi el factorial d'un nombre n de forma recursiva.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
print(factorial(0))
print(factorial(3))
print(factorial(7))
