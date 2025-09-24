import math

PI = 3.1416  # Constant

# Funció per calcular L'àrea d'un cercle
def calcular_area(radi): 
    return PI * radi ** 2

radi = float(input("Introdueix el radi: ")) # Variable + línia que llegeix dades de l'usuari
area = calcular_area(radi) # Variable
print("L'àrea del cercle és:", area) # Línia que mostra el resultat
