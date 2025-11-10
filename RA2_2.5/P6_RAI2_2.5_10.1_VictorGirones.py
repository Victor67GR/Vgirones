# Nom i cognoms: Victor Girones De Asix
# Data: 04/11/2025
# Descripció:
# Especificació de la tasca: Filtra nombres parells de diverses llistes, Defineix filtra_parells(llista). Aplica la funció a: [1, 2, 3, 4, 5, 6], [10, 15, 20, 25, 30], Imprimeix la nova llista de parells.

def filtra_parells(llista):
    return [num for num in llista if num % 2 == 0]  
llista1 = [1, 2, 3, 4, 5, 6]
llista2 = [10, 15, 20, 25, 30]
print("Nombres parells de la llista1:", filtra_parells(llista1))
print("Nombres parells de la llista2:", filtra_parells(llista2))    