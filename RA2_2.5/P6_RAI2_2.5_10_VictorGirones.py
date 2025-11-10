# Nom i cognoms: Victor Girones De Asix
# Data: 04/11/2025
# Descripció:
# Especificació de la tasca: Escriu una funció filtra_parells(llista) que: Rebi una llista de nombres i retorni una nova llista només amb els nombres parells.

def filtra_parells(llista):
    return [num for num in llista if num % 2 == 0]
print(filtra_parells([1, 2, 3, 4, 5, 6]))
print(filtra_parells([10, 15, 20, 25, 30]))
print(filtra_parells([7, 9, 11]))
print(filtra_parells([]))
