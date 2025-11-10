# Nom i cognoms: Victor Girones De Asix
# Data: 04/11/2025
# Descripció:
# Especificació de la tasca: Escriu una funció multiplica_tot(*nombres) que rebi qualsevol quantitat de nombres i retorni la seva multiplicació.

def multiplica_tot(*nombres):
    resultat = 1
    for nombre in nombres:
        resultat *= nombre
    return resultat
print(multiplica_tot(2, 3, 4))  
print(multiplica_tot(5, 6))     
print(multiplica_tot(7))       
print(multiplica_tot())         