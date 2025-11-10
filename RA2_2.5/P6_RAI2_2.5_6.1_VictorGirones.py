# Nom i cognoms: Victor Girones De Asix
# Data: 04/11/2025
# Descripció:
# Especificació de la tasca: Multiplica una sèrie de nombres. Defineix multiplica_tot(*nombres). Crea dues crides: Multiplica 2, 3, 4, Multiplica 5, 10.

def multiplica_tot(*nombres):
    resultat = 1
    for nombre in nombres:
        resultat *= nombre
    return resultat
print("El resultat de multiplicar 2, 3, 4 és:", multiplica_tot(2, 3, 4))
print("El resultat de multiplicar 5, 10 és:", multiplica_tot(5, 10))        
    
