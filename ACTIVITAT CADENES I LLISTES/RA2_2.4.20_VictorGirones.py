# Nom i cognoms: Victor Girones De Asix
# Data: 04/11/2025
# Descripció:
# Crea una nova llista amb les paraules que comencen per vocal.

paraules = input("Introdueix paraules separades per espais: ").split()
vocals = "aeiouAEIOU"
nova_llista = [p for p in paraules if p[0] in vocals]
print(nova_llista)