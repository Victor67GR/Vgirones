# Nom i cognoms: Victor Girones Estuidant de Asix
# Data: 19/11/2025
# Descripció:
# Comptar línies: Llegeix un fitxer i mostra quantes línies té.

fitxer = open("missatge.txt", "r")
linies = fitxer.readlines()
print("El fitxer te", len(linies), "linies.")
fitxer.close()