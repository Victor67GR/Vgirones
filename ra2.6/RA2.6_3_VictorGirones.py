# Nom i cognoms: Victor Girones Estuidant de Asix
# Data: 19/11/2025
# Descripció:
# Afegir continguts: Afegeix una línia nova a un fitxer existent (sortida.txt) sense esborrar el que ja hi ha.

fitxer = open("sortida.txt", "a")
fitxer.write("Quarta linia afegida.\n")
fitxer.close()
