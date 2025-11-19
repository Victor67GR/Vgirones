# Nom i cognoms: Victor Girones Estuidant de Asix
# Data: 19/11/2025
# Descripció:
# Llegir i escriure: Obre un fitxer en mode lectura i escriptura (r+). Mostra el contingut per pantalla i afegeix una línia al final sense esborrar el contingut anterior.

fitxer = open("escriptura.txt", "r+")
contingut = fitxer.read()
print(contingut)
fitxer.write("\nAquesta és una línia afegida al final.")
fitxer.close()
