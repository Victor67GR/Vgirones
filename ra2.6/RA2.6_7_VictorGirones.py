# Nom i cognoms: Victor Girones Estuidant de Asix
# Data: 19/11/2025
# Descripció:
# Gestionar errors d'escriptura: Escriu un programa que intenti escriure en un fitxer anomenat resultats.txt, però gestiona l'error que es pot produir si el fitxer és només de lectura o si el sistema impedeix escriure-hi (permisos denegats).

try:
    fitxer = open("resultats.txt", "w")
    fitxer.write("Aquest es un text de prova per escriure en el fitxer.\n")
    fitxer.close()
    print("Escriptura realitzada amb exit.")
except IOError:
    print("Error: No s'ha pogut escriure en el fitxer. Comprova els permisos.")
except Exception as e:
    print("S'ha produït un error inesperat:", e)