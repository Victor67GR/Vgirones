# Nom i cognoms: Victor Girones Estudiant de Asix
# Data: 19/11/2025
# Descripció:
# Escriure en un fitxer: Crea un programa que escrigui les següents 3 línies en un fitxer nou anomenat sortida.txt. El contingut anterior (si n'hi ha) ha de desaparèixer.

fitxer = open("sortida.txt", "w")
fitxer.write("Primera linia.\n")
fitxer.write("Segona linia.\n")
fitxer.write("Tercera linia.\n")
fitxer.close()

