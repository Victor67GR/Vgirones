# Nom i cognoms: Victor Girones Estuidant de Asix
# Data: 19/11/2025
# Descripció:
# Comprovar si el fitxer existeix abans de llegir-lo: Fes un programa que intenti llegir un fitxer anomenat dades.txt, però abans comprovi si existeix. Si no existeix, mostra un missatge d’error amigable.

import os
if os.path.exists("dades.txt"):
    fitxer = open("dades.txt", "r")
    contingut = fitxer.read()
    print(contingut)
    fitxer.close()