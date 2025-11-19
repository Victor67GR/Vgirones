# Nom i cognoms: Victor Girones Estuidant de Asix
# Data: 19/11/2025
# Descripció:
# Llegir un fitxer: Crea un fitxer de text anomenat missatge.txt amb contingut a mà (o des del codi). Escriu un programa que llegeixi i mostri el contingut per pantalla.

fitxer = open("missatge.txt", "r")
contingut = fitxer.read()
print(contingut)
fitxer.close()
