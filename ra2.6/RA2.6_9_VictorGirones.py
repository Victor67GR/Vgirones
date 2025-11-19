# Nom i cognoms: Victor Girones Estuidant de Asix
# Data: 19/11/2025
# Descripció:
# Crear el fitxer si no existeix: Intenta obrir un fitxer en mode lectura. Si no existeix, crea’l automàticament i escriu-hi una línia per defecte: "Fitxer creat automàticament". Pista: utilitza try-except amb open(...) en mode "r", i si falla, obre'l en mode "w".

try:
    fitxer = open("nou_fitxer.txt", "r")
    contingut = fitxer.read()
    print("El fitxer ja existeix. Contingut:")
    print(contingut)
    fitxer.close()
except FileNotFoundError:
    fitxer = open("nou_fitxer.txt", "w")
    fitxer.write("Fitxer creat automaticament.\n")
    fitxer.close()
    print("El fitxer no existia i ha estat creat amb una línia per defecte.")