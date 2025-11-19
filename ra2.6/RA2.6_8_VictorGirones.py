# Nom i cognoms: Victor Girones Estuidant de Asix
# Data: 19/11/2025
# Descripció:
# Evitar que el programa es bloquegi si el fitxer està mal format: Suposa que tens un fitxer nombres.txt que hauria de contenir un nombre enter per línia. Fes un programa que llegeixi cada línia i la transformi en enter. Si alguna línia no és un enter vàlid, captura l’error i mostra un missatge, però continua amb la resta.

fitxer = open("nombres.txt", "r")
for linia in fitxer:
    try:
        nombre = int(linia.strip())
        print("Nombre llegit:", nombre)
    except ValueError:
        print("Error: La linia no es un nombre enter valid:", linia.strip())
fitxer.close()