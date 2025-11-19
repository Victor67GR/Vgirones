# Nom i cognoms: Victor Girones Estuidant de Asix
# Data: 19/11/2025
# Descripció:
# Assegurar el tancament del fitxer (amb error): Simula una operació amb fitxers on pot haver-hi un error durant la lectura. Assegura’t que el fitxer es tanqui sempre, fins i tot si es produeix un error en llegir-lo. Pista: utilitza try-except amb open(...) en mode "r", i si falla, obre'l en mode "w".

try:
    fitxer = open("operacio.txt", "r")
    contingut = fitxer.read()
    print("Contingut del fitxer:")
    print(contingut)
except Exception as e:
    print("S'ha produït un error en llegir el fitxer:", e)
finally:
    try:
        fitxer.close()
        print("El fitxer s'ha tancat correctament.")
    except:
        print("El fitxer no s'ha pogut tancar perquè no s'havia obert correctament.")
    try:
        fitxer = open("operacio.txt", "w")
        fitxer.write("Aquest es un text de prova per escriure en el fitxer.\n")
        fitxer.close()
        print("Fitxer creat i escrit correctament.")
    except Exception as e:
        print("No s'ha pogut crear o escriure en el fitxer:", e)

