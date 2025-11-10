# Nom i cognoms: Victor Girones De Asix
# Data: 04/11/2025
# Descripció:
# Especificació de la tasca: Escriu una funció estat_persona(edat) que: Retorni "Menor d'edat", "Adult" o "Jubilat" segons l'edat i retorni tant l'estat com una descripció (return estat, descripcio).
def estat_persona(edat):
    if edat < 18:
        return "Menor d'edat", "La persona és menor d'edat."
    elif 18 <= edat < 65:
        return "Adult", "La persona és adulta."
    else:
        return "Jubilat", "La persona està jubilada."
estat, descripcio = estat_persona(45)
print(estat)
print(descripcio)
estat, descripcio = estat_persona(16)
print(estat)
print(descripcio)
estat, descripcio = estat_persona(70)
print(estat)
print(descripcio)
estat, descripcio = estat_persona(18)
print(estat)
print(descripcio)