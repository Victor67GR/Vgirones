def reverteix_cadena(cadena):
    invertida = ""
    for lletra in cadena:
        invertida = lletra + invertida
    return invertida
text = input("Escriu una cadena: ")
print("Cadena invertida:", reverteix_cadena(text))
