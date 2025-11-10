# Nom i cognoms: Victor Girones De Asix
# Data: 06/11/2025
# Descripció:
# Crea un mòdul textos.py amb una funció que posi en majúscules, minúscules i capitalitzi textos.Importa’l amb un àlies (import textos as tx) i prova les funcions amb frases diferents.





def majuscules(text):
    return text.upper()

def minuscules(text):
    return text.lower()

def capitalitza(text):
    return text.capitalize()

frase = "hola, com estàs?"

print("Majúscules:", majuscules(frase))
print("Minúscules:", minuscules(frase))
print("Capitalitza:", capitalitza(frase))
