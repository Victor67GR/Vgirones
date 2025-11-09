# Nom i cognoms: Victor Girones De Asix
# Data: 06/11/2025
# Descripció:
# Crea una carpeta utilitats amb:__init__.py (pot estar buit),temps.py (funcions per convertir segons a hores, minuts, etc.),moneda.py (funció per convertir entre euros i dòlars).

def segons_a_minuts(segons):
    return segons / 60

def segons_a_hores(segons):
    return segons / 3600

def segons_a_dies(segons):
    return segons / 86400

def euros_a_dolars(euros, tipus_canvi=1.1):
    return euros * tipus_canvi

segons = 7200
print(segons, "segons són:")
print("-", segons_a_minuts(segons), "minuts")
print("-", segons_a_hores(segons), "hores")
print("-", segons_a_dies(segons), "dies")

euros = 50
print(f"{euros} euros són {euros_a_dolars(euros)} dòlars")