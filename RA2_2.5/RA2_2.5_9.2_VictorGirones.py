# Nom i cognoms: Victor Girones De Asix
# Data: 06/11/2025
# Descripció:
# Crea validacions.py amb funcions: es_email_valid(email), es_telefon_valid(telefon)

import re

def es_email_valid(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

def es_telefon_valid(telefon):
    return bool(re.match(r'^\d{9}$', telefon))

# Proves
email = "hola@example.com"
telefon = "612345678"

print(email, "és vàlid?", es_email_valid(email))
print(telefon, "és vàlid?", es_telefon_valid(telefon))
