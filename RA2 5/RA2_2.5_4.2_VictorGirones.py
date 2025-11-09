# Nom i cognoms: Victor Girones De Asix
# Data: 06/11/2025
# Descripció:
# Escriu un programa que simuli llençar un dau (1-6) usant el mòdul random i prova de fer una funció que llenci el dau n vegades i mostri la mitjana.

import random

n = 10
print("Mitjana:", sum(random.randint(1, 6) for _ in range(n)) / n)
