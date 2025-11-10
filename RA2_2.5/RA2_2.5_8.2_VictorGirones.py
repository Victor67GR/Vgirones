# Nom i cognoms: Victor Girones De Asix
# Data: 06/11/2025
# Descripció:
# Fes un programa que mostri la data i hora actual i la formati de manera llegible (dd/mm/yyyy hh:mm) i calcula quants dies falten per una data determinada (com Nadal o el teu aniversari).

from datetime import datetime, date

ara = datetime.now()
print("Data i hora:", ara.strftime("%d/%m/%Y %H:%M"))

nadal = date(ara.year, 12, 25)
if nadal < ara.date(): nadal = date(ara.year + 1, 12, 25)
print("Dies fins a Nadal:", (nadal - ara.date()).days)
