paraula = input("Escriu una paraula: ")
paraula = paraula.lower()
if paraula == paraula[::-1]:
    print("És un palíndrom!")
else:
    print("No és un palíndrom.")
