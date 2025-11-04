frase = input("Escriu una frase: ")
vocal_count = 0
for lletra in frase:
    if lletra.lower() in "aeiou":
        vocal_count += 1
print("Nombre de vocals:", vocal_count)
