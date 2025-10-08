frase = input("Introdueix una frase: ")
vocals = "aeiouAEIOU"
i = 0
comptador = 0

while i < len(frase):
    if frase[i] in vocals:
        comptador += 1
    i += 1
print("Nombre de vocals:", comptador)
