try:
    numero = int(input("Introdueix un número: "))
    print(f"Taula de multiplicar del {numero}:")

    for i in range(1, 11):
        resultat = numero * i
        print(f"{numero} x {i} = {resultat}")

except ValueError:
    print("Error: Has d'introduir un número enter vàlid.")