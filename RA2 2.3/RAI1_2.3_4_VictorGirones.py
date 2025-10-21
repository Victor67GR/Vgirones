try:
    numero = int(input("Introdueix un nombre enter positiu: "))
    if numero < 0:
        print("Error: has d’introduir un nombre enter positiu.")
    else:
        print(f"Nombres parells des de 0 fins a {numero}:")
        for i in range(0, numero +1, 2):
            print(i)
except ValueError:
    print("Error: has d’introduir un nombre enter vàlid.")