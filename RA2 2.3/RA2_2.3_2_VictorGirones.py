try:
    numero = int(input("Dis un número enter:    "))
    if numero <=0:
        print("Error: Has d'intoduir un número enter")
    else:
        total = sum(range(0,numero +1))
        print (f"La suma dels nombre de 0 fins a {numero} és {total}")
except ValueError:
    print("Error: has d'introduir un nombre vàlid.")