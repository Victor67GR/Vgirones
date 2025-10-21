try:
    numero = int(input("Dis un número   "))

    for i in range(0,numero+1):
        print(i)

except ValueError:
    print ("no pot ser lletres, nomes números")