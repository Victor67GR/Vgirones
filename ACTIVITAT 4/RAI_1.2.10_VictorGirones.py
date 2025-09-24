num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

suma = num1 + num2
print("Suma:", suma)

resta = num1 - num2
print("Resta:", resta)

multiplicacio = num1 * num2
print("Multiplicació:", multiplicacio)

if num2 != 0:
    divisio = num1 / num2
    print("Divisió:", divisio)
else:
    print("Divisió: No es pot dividir per zero")
