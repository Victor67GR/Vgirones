try:
    numero =int(input("Introdueix un nombre enter positiu: "))
    if numero < 2:
        print("Has d’introduir un nombre més gran o igual a 2.")
    else:
        print(f"Nombres primers des de 2 fins a {numero}:")
        for num in range(2, numero + 1):
            primer = True
            for i in range(2, num):
                if num % i == 0:
                    primer = False
                    break
            if primer:
                print(num)

except ValueError:
    print("Error: has d’introduir un nombre enter vàlid.")
