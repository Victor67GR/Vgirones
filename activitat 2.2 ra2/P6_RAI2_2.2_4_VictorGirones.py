import random

secret = random.randint(1, 100)
intents = 0

while True:
    try:
        guess = int(input("Introdueix un número entre 1 i 100: "))
    except ValueError:
        print("Si us plau, introdueix un nombre enter vàlid.")
        continue

    intents += 1

    if guess < secret:
        print("Massa baix")
    elif guess > secret:
        print("Massa alt")
    else:
        print(f"Correcte! Has encertat el {secret} en {intents} intents.")
        break
