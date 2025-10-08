num = int(input("Introdueix un número enter positiu: "))

if num <= 1:
    print("No és un nombre primer.")
else:
    divisor = 2
    while divisor * divisor <= num and num % divisor != 0:
        divisor += 1
    print("És un nombre primer." if divisor * divisor > num else "No és un nombre primer.")
