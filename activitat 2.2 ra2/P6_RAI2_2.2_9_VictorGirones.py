llista = [4, 7, 1, 9, 3, 8]
maxim = llista[0]
i = 0
while i < len(llista):
    if llista[i] > maxim:
        maxim = llista[i]
    i += 1
print("El número màxim és:", maxim)
