numeros = [input("Número: ") for _ in range(10)]
parells = [int(n) for n in numeros if n[-1] in "02468"]
senars = [int(n) for n in numeros if n[-1] in "13579"]
print("Parells:", parells)
print("Senars:", senars)
