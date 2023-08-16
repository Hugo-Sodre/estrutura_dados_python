frutas = ["laranja", "maça", "uva"]

frutas= []

letras = list("Python")

numeros = list(range(10))
print(numeros)
carro = ["Ferrari", 'f8', 4200000, 2020, 2900, "São paulo",True]

frutas = ["maça", "laranja", "uva", "pera"]

frutas[-1]
frutas[-3]

matriz = [
    [1, "a",2],
    ["b", 3, 4],
    [6,5,"c"]
]
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero %2==0]