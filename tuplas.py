#tupla é imutavel

frutas = ("laranja", "pera", "uva")

letras = tuple("python")

numeros = tuple([1,2,3,4])

pais = ("Brasil",)

print(frutas[0])

carros = ('gol', "celta", "palio",)

for carro in carros:
    print(carro)

carros = ("gol")
print(isinstance(carros, tuple))