set([1,2,3,1,3,4])

letras = set("Abacaxi")
print(letras)

set(("palio", "gol", "celta", "palio"))

numeros = { 1,2,3,2}

numeros = list(numeros)

print(numeros[0])

conjunto_a = {1,2}
conjunto_b = {3,4}

conjunto_a.union(conjunto_b)

conjunto_a = {1,2,3}
conjunto_b = {2, 3,4}

conjunto_a.intersection(conjunto_b)

conjunto_a = {1,2,3}
conjunto_b = {2, 3,4}
conjunto_c = {1, 0}
conjunto_a.difference(conjunto_b)
conjunto_b.difference(conjunto_a)

conjunto_a.issubset(conjunto_b)

conjunto_a.isdisjoint(conjunto_b)
conjunto_a.isdisjoint(conjunto_c)

sorteio = {1 ,23}

sorteio.add(25)
sorteio.add(42)

sorteio.clear()
