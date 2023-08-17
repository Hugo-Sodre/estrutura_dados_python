def criar_carro (modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro("Palio", 1999, "abc-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")


def criar_carro (*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")


def criar_carro (modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="gasolina")



def somar(a,b) :
    return a+b

def exibir_resultado (a,b, funcao) :
    resultado = funcao(a, b)
    print(f"o resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)


def funcao(*args, **kw):
    funcao("python", 2022, curso="dio")
funcao()
print(funcao)
