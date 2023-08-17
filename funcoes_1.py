def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"seja bem vindo {nome}")


def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero + 1

    return antecessor, sucessor

calcular_total([10,20,34])

retorna_antecessor_e_sucessor(10)