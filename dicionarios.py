#chave e valor
pessoa = { "nome ": "Hugo", "idade" : 22}

pessoa = dict(nome = "Guilherme", idade = 28)

pessoa["telefone"] = "3333-1234"


dados = {"nome" : "Hugo", "idade" : 28, "telefone" : "3333-1234"}

print(dados["nome"])
print(dados["idade"])


carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}

print(carro.get("motor"))