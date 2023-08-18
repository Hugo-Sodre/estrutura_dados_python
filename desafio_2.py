valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())


def valor_total_hamburguer_bebidas(valorHamburguer, quantidadeHamburguer, valorBebida, quantidadeBebida, valorPago):
    totalHamburguer = valorHamburguer * quantidadeHamburguer
    totalBebida = valorBebida * quantidadeBebida
    valorTotal = totalHamburguer + totalBebida
    troco = valorPago - valorTotal
    return valorTotal, troco


valorFinal, troco = valor_total_hamburguer_bebidas(valorHamburguer, quantidadeHamburguer, valorBebida, quantidadeBebida,
                                                   valorPago)
print(f"O preço final do pedido é R$ {valorFinal:.2f}. Seu troco é R$ {troco:.2f}.")
