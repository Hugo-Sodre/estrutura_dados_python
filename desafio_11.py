codigo_peca1, numero_peca1, valor_unitario_peca1 = input().split()
codigo_peca1 = int(codigo_peca1)
numero_peca1 = int(numero_peca1)
valor_unitario_peca1 = float(valor_unitario_peca1)

codigo_peca2, numero_peca2, valor_unitario_peca2 = input().split()
codigo_peca2 = int(codigo_peca2)
numero_peca2 = int(numero_peca2)
valor_unitario_peca2 = float(valor_unitario_peca2)


valor_total = (numero_peca1 * valor_unitario_peca1) + (numero_peca2 * valor_unitario_peca2)


print("VALOR A PAGAR: R$ {:.2f}".format(valor_total))