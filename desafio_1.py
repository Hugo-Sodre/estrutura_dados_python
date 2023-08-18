nomeRestaurante = input("")
tempoEstimadoEntrega = int(input())


def tempo_estimado_entrega(nomeRestaurante, tempoEstimadoEntrega):
    mensagem = "O restaurante %s entrega em %d minutos." % (nomeRestaurante, tempoEstimadoEntrega)
    return mensagem


mensagem_saida = tempo_estimado_entrega(nomeRestaurante, tempoEstimadoEntrega)
print(mensagem_saida)

