def analisar_energia(geracao, consumo, reserva):
    """Compara geracao, consumo e reserva para gerar uma orientacao."""
    saldo = geracao - consumo

    if consumo > geracao:
        uso_reserva = consumo - geracao

        if reserva >= uso_reserva:
            mensagem = "ALERTA: consumo maior que geracao. Usar parte da reserva e reduzir consumo."
        else:
            mensagem = "RISCO CRITICO: geracao e reserva nao sustentam o consumo atual."
    elif geracao > consumo:
        mensagem = "SUGESTAO: armazenar energia excedente."
    else:
        mensagem = "ESTAVEL: geracao igual ao consumo."

    return {
        "geracao": geracao,
        "consumo": consumo,
        "reserva": reserva,
        "saldo": saldo,
        "mensagem": mensagem
    }


def calcular_consumo_total_setores(setores):
    total = 0

    for dados in setores.values():
        total += dados["consumo"]

    return total
