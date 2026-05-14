def calcular_regressao_linear(x, y):
    """Calcula uma reta simples: y = a * x + b."""
    quantidade = len(x)
    soma_x = sum(x)
    soma_y = sum(y)
    soma_xy = 0
    soma_x_quadrado = 0

    for i in range(quantidade):
        soma_xy += x[i] * y[i]
        soma_x_quadrado += x[i] ** 2

    divisor = quantidade * soma_x_quadrado - soma_x ** 2

    if divisor == 0:
        return 0, 0

    a = (quantidade * soma_xy - soma_x * soma_y) / divisor
    b = (soma_y - a * soma_x) / quantidade

    return a, b


def prever_energia_eolica(vento, historico_vento, historico_energia):
    a, b = calcular_regressao_linear(historico_vento, historico_energia)
    previsao = a * vento + b
    return round(previsao, 2)
