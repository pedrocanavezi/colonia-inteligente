def tomar_decisao(energia_disponivel, consumo, setores):
    """Aplica regras simples para decidir o que a colonia deve fazer."""
    acoes = []

    if energia_disponivel < 50:
        acoes.append("ALERTA: reduzir consumo")

    if energia_disponivel < 50 and consumo > 60:
        acoes.append("ATIVAR MODO ECONOMIA")

    if consumo > energia_disponivel:
        acoes.append("DESLIGAR sistemas nao essenciais")

    if energia_disponivel >= consumo:
        acoes.append("Manter operacao normal")

    sistemas_mantidos = []
    sistemas_reduzidos = []

    for nome, dados in setores.items():
        if dados["essencial"]:
            sistemas_mantidos.append(nome)
        elif consumo > energia_disponivel:
            sistemas_reduzidos.append(nome)

    return {
        "acoes": acoes,
        "sistemas_mantidos": sistemas_mantidos,
        "sistemas_reduzidos": sistemas_reduzidos
    }
