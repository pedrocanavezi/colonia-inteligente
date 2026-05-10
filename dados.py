def obter_dados_colonia():
    """Organiza os dados principais da colonia em dicionarios e listas."""
    colonia = {
        "nome": "Colonia Inteligente Aurora",
        "energia": {
            "geracao_atual": 40,
            "consumo_atual": 70,
            "reserva": 120,
            "sistemas": {
                "solar": {
                    "status": "ativo",
                    "geracao": 25
                },
                "eolico": {
                    "status": "ativo",
                    "geracao": 15
                }
            }
        },
        "clima": {
            "temperatura": -8,
            "vento_atual": 11,
            "condicao": "vento moderado"
        },
        "setores": {
            "suporte_vida": {
                "prioridade": "alta",
                "consumo": 35,
                "essencial": True
            },
            "laboratorio": {
                "prioridade": "media",
                "consumo": 20,
                "essencial": False
            },
            "lazer": {
                "prioridade": "baixa",
                "consumo": 15,
                "essencial": False
            }
        }
    }

    historico_vento = [8, 10, 12, 14]
    historico_energia_eolica = [20, 25, 30, 35]

    return colonia, historico_vento, historico_energia_eolica


def mostrar_resumo_colonia(colonia):
    print("=== DADOS DA COLONIA ===")
    print("Nome:", colonia["nome"])
    print("Geracao atual:", colonia["energia"]["geracao_atual"])
    print("Consumo atual:", colonia["energia"]["consumo_atual"])
    print("Reserva:", colonia["energia"]["reserva"])
    print("Vento atual:", colonia["clima"]["vento_atual"])
    print()

    print("Sistemas de energia:")
    for nome, dados in colonia["energia"]["sistemas"].items():
        print("-", nome, "| status:", dados["status"], "| geracao:", dados["geracao"])
    print()

    print("Setores da colonia:")
    for nome, dados in colonia["setores"].items():
        print("-", nome, "| prioridade:", dados["prioridade"], "| consumo:", dados["consumo"])
