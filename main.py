from dados import obter_dados_colonia, mostrar_resumo_colonia
from decisoes import tomar_decisao
from energia import analisar_energia, calcular_consumo_total_setores
from previsao import prever_energia_eolica


def executar_sistema():
    colonia, historico_vento, historico_energia = obter_dados_colonia()

    mostrar_resumo_colonia(colonia)

    geracao = colonia["energia"]["geracao_atual"]
    consumo = colonia["energia"]["consumo_atual"]
    reserva = colonia["energia"]["reserva"]
    vento_atual = colonia["clima"]["vento_atual"]
    setores = colonia["setores"]

    print()
    print("=== ANALISE DE ENERGIA ===")
    analise = analisar_energia(geracao, consumo, reserva)
    print("Saldo de energia:", analise["saldo"])
    print(analise["mensagem"])

    print()
    print("=== DECISAO AUTOMATICA ===")
    decisao = tomar_decisao(geracao, consumo, setores)

    for acao in decisao["acoes"]:
        print("-", acao)

    print("Sistemas mantidos:", decisao["sistemas_mantidos"])
    print("Sistemas reduzidos:", decisao["sistemas_reduzidos"])

    print()
    print("=== PREVISAO DE ENERGIA EOLICA ===")
    previsao = prever_energia_eolica(vento_atual, historico_vento, historico_energia)
    print("Vento informado:", vento_atual)
    print("Energia eolica prevista:", previsao)

    print()
    print("=== CONFERENCIA DOS SETORES ===")
    consumo_total = calcular_consumo_total_setores(setores)
    print("Consumo total calculado pelos setores:", consumo_total)


if __name__ == "__main__":
    executar_sistema()
