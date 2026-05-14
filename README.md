# Colonia Inteligente

Sistema simples em Python que representa uma colonia inteligente. O objetivo e organizar dados da colonia, analisar energia, tomar decisoes automaticas e fazer uma previsao simples de energia eolica usando regressao linear.

## Como o sistema foi organizado

O projeto foi separado em arquivos para deixar cada parte mais clara:

- `dados.py`: guarda os dados da colonia em dicionarios e listas.
- `energia.py`: compara geracao, consumo e reserva.
- `decisoes.py`: aplica regras de decisao.
- `previsao.py`: calcula uma regressao linear simples.
- `main.py`: junta tudo e mostra o resultado final.

## Estrutura de dados

Os dados principais ficam em um dicionario chamado `colonia`. Ele possui informacoes de energia, clima e setores.

Exemplo de organizacao hierarquica:

```python
energia -> sistemas -> solar / eolico
```

Tambem foram usadas listas para guardar dados historicos:

```python
historico_vento = [8, 10, 12, 14]
historico_energia_eolica = [20, 25, 30, 35]
```

## Regras de decisao

O sistema usa regras simples, como:

- Se a energia for menor que 50, reduzir consumo.
- Se a energia for menor que 50 e o consumo for maior que 60, ativar modo economia.
- Se o consumo for maior que a geracao, desligar sistemas nao essenciais.
- O suporte de vida sempre tem prioridade.

## Modelo de previsao

Foi usada regressao linear simples para estimar a energia eolica a partir da velocidade do vento.

Exemplo:

```text
Entrada: vento = 11
Saida: energia eolica prevista = 27.5
```

## Exemplo de entrada

```text
Geracao atual: 40
Consumo atual: 70
Reserva: 120
Vento atual: 11
```

## Exemplo de saida

```text
ALERTA: consumo maior que geracao. Usar parte da reserva e reduzir consumo.
- ALERTA: reduzir consumo
- ATIVAR MODO ECONOMIA
- DESLIGAR sistemas nao essenciais
Energia eolica prevista: 27.5
```

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

## Objetivo

O sistema ajuda a colonia a entender melhor seu uso de energia, identificar riscos quando o consumo passa da geracao e prever a geracao eolica com base no vento. Assim, a colonia deixa de apenas reagir aos problemas e passa a tomar decisoes mais planejadas.
