# 📊 Indicadores de Continuidade - Base de Dados ANEEL

Este projeto desenvolve um dashboard interativo no Power BI, utilizando dados públicos da Agência Nacional de Energia Elétrica (ANEEL) para analisar a continuidade do fornecimento de energia elétrica no Brasil, com destaque para a análise regional e a possibilidade de detalhamento mensal dos indicadores.

## 🔎 Objetivo
Analisar o desempenho das distribuidoras de energia elétrica, com foco nos indicadores de:
- **DEC (Duração Equivalente de Interrupção por Unidade Consumidora)**
- **FEC (Frequência Equivalente de Interrupção por Unidade Consumidora)**

## 🛠 Tecnologias Utilizadas
- **Power BI** para modelagem de dados, criação de medidas DAX e visualização.
- **Python (pandas)** para tratamento inicial dos dados.
- **Power Query** para transformação e preparação dos dados.

## 📚 Principais etapas do projeto
- Tratamento e normalização dos dados extraídos do site da ANEEL.
- Criação de tabelas fato e dimensões (modelo estrela).
- Desenvolvimento de medidas em DAX para cálculos corretos dos indicadores.
- Construção de um dashboard intuitivo, limpo e responsivo.
- Implementação de filtros interativos por ano e região.

## 🔗 Fonte dos Dados
Os dados utilizados são públicos e estão disponíveis em:  
[Dados Abertos ANEEL - Indicadores de Continuidade](https://dadosabertos.aneel.gov.br/dataset/indicadores-coletivos-de-continuidade-dec-e-fec)
