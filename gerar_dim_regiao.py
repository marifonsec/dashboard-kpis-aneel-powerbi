import pandas as pd

# Carregar o CSV com os dados completos
df = pd.read_csv("aneel_com_numcon.csv", sep=';', encoding='utf-8')

# Selecionar apenas as colunas relevantes para a dimensão
df_dim = df[["SigAgente", "IdeConjUndConsumidoras", "DscConjUndConsumidoras", "Região"]].drop_duplicates()

# Ordenar por nome da distribuidora e conjunto, opcionalmente
df_dim = df_dim.sort_values(by=["SigAgente", "IdeConjUndConsumidoras"])

# Salvar como CSV de dimensão
df_dim.to_csv("dim_localidade.csv", index=False, sep=';', encoding='utf-8')
