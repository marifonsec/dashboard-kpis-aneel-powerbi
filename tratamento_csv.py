import pandas as pd

# Caminho do CSV original
arquivo = "dados_tratados_aneel_2024.csv"

# Carregar CSV
df = pd.read_csv(arquivo, sep=';', encoding='utf-8')

# Corrigir vírgula para ponto e converter valores numéricos
df["VlrIndiceEnviado"] = df["VlrIndiceEnviado"].astype(str).str.replace(',', '.').astype(float)

# Separar NumCon e os demais indicadores
df_numcon = df[df["SigIndicador"] == "NumCon"].copy()
df_numcon["VlrIndiceEnviado"] = df_numcon["VlrIndiceEnviado"].astype(int)

df_indicadores = df[df["SigIndicador"] != "NumCon"]

# Juntar número de consumidores com os indicadores com base em conjunto + ano + mês
df_final = pd.merge(
    df_indicadores,
    df_numcon[["AnoIndice", "NumPeriodoIndice", "IdeConjUndConsumidoras", "VlrIndiceEnviado"]],
    on=["AnoIndice", "NumPeriodoIndice", "IdeConjUndConsumidoras"],
    how="left",
    suffixes=('', '_NumCon')
)

# Renomear a coluna de consumidores
df_final = df_final.rename(columns={"VlrIndiceEnviado_NumCon": "NumCon"})

# Exportar CSV final
df_final.to_csv("aneel_com_numcon.csv", index=False, sep=';', encoding='utf-8')

csv_path = "aneel_com_numcon.csv"

# Ler o CSV com separador ';' e codificação UTF-8
df = pd.read_csv(csv_path, sep=';', encoding='utf-8')

# Caminho do arquivo de saída em Excel
excel_path = "aneel_para_excel.xlsx"

# Salvar em formato Excel
df.to_excel(excel_path, index=False)