import pandas as pd

# Lê o arquivo original
df = pd.read_csv("indicadores-continuidade-coletivos-2024.csv", sep=';', encoding='latin1')

# Limpa espaços e deixa nomes em caixa alta
df['SigAgente'] = df['SigAgente'].str.strip().str.upper()

# Mapeamento atualizado
mapa_regioes = {
    "EQUATORIAL MA": "Nordeste",
    "EQUATORIAL PI": "Nordeste",
    "EQUATORIAL AL": "Nordeste",
    "COELBA": "Nordeste",
    "COSERN": "Nordeste",
    "NEOENERGIA PE": "Nordeste",
    "ENEL CE": "Nordeste",
    "ENEL RJ": "Sudeste",
    "LIGHT": "Sudeste",
    "LIGHT SESA": "Sudeste",
    "CPFL-PAULISTA": "Sudeste",
    "CPFL PAULISTA": "Sudeste",
    "CEMIG-D": "Sudeste",
    "EDP ES": "Sudeste",
    "EDP SP": "Sudeste",
    "ELEKTRO": "Sudeste",
    "ENEL GO": "Centro-Oeste",
    "EQUATORIAL GO": "Centro-Oeste",
    "ENERGISA MT": "Centro-Oeste",
    "EQUATORIAL PA": "Norte",
    "ELETROACRE": "Norte",
    "BOA VISTA": "Norte",
    "CEEE-D": "Sul",
    "CELESC-DIS": "Sul",
    "COPEL-DIS": "Sul",
    "RGE SUL": "Sul",
      "EAC": "Norte",
  "CEA": "Norte",
  "ETO": "Centro-Oeste",
  "CPFL JAGUARI": "Sudeste",
  "DEMEI": "Sul",
  "ERO": "Norte",
  "ELFSM": "Sul",
  "SULGIPE": "Nordeste",
  "COCEL": "Sul",
  "CHESP": "Sudeste",
  "DMED": "Sudeste",
  "PACTO ENERGIA PR": "Sul",
  "ELETROPAULO": "Sudeste",
  "DCELT": "Sul",
  "EFLJC": "Sul",
  "EFLUL": "Sul",
  "MUXENERGIA": "Sul",
  "EMS": "Sudeste",
  "UHENPAL": "Sul",
  "EMT": "Centro-Oeste",
  "CERTHIL": "Sul",
  "CERILUZ": "Sul",
  "CERMISSÕES": "Sul",
  "COPREL": "Sul",
  "CPFL-PIRATINING": "Sudeste",
  "CRELUZ-D": "Sul",
  "CERAL-DIS": "Sul",
  "NEOENERGIA BRASÍLIA": "Centro-Oeste",
  "ESS": "Sudeste",
  "CERCI": "Sul",
  "CERAL ANITÁPOLIS": "Sul",
  "CEDRI": "Sul",
  "CEREJ": "Sul",
  "CERGAPA": "Sul",
  "CERVAM": "Sul",
  "CERMOFUL": "Sul",
  "CEJAMA": "Sul",
  "CERGRAL": "Sul",
  "CETRIL": "Sul",
  "CERIS": "Sul",
  "CERCOS": "Sul",
  "CERTREL": "Sul",
  "CEGERO": "Sul",
  "CEPRAG": "Sul",
  "COOPERALIANÇA": "Sul",
  "CERIPA": "Sul",
  "EQUATORIAL GO": "Centro-Oeste",
  "CERSUL": "Sul",
  "EMR": "Sul",
  "COOPERCOCAL": "Sul",
  "ESE": "Nordeste",
  "EPB": "Nordeste",
  "ELETROCAR": "Sul",
  "CERGAL": "Sul",
  "CERPRO": "Sul",
  "CERIM": "Sul",
  "COOPERMILA": "Sul",
  "EBO": "Centro-Oeste",
  "CERNHE": "Sul",
  "CERES": "Sul",
  "ENF": "Sul",
  "AME": "Sul",
  "COOPERA": "Sul",
  "CERFOX": "Sul",
  "CEDRAP": "Sul",
  "COOPERLUZ": "Sul",
  "CERTAJA": "Sul",
  "CERTEL ENERGIA": "Sul",
  "CERSAD DISTRIBUIDORA": "Sul",
  "CASTRO-DIS": "Sul",
  "CODESAM": "Sudeste",
  "CERRP": "Sudeste",
  "HIDROPAN": "Sul",
  "CERMC": "Sul",
  "COOPERZEM": "Sudeste",
  "CERPALO": "Sul",
  "CERAL ARARUAMA": "Sudeste",
  "COORSEL": "Sul",
  "CERBRANORTE": "Sul",
  "CERAÇÁ": "Sul",
  "COOPERNORTE": "Sudeste",
  "CEMIRIM": "Sudeste",
  "COOPERSUL": "Sudeste",
  "CELETRO": "Sul"
}

# Cria coluna de região
df['Região'] = df['SigAgente'].map(mapa_regioes)

# Filtra só o ano de 2024 (se tiver a coluna)
if 'Ano' in df.columns:
    df_2024 = df[df['Ano'] == 2024].copy()
else:
    df_2024 = df.copy()

# Mostrar distribuidoras não mapeadas
nao_mapeadas = df_2024[df_2024['Região'].isna()]['SigAgente'].unique()
print("\n⚠️ Distribuidoras sem região atribuída:")
print(nao_mapeadas)

# Exportar em CSV
df_2024.to_csv("dados_tratados_aneel_2024.csv", index=False, sep=';', encoding='utf-8')

print("\n✅ Arquivo salvo: dados_tratados_aneel_2024.csv")
