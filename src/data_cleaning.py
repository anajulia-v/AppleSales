# importando as bibliotecas 
# pandas para manipulação e análise de dados
import pandas as pd

# funções reutilizáveis para o tratamento de dados

# padronização dos nomes das colunas
def rename_columns(df, new_columns) :
  df.columns = new_columns
  return df

# conversão de tipo de dados
def convert_dates(df, column, fmt):
  df[column] = pd.to_datetime(df[column], format=fmt)
  return df

# validação de relacionamentos entre tabelas 
def validate_relationship(df_main, df_lookup, key):
  validacao = df_main.merge(
    df_lookup[[key]],
    on=key,
    how='left',
    indicator=True
  )

  invalidos = validacao[validacao['_merge'] == 'left_only']
  print(f'Registros inválidos: {len(invalidos)}')
  return invalidos