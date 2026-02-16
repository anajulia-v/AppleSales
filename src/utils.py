# importando as bibliotecas 
# pandas para manipulação e análise de dados
import pandas as pd
# pathlib para facilitar o trabalho com caminhos de arquivos
from pathlib import Path

# módulo para ler e armazenar as tabelas em dataframes
def load_data(path: Path) -> pd.DataFrame:
  return pd.read_csv(path, sep=',')

