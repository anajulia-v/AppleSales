# pathlib para facilitar o trabalho com caminhos de arquivos
from pathlib import Path

# diretório raiz do projeto
base_dir = Path(__file__).resolve().parent.parent

# pastas principais
raw_data_path = base_dir / "data" / "raw"
processed_data_path = base_dir / "data" / "processed"

# arquivos raw
products_raw_path = raw_data_path / "products.csv"
category_raw_path = raw_data_path / "category.csv"
stores_raw_path = raw_data_path / "stores.csv"
sales_raw_path = raw_data_path / "sales.csv"
warranty_raw_path = raw_data_path / "warranty.csv"

# arquivos tratados
products_processed_path = processed_data_path / "products_processed.csv" 
stores_processed_path = processed_data_path / "stores_processed.csv" 
sales_processed_path = processed_data_path / "sales_processed.csv"
warranty_processed_path = processed_data_path / "warranty_processed.csv"