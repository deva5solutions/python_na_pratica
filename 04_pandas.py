import pandas as pd

# Exemplo de leitura de CSV (crie um arquivo vendas.csv)
df = pd.read_csv('vendas.csv')

# Visualizar as primeiras linhas
print(df.head())

# Agrupar por produto e somar valor
print(df.groupby('produto')['valor'].sum())
