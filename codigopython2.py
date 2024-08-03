#Exploração de Dados: Exibir as primeiras linhas e informações básicas do conjunto de dados, como número de linhas, colunas e tipos de dados presentes.

#importar a biblioteca Pandas
import pandas as pd

#definição da função
def carregar_csv(caminho_arquivo):

#tentando ler o arquivo CSV por meio de codificações 
    codificacoes = ['utf-8', 'latin1', 'windows-1252']
    for encoding in codificacoes:
        try:
            return pd.read_csv(caminho_arquivo, encoding=encoding, parse_dates=["Data"])
        except UnicodeDecodeError:
            continue
 
# caminho para o arquivo CSV
caminho_arquivo = 'C:\\Users\\grazi\\Downloads\\codes\\Análise de Dados Vendas de Cursos Online.csv'

# carregar o DataFrame
df = carregar_csv(caminho_arquivo)

# exibir as primeiras linhas do DataFrame
print("Primeiras linhas do DataFrame:")
print(df.head())

# exibir as informações básicas do DataFrame, como número de linhas, colunas e tipos de dados
print("Informações básicas do DataFrame:")
print(df.info())