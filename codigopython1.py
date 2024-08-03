#Carregamento de Dados: Implemente a funcionalidade para carregar um conjunto de dados em formato CSV ou outro formato simples suportado pelo Python.

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
 
# Caminho para o arquivo CSV
caminho_arquivo = 'C:\\Users\\grazi\\Downloads\\codes\\Análise de Dados Vendas de Cursos Online.csv'

# Carregar o DataFrame
df = carregar_csv(caminho_arquivo)

