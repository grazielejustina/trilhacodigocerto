#Estatísticas Descritivas: Calcular e exibir estatísticas descritivas básicas para colunas numéricas do conjunto de dados, como média, mediana, mínimo, máximo e desvio padrão.

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

# calcular a receita total das vendas
df['Receita'] = df['Quantidade de Vendas'] * df['Preço Unitário']
receita_total = df['Receita'].sum()
print(f'\nA receita total gerada pelas vendas é: R${receita_total:.2f}')

# identificar o curso com o maior número de vendas
curso_mais_vendido = df.loc[df['Quantidade de Vendas'].idxmax()]
print(f'O curso com o maior número de vendas é: {curso_mais_vendido["Nome do Curso"]}')
print(f'O número de vendas foi de: {curso_mais_vendido["Quantidade de Vendas"]}')
print(f'A receita gerada foi de : R${curso_mais_vendido["Receita"]:.2f}')

# estatísticas descritivas básicas
estatisticas = df[['Quantidade de Vendas', 'Preço Unitário', 'Receita']].describe().T  
estatisticas['Mediana'] = df[['Quantidade de Vendas', 'Preço Unitário', 'Receita']].median()
estatisticas = estatisticas[['mean', '50%', 'min', 'max', 'std']]  
estatisticas.columns = ['Média', 'Mediana', 'Mínimo', 'Máximo', 'Desvio Padrão']
print("Estatísticas Descritivas Básicas:")
print(estatisticas)
