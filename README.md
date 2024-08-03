![Código Certo Coders](68747470733a2f2f757466732e696f2f662f33623233343065382d353532332d346163612d613534392d3036383866643037343530652d6a346564752e6a666966.jpeg)

# Trilha CódigoCerto Analista de Dados Júnior

**Desafio: Este projeto tem como objetivo realizar uma análise básica de dados utilizando Python, explorando um conjunto de dados sugerido para extrair insights simples através de estatísticas descritivas e visualizações gráficas.**

## Descrição do Projeto

O projeto consiste na análise de um conjunto de dados sobre a venda de cursos. O objetivo é explorar os dados, calcular estatísticas descritivas, gerar visualizações e obter insights. As análises realizadas ajudam a entender o desempenho das vendas dos cursos, identificar tendências e fazer recomendações baseadas nos dados.

## Requisitos Funcionais

1. **Carregamento de Dados**
- **Objetivo**: carregar o arquivo com os dados em formato CSV no Visual Code Studio.
- **Como Fazer**: importar a biblioteca Pandas, definir a função, ler o arquivo CSV por meio de codificações, carregar o caminho para o arquivo CSV e carregar o DataFrame.
- **Descrição do código Python**: 

```
import pandas as pd

def carregar_csv(caminho_arquivo):

    codificacoes = ['utf-8', 'latin1', 'windows-1252']
    for encoding in codificacoes:
        try:
            return pd.read_csv(caminho_arquivo, encoding=encoding, parse_dates=["Data"])
        except UnicodeDecodeError:
            continue
 
caminho_arquivo = 'C:\\Users\\grazi\\Downloads\\codes\\Análise de Dados Vendas de Cursos Online.csv'

df = carregar_csv(caminho_arquivo)
```

2. **Exploração de Dados**
- **Objetivo**: Exibir as primeiras linhas e informações básicas dos dados.
- **Como Fazer**: importar a biblioteca Pandas, definir a função, ler o arquivo CSV por meio de codificações, carregar o caminho para o arquivo CSV, carregar o DataFrame, exibir as primeiras linhas do DataFrame e exibir as informações básicas do DataFrame, como número de linhas, colunas e tipos de dados.
- **Descrição do código Python**: 

```
import pandas as pd

def carregar_csv(caminho_arquivo):

    codificacoes = ['utf-8', 'latin1', 'windows-1252']
    for encoding in codificacoes:
        try:
            return pd.read_csv(caminho_arquivo, encoding=encoding, parse_dates=["Data"])
        except UnicodeDecodeError:
            continue
 
caminho_arquivo = 'C:\\Users\\grazi\\Downloads\\codes\\Análise de Dados Vendas de Cursos Online.csv'

df = carregar_csv(caminho_arquivo)

print("Primeiras linhas do DataFrame:")
print(df.head())

print("Informações básicas do DataFrame:")
print(df.info())
```

3. **Estatísticas Descritivas**
- **Objetivo**: Calcular e exibir estatísticas descritivas básicas para colunas numéricas, como média, mediana, mínimo, máximo e desvio padrão.
- **Como Fazer**: importar a biblioteca Pandas, definir a função, ler o arquivo CSV por meio de codificações, carregar o caminho para o arquivo CSV, carregar o DataFrame, exibir as primeiras linhas do DataFrame e exibir as informações básicas do DataFrame, como número de linhas, colunas e tipos de dados, calcular a receita total das vendas, identificar o curso com o maior número de vendas e estatísticas descritivas básicas.
- **Descrição do código Python**: 

```
import pandas as pd

def carregar_csv(caminho_arquivo):

    codificacoes = ['utf-8', 'latin1', 'windows-1252']
    for encoding in codificacoes:
        try:
            return pd.read_csv(caminho_arquivo, encoding=encoding, parse_dates=["Data"])
        except UnicodeDecodeError:
            continue
 
caminho_arquivo = 'C:\\Users\\grazi\\Downloads\\codes\\Análise de Dados Vendas de Cursos Online.csv'

df = carregar_csv(caminho_arquivo)

df['Receita'] = df['Quantidade de Vendas'] * df['Preço Unitário']
receita_total = df['Receita'].sum()
print(f'\nA receita total gerada pelas vendas é: R${receita_total:.2f}')

curso_mais_vendido = df.loc[df['Quantidade de Vendas'].idxmax()]
print(f'O curso com o maior número de vendas é: {curso_mais_vendido["Nome do Curso"]}')
print(f'O número de vendas foi de: {curso_mais_vendido["Quantidade de Vendas"]}')
print(f'A receita gerada foi de : R${curso_mais_vendido["Receita"]:.2f}')

estatisticas = df[['Quantidade de Vendas', 'Preço Unitário', 'Receita']].describe().T  
estatisticas['Mediana'] = df[['Quantidade de Vendas', 'Preço Unitário', 'Receita']].median()
estatisticas = estatisticas[['mean', '50%', 'min', 'max', 'std']]  
estatisticas.columns = ['Média', 'Mediana', 'Mínimo', 'Máximo', 'Desvio Padrão']
print("Estatísticas Descritivas Básicas:")
print(estatisticas)
```

4. **Visualização de Dados**
- **Objetivo**: Crie pelo menos dois tipos de gráficos utilizando bibliotecas como Matplotlib ou Seaborn, como gráficos de barras para contagem de categorias e gráficos de dispersão para relação entre variáveis.
- **Gráficos de Barras**: Demostrar a contagem de vendas por curso.



- **Gráficos de Dispersão**: Demostrar a relação entre data e receita.
- **Como Fazer**: importar as bibliotecas Pandas, Matplotlib e Seaborn, carregar o caminho para o arquivo CSV, ler o arquivo com diferentes codificações, calcular a receita total, estatísticas descritivas básicas, gráfico de Barras - contagem de vendas por curso, gráfico de dispersão - relação entre data e receita e ajuste da legenda necessário.
- **Descrição do código Python**: 

```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

caminho_arquivo = 'C:\\Users\\grazi\\Downloads\\codes\\Análise de Dados Vendas de Cursos Online.csv'

for encoding in ['utf-8', 'latin1', 'windows-1252']:
    try:
        df = pd.read_csv(caminho_arquivo, encoding=encoding, parse_dates=["Data"])
        break
    except UnicodeDecodeError:
        continue

df['Receita'] = df['Quantidade de Vendas'] * df['Preço Unitário']

estatisticas = df[['Quantidade de Vendas', 'Preço Unitário', 'Receita']].describe().T  
estatisticas['Mediana'] = df[['Quantidade de Vendas', 'Preço Unitário', 'Receita']].median()
estatisticas = estatisticas[['mean', '50%', 'min', 'max', 'std']]
estatisticas.columns = ['Média', 'Mediana', 'Mínimo', 'Máximo', 'Desvio Padrão']
print("Estatísticas Descritivas Básicas:")
print(estatisticas)

plt.figure(figsize=(14, 8))
sns.barplot(x="Quantidade de Vendas", y="Nome do Curso", data=df, estimator=sum, errorbar=None, palette="viridis")
plt.title("Contagem de Vendas por Curso")
plt.xlabel("Quantidade de Vendas")
plt.ylabel("Nome do Curso")
plt.show()

plt.figure(figsize=(12, 6))
scatter_plot = sns.scatterplot(x="Data", y="Receita", data=df, hue="Nome do Curso", palette="viridis", s=100)

plt.title("Relação entre Data e Receita")
plt.xlabel("Data")
plt.ylabel("Receita")
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Nome do Curso')  
plt.tight_layout() 
plt.show()
```

## Desafios Propostos

1. **Calcule a Receita Total Gerada pela Venda dos Cursos**
- **Objetivo**: Determinar a receita total gerada pela venda dos produtos.
- **Como Fazer**: importar a biblioteca Pandas, definir a função, ler o arquivo CSV por meio de codificações, carregar o caminho para o arquivo CSV, carregar o DataFrame, exibir as primeiras linhas do DataFrame e exibir as informações básicas do DataFrame, como número de linhas, colunas e tipos de dados e calcular a receita total das vendas.
- **Descrição do código Python**: 

```
import pandas as pd

def carregar_csv(caminho_arquivo):

    codificacoes = ['utf-8', 'latin1', 'windows-1252']
    for encoding in codificacoes:
        try:
            return pd.read_csv(caminho_arquivo, encoding=encoding, parse_dates=["Data"])
        except UnicodeDecodeError:
            continue
 
caminho_arquivo = 'C:\\Users\\grazi\\Downloads\\codes\\Análise de Dados Vendas de Cursos Online.csv'

df = carregar_csv(caminho_arquivo)

df['Receita'] = df['Quantidade de Vendas'] * df['Preço Unitário']
receita_total = df['Receita'].sum()
print(f'\nA receita total gerada pelas vendas é: R${receita_total:.2f}')
```

2. **Identificar o Curso com o Maior Número de Vendas**
- **Objetivo**: Identificar qual o curso teve o maior número de vendas.
- **Como Fazer**: importar a biblioteca Pandas, definição da função, tentando ler o arquivo CSV por meio de codificações, carregar o caminho para o arquivo CSV, carregar o DataFrame, calcular a receita total das vendas e identificar o curso com o maior número de vendas.
- **Descrição do código Python**: 

```
import pandas as pd

def carregar_csv(caminho_arquivo):

    codificacoes = ['utf-8', 'latin1', 'windows-1252']
    for encoding in codificacoes:
        try:
            return pd.read_csv(caminho_arquivo, encoding=encoding, parse_dates=["Data"])
        except UnicodeDecodeError:
            continue
 
caminho_arquivo = 'C:\\Users\\grazi\\Downloads\\codes\\Análise de Dados Vendas de Cursos Online.csv'

df = carregar_csv(caminho_arquivo)

df['Receita'] = df['Quantidade de Vendas'] * df['Preço Unitário']
receita_total = df['Receita'].sum()
print(f'\nA receita total gerada pelas vendas é: R${receita_total:.2f}')

curso_mais_vendido = df.loc[df['Quantidade de Vendas'].idxmax()]
print(f'O curso com o maior número de vendas é: {curso_mais_vendido["Nome do Curso"]}')
print(f'O número de vendas foi de: {curso_mais_vendido["Quantidade de Vendas"]}')
print(f'A receita gerada foi de : R${curso_mais_vendido["Receita"]:.2f}')
```

3. **Visualize a Distribuição das Vendas ao Longo do Tempo**: Apresentado nos requisitos funcionais.

## Código Python completo com explicações de cada etapa:

```
#Importar as bibliotecas Pandas, Matplotlib e Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#definição da função
def carregar_csv(caminho_arquivo):

#tentando ler o arquivo CSV por meio de codificações 
    codificacoes = ['utf-8', 'latin1', 'windows-1252']
    for encoding in codificacoes:
        try:
            return pd.read_csv(caminho_arquivo, encoding=encoding, parse_dates=["Data"])
        except UnicodeDecodeError:
            continue
 
#caminho para o arquivo CSV
caminho_arquivo = 'C:\\Users\\grazi\\Downloads\\codes\\Análise de Dados Vendas de Cursos Online.csv'

#carregar o DataFrame
df = carregar_csv(caminho_arquivo)

#calcular a receita total das vendas
df['Receita'] = df['Quantidade de Vendas'] * df['Preço Unitário']
receita_total = df['Receita'].sum()
print(f'\nA receita total gerada pelas vendas é: R${receita_total:.2f}')

#identificar o curso com o maior número de vendas
curso_mais_vendido = df.loc[df['Quantidade de Vendas'].idxmax()]
print(f'O curso com o maior número de vendas é: {curso_mais_vendido["Nome do Curso"]}')
print(f'O número de vendas foi de: {curso_mais_vendido["Quantidade de Vendas"]}')
print(f'A receita gerada foi de : R${curso_mais_vendido["Receita"]:.2f}')

#estatísticas descritivas básicas
estatisticas = df[['Quantidade de Vendas', 'Preço Unitário', 'Receita']].describe().T  
estatisticas['Mediana'] = df[['Quantidade de Vendas', 'Preço Unitário', 'Receita']].median()
estatisticas = estatisticas[['mean', '50%', 'min', 'max', 'std']]  
estatisticas.columns = ['Média', 'Mediana', 'Mínimo', 'Máximo', 'Desvio Padrão']
print("Estatísticas Descritivas Básicas:")
print(estatisticas)

#Gráfico de Barras - Contagem de Vendas por Curso
plt.figure(figsize=(14, 8))
sns.barplot(x="Quantidade de Vendas", y="Nome do Curso", data=df, estimator=sum, errorbar=None, palette="viridis")
plt.title("Contagem de Vendas por Curso")
plt.xlabel("Quantidade de Vendas")
plt.ylabel("Nome do Curso")
plt.show()

#Gráfico de Dispersão - Relação entre Data e Receita
plt.figure(figsize=(12, 6))
scatter_plot = sns.scatterplot(x="Data", y="Receita", data=df, hue="Nome do Curso", palette="viridis", s=100)

#Ajuste da legenda necessário
plt.title("Relação entre Data e Receita")
plt.xlabel("Data")
plt.ylabel("Receita")
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Nome do Curso')  
plt.tight_layout() 
```

## Análises Realizadas

1. **Receita Total**: A receita total foi calculada somando a receita de todas as transações.
2. **Estatísticas Descritivas**: Estatísticas básicas foram calculadas para colunas numéricas, fornecendo uma visão geral do desempenho dos cursos.
3. **Curso com Mais Vendas**: Identificado o curso com o maior número de vendas.
4. **Visualizações**:
- **Gráfico de Barras**: Demostrou a contagem total de vendas para cada curso, ajudando a identificar quais cursos têm mais vendas.
- **Gráfico de Dispersão**: Demostrou a relação entre a receita e a data, facilitando a visualização de como as vendas variaram ao longo do tempo.

## Insights Obtidos

1. **Desempenho dos Cursos**: Identificação de quais cursos são mais populares com base no número de vendas.
2. **Tendências Temporais**: Visualização de como as vendas se distribuíram ao longo do tempo, ajudando a identificar tendências sazonais ou outros padrões temporais.

Este projeto fornece uma análise abrangente dos dados de vendas de cursos, com o objetivo de oferecer insights valiosos para melhorar as estratégias de vendas e marketing.

## Projeto apresentado como Trilha Inicial de Analista de Dados Júnior no Projeto CódigoCerto.

