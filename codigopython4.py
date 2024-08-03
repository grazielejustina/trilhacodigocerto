#Visualização de Dados: Crie pelo menos dois tipos de gráficos utilizando bibliotecas como Matplotlib ou Seaborn, como gráficos de barras para contagem de categorias e gráficos de dispersão para relação entre variáveis

# Importar as bibliotecas Pandas, Matplotlib e Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho para o arquivo CSV
caminho_arquivo = 'C:\\Users\\grazi\\Downloads\\codes\\Análise de Dados Vendas de Cursos Online.csv'

# Tentar ler o arquivo com diferentes codificações
for encoding in ['utf-8', 'latin1', 'windows-1252']:
    try:
        df = pd.read_csv(caminho_arquivo, encoding=encoding, parse_dates=["Data"])
        break
    except UnicodeDecodeError:
        continue

# Calcular a receita total
df['Receita'] = df['Quantidade de Vendas'] * df['Preço Unitário']

# Estatísticas descritivas básicas
estatisticas = df[['Quantidade de Vendas', 'Preço Unitário', 'Receita']].describe().T  
estatisticas['Mediana'] = df[['Quantidade de Vendas', 'Preço Unitário', 'Receita']].median()
estatisticas = estatisticas[['mean', '50%', 'min', 'max', 'std']]
estatisticas.columns = ['Média', 'Mediana', 'Mínimo', 'Máximo', 'Desvio Padrão']
print("Estatísticas Descritivas Básicas:")
print(estatisticas)

# Gráfico de Barras - Contagem de Vendas por Curso
plt.figure(figsize=(14, 8))
sns.barplot(x="Quantidade de Vendas", y="Nome do Curso", data=df, estimator=sum, errorbar=None, palette="viridis")
plt.title("Contagem de Vendas por Curso")
plt.xlabel("Quantidade de Vendas")
plt.ylabel("Nome do Curso")
plt.show()

# Gráfico de Dispersão - Relação entre Data e Receita
plt.figure(figsize=(12, 6))
scatter_plot = sns.scatterplot(x="Data", y="Receita", data=df, hue="Nome do Curso", palette="viridis", s=100)

# Ajuste da legenda necessário
plt.title("Relação entre Data e Receita")
plt.xlabel("Data")
plt.ylabel("Receita")
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Nome do Curso')  
plt.tight_layout() 
plt.show()
