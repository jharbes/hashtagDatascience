"""
# Pandas


- Alta performance e fácil uso para trabalhar com dados

- Tem muitas coisas que lembram o Excel

- O DataFrame é usado em várias outras bibliotecas de Ciência de Dados
- https://pandas.pydata.org/

- O Pandas vai desde a importação da base, passando por toda a análise exploratória até a exibição de gráficos

"""
# Importando o pandas
import pandas as pd



"""
### Conseguimos importar praticamente todas as bases de dados usando o pandas
"""
base = pd.read_csv("07_pandas.csv")



### E também visualizar todas as informações sobre essa base
# Visualizando as 5 primeiras linhas
print(base.head())

# Visualizando as 15 primeiras linhas
print(base.head(15))



# Visualizando as 5 últimas linhas
print(base.tail())



# Tamanho da base
base.shape # (7100, 10)



# Visualizando primeiras e últimas linhas e tamanho da base (display funciona apenas no jupyter)
# display(base)
print(base)