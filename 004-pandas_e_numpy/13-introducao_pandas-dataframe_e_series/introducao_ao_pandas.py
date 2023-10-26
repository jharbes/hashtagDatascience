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




"""
### DataFrame e Series

**Essa base que acabamos de importar é um DataFrame!**
"""
type(base) # pandas.core.frame.DataFrame



# **Também podemos criar um novo DataFrame usando um dicionário:**
dic = {
    "funcionarios": ['Lucas','Bia','Jean','Gabi','Pedro'],
    "venda_valor": [150000,230000,82000,143000,184000],
    "comissao": [5,8,8,5,12]
}

type(dic) # dict

print(dic)
"""
{'funcionarios': ['Lucas', 'Bia', 'Jean', 'Gabi', 'Pedro'],
 'venda_valor': [150000, 230000, 82000, 143000, 184000],
 'comissao': [5, 8, 8, 5, 12]}
"""


# Transformando esse dicionário em um DataFrame
base_dic = pd.DataFrame(dic)

print(base_dic)
"""
  funcionarios  venda_valor  comissao
0        Lucas       150000         5
1          Bia       230000         8
2         Jean        82000         8
3         Gabi       143000         5
4        Pedro       184000        12
"""


# Verificando o tipo do dado
type(base_dic) # pandas.core.frame.DataFrame