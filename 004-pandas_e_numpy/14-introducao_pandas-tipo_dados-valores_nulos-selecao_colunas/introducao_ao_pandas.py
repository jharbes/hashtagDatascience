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




"""
**Cada coluna do DataFrame é uma Series, assim:

series = DataFrame["coluna"]

"""
series_funcionarios = base_dic["funcionarios"]

print(series_funcionarios)
"""
0    Lucas
1      Bia
2     Jean
3     Gabi
4    Pedro
Name: funcionarios, dtype: object
"""


print(series_funcionarios.index) # RangeIndex(start=0, stop=5, step=1)

print(series_funcionarios.values) # ['Lucas' 'Bia' 'Jean' 'Gabi' 'Pedro']


print(type(series_funcionarios)) # <class 'pandas.core.series.Series'>



"""
**Para filtrar uma única coluna e continuar sendo um DataFrame, podemos fazer:

series = DataFrame[["coluna"]]

"""
dataframe_funcionarios = base_dic[["funcionarios"]]

print(dataframe_funcionarios)
"""
  funcionarios
0        Lucas
1          Bia
2         Jean
3         Gabi
4        Pedro
"""


print(type(dataframe_funcionarios)) # pandas.core.frame.DataFrame




"""
## Podemos aplicar vários conceitos que vimos no NumPy!

### Assim como o NumPy, ele também mostra as informações gerais

"""
# Mostrando somente o tipo dos dados
print(base.dtypes)
"""
As of                   object
Rank                     int64
Year to Date Rank       object
Last Week Rank          object
Title                   object
Type                    object
Netflix Exclusive       object
Netflix Release Date    object
Days In Top 10           int64
Viewership Score         int64
dtype: object
"""




# Mostrando o tipo de dados e os valores vazios
print(base.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7100 entries, 0 to 7099
Data columns (total 10 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   As of                 7100 non-null   object
 1   Rank                  7100 non-null   int64 
 2   Year to Date Rank     7100 non-null   object
 3   Last Week Rank        7100 non-null   object
 4   Title                 7100 non-null   object
 5   Type                  7100 non-null   object
 6   Netflix Exclusive     4599 non-null   object
 7   Netflix Release Date  7100 non-null   object
 8   Days In Top 10        7100 non-null   int64 
 9   Viewership Score      7100 non-null   int64 
dtypes: int64(3), object(7)
memory usage: 554.8+ KB

"""




# True = 1, False = 0, usamos essa logica para contar o numero de valores nulos da tabela
print(False + False + False)
print(True + False + False)
print(True + True + False)
print(True + True + True)


# Contando os valores vazios por coluna
print(base.isnull().sum())
"""
As of                      0
Rank                       0
Year to Date Rank          0
Last Week Rank             0
Title                      0
Type                       0
Netflix Exclusive       2501
Netflix Release Date       0
Days In Top 10             0
Viewership Score           0
dtype: int64
"""


# Mostrando a tabela e onde estão os valores vazios
print(base.isnull())




"""
### Podemos limitar a base escolhendo apenas as colunas que queremos trabalhar

- Vamos falar disso agora para depois voltarmos na parte de estatística

"""

# Antes de falarmos de estatística, vamos precisar selecionar apenas as colunas que vamos trabalhar para evitar esse erro
# com essa funcao esperamos calcular a media das colunas, porem nem todas elas sao numericas, portanto haverá erro na tentativa de calcular media das colunas nao numericas
base.mean()




# Podemos usar o nome da coluna entre aspas
print(base["Title"])
# ou
print(base.Title)
"""
0       Tiger King: Murder, Mayhem …
1                              Ozark
2                       All American
3                       Blood Father
4                       The Platform
                    ...             
7095             Worst Roommate Ever
7096               Vikings: Valhalla
7097                         Shooter
7098                         Shrek 2
7099                           Shrek
Name: Title, Length: 7100, dtype: object
"""