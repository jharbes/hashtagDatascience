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

# Ou usar o ponto (só funciona se o nome da coluna nao tiver caracteres espaço no nome)
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




# O value_counts() permite contar os valores de uma coluna:
# base["Coluna"].value_counts()

base["Title"].value_counts()
"""
Title
Cocomelon                       428
Ozark                            85
Cobra Kai                        81
Manifest                         80
The Queenâs Gambit             73
                               ... 
The Office                        1
Animals on the Loose: A You…      1
Dark                              1
The Secret Life of Pets 2         1
Step Up Revolution                1
Name: count, Length: 645, dtype: int64
"""



# Para selecionar mais de uma coluna incluiremos elas em uma lista
lista_colunas = ["Rank","Days In Top 10","Viewership Score"]

print(base[lista_colunas])
"""
      Rank  Days In Top 10  Viewership Score
0        1               9                90
1        2               5                45
2        3               9                76
3        4               5                30
4        5               9                55
...    ...             ...               ...
7095     6              10                81
7096     7              14               100
7097     8               3                 7
7098     9              10                33
7099    10               7                12

[7100 rows x 3 columns]
"""




"""
### Voltando para as informações estatísticas

Obs: Colunas que estejam do tipo objeto não vão ter informações estatísticas!

"""
# Selecionando a base que vamos mostrar informações estatísticas (apenas bases numéricas para que possam haver calculos)
base_estatistica = base[["Rank","Days In Top 10","Viewership Score"]]


print(base_estatistica.head())
"""
   Rank  Days In Top 10  Viewership Score
0     1               9                90
1     2               5                45
2     3               9                76
3     4               5                30
4     5               9                55
"""


print(base_estatistica.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7100 entries, 0 to 7099
Data columns (total 3 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
 0   Rank              7100 non-null   int64
 1   Days In Top 10    7100 non-null   int64
 2   Viewership Score  7100 non-null   int64
dtypes: int64(3)
memory usage: 166.5 KB
None
"""


# Mostrando a média
print(base_estatistica.mean())
"""
Rank                  5.500000
Days In Top 10       24.123662
Viewership Score    122.790141
dtype: float64
"""


# Mostrando a contagem de registros
print(base_estatistica.count())
"""
Rank                7100
Days In Top 10      7100
Viewership Score    7100
dtype: int64
"""


# Mediana
print(base_estatistica.median())
"""
Rank                 5.5
Days In Top 10       7.0
Viewership Score    50.0
dtype: float64
"""


# Desvio Padrão
print(base_estatistica.std())
"""
Rank                  2.872484
Days In Top 10       58.473789
Viewership Score    213.861642
dtype: float64
"""



"""
**Também podemos usar o describe para trazer todo o resumo estatístico:

base.describe()

"""

print(base_estatistica.describe())
"""
              Rank  Days In Top 10  Viewership Score
count  7100.000000     7100.000000       7100.000000
mean      5.500000       24.123662        122.790141
std       2.872484       58.473789        213.861642
min       1.000000        1.000000          1.000000
25%       3.000000        3.000000         19.000000
50%       5.500000        7.000000         50.000000
75%       8.000000       18.000000        128.000000
max      10.000000      428.000000       1474.000000
"""




### Também conseguimos fazer filtros na base

# Filtrando apenas programas que ficaram mais de 100 dias no Top 10
print(base[base["Days In Top 10"] > 100])


# linhas onde o valor da coluna Title for 'Ozark'
print(base[base.Title == "Ozark"])


# Podemos fazer filtros usando E / OU
print(base[(base["Days In Top 10"] > 100) & (base["Title"] != "Cocomelon")])

print(base[(base["Title"] == "Squid Game") | (base["Title"] == "Ozark")])

print(base[base["Title"] == "Squid Game"])




#### Uma forma muito útil de fazer seleção de dados é usando o .loc() ou o .iloc()

# O .loc() (LOCATION) permite fazer a busca da mesma forma acima
print(base.loc[base["Days In Top 10"] > 100])


# Ele também permite usar argumentos lógicos
print(base.loc[(base["Title"] == "Squid Game") | (base["Title"] == "Ozark")])


# Ele permite filtrar colunas de forma muito prática
base.loc[(base["Title"] == "Squid Game") | (base["Title"] == "Ozark"),["As of","Title",'Type']]
"""
           As of  Title     Type
1     2020-04-01  Ozark  TV Show
11    2020-04-02  Ozark  TV Show
21    2020-04-03  Ozark  TV Show
31    2020-04-04  Ozark  TV Show
41    2020-04-05  Ozark  TV Show
...          ...    ...      ...
6954  2022-02-25  Ozark  TV Show
6967  2022-02-26  Ozark  TV Show
6979  2022-02-27  Ozark  TV Show
6986  2022-02-28  Ozark  TV Show
6996  2022-03-01  Ozark  TV Show

[151 rows x 3 columns]
"""




# **Já o .iloc() vai usar o índice para filtrar**

# iloc() - INDICE LOCATION
# Buscando as linhas de 30 (inclusive) a 40 (exclusive)
print(base.iloc[30:40])


# Também posso usar para buscar apenas colunas específicas
print(base.iloc[30:40,[0,4,5]])
"""
         As of                         Title     Type
30  2020-04-04  Tiger King: Murder, Mayhem …  TV Show
31  2020-04-04                         Ozark  TV Show
32  2020-04-04                   Money Heist  TV Show
33  2020-04-04                  All American  TV Show
34  2020-04-04               Coffee & Kareem    Movie
35  2020-04-04     How to Fix a Drug Scandal  TV Show
36  2020-04-04                  The Roommate    Movie
37  2020-04-04                    Nailed It!  TV Show
38  2020-04-04                    Unorthodox  TV Show
39  2020-04-04              The Players Club    Movie
"""




"""
### Por fim, conseguimos fazer gráficos com o Pandas de forma bem simples

    - https://pandas.pydata.org/docs/user_guide/visualization.html

"""
import matplotlib.pyplot as plt

