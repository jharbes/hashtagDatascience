"""
# O Pandas
- https://pandas.pydata.org/


### O DataFrame no pandas
- https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html

"""

# Importando o pandas
import pandas as pd



# Criando um DataFrame
# To manually store data in a table, create a DataFrame. When using a Python dictionary of lists, the dictionary keys will be used as column headers and the values in each list as columns of the DataFrame
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)



# Verificando o DataFrame criado
print(df)
"""
                       Name  Age     Sex
0   Braund, Mr. Owen Harris   22    male
1  Allen, Mr. William Henry   35    male
2  Bonnell, Miss. Elizabeth   58  female
"""



# Visualizando o tipo de dado
print(type(df),end='\n\n') # <class 'pandas.core.frame.DataFrame'>

print(type(df['Age']),end='\n\n') # <class 'pandas.core.frame.DataFrame'>

print(df.dtypes,end='\n\n')
"""
Name    object
Age      int64
Sex     object
dtype: object
"""

print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    3 non-null      object
 1   Age     3 non-null      int64 
 2   Sex     3 non-null      object
dtypes: int64(1), object(2)
memory usage: 200.0+ bytes
None
"""




# Visualizando apenas 1 coluna do DataFrame
# observe que quando separamos apenas UMA coluna do DataFrame ela se transforma em uma SERIES tendo outros atributos e metodos
print(df['Age'],end='\n\n')
"""
0    22
1    35
2    58
Name: Age, dtype: int64
"""

# acessando apenas os indices da coluna

print(df['Age'].index,end='\n\n') # RangeIndex(start=0, stop=3, step=1)

# acessando apenas os valores da coluna

print(df['Age'].values) # [22 35 58]


# Visualizando o tipo de dado
# vendo o tipo da coluna (series)
print(type(df['Age']),end='\n\n') # <class 'pandas.core.series.Series'>




"""
### Importando uma base de dados

- https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html
    - A base de dados está em: `titanic.csv`

"""

# Importando o csv
df2=pd.read_csv(r'C:\Users\jharbes\Documents\GitHub\hashtagDatascience\004-pandas_e_numpy\11-opcional-documentacao_do_pandas\titanic.csv')


# Visualizando a base
print(df2)


# Visualizando as primeiras linhas
print(df2.head())


# Visualizando as 8 primeiras linhas
print(df2.head(8))



# Obtendo o tipo dos dados
print(type(df2),end='\n\n') # <class 'pandas.core.frame.DataFrame'>

print(df2.dtypes)

print(df2.info())



"""
### Selecionando partes do DataFrame

- https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html

"""

# Selecionando apenas 1 coluna
print(df2['Age'],end='\n\n')
"""
0      22.0
1      38.0
2      26.0
3      35.0
4      35.0
       ... 
886    27.0
887    19.0
888     NaN
889    26.0
890    32.0
Name: Age, Length: 891, dtype: float64
"""

type(df2['Age']) # pandas.core.series.Series


# Selecionando 2 ou mais colunas
print(df2[['Age','Name']])




# Fazendo um filtro nas linhas
print(df2['Age'] > 35,end='\n\n') # nesse caso retorna apenas o booleano

print(df2[df2['Age'] > 35],end='\n\n')

print(df2[(df2['Age'] > 35) & df2['Age'] < 60])



# Selecionando linhas e colunas específicas
print(df2.loc[(df2['Age'] > 35) & (df2['Age'] < 60),['Name','Age']])



# Substituindo valores
df2.loc[(df2['Age'] > 35) & (df2['Age'] <= 40),'Age']=40

print(df2.loc[(df2['Age'] > 35) & (df2['Age'] <= 40),'Age'])




"""
# Criando um plot

- https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html

"""

# Criando um plot
df2.plot() # so funciona no jupyter

print(df2.Age)



# Fazendo um scatter plot
df2.plot.scatter(x='Survived',y='Age',alpha=0.5)



# Mostrando um boxplot
df2.plot.box()