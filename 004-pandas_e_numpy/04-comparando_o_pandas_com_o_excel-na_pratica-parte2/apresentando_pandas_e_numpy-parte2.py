"""
# NumPy e Pandas


- São **bibliotecas** do Python voltadas para Ciência de Dados


- O **NumPy** é a principal biblioteca de **computação numérica** do Python, **otimizada para calculos pesados** e serve de **base para o Pandas**

    - No NumPy vamos trabalhar com **arrays**, que são estruturas de dados multidimensionais (1D, 2D, 3D,...)
    - Os arrays lembram muito as **listas**, porém com algumas diferenças e várias vantagens na questão de processamento 

    
- O **Pandas** vai ser a biblioteca que vamos utilizar em toda a parte inicial do nosso processo de Ciência de Dados! Além de possuir **alta performance e fácil uso** para trabalharmos com estruturas de dados, possui um **visual muito amigável** ao usuário não técnico

    - Os DataFrames do Pandas lembram muito o excel, popularmente conhecido nas empresas
    - É usado **desde a importação da base até a criação do modelo**, incluindo a **análise e visualização dos dados, tratamentos, agregações, etc**

- Exemplo de um DataFrame do Pandas:

<img src="https://drive.google.com/uc?id=1IXohvu2-EA3QoOFNUB_K9MSIerIwal_B" style='width: 9000px;' />

"""

# - **Podemos começar comparando as funções do Excel com o Pandas**
#   - https://pandas.pydata.org/docs/

# Importando o pandas
import pandas as pd

# Lendo uma base no Pandas

# em excel
df=pd.read_excel(r'C:\Users\jharbes\Documents\GitHub\hashtagDatascience\004-pandas_e_numpy\03-comparando_o_pandas_com_o_excel-na_pratica-parte1\pandas_x_excel.xlsx')

# em json
df2 = pd.DataFrame(
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




# Verificando o tipo desse dado
print(type(df)) # <class 'pandas.core.frame.DataFrame'>
print(df.dtypes,end='\n\n')

print(type(df2)) # <class 'pandas.core.frame.DataFrame'>
print(df2.dtypes)




# Visualizando a base
print(df)

# retorna informacoes sobre a tabela
df.info()

print(df2)

df2.info()




# Visualizando apenas as 5 primeiras linhas
print(df.head())

# Visualiza as ultimas 5 linhas da tabela
print(df.tail())




