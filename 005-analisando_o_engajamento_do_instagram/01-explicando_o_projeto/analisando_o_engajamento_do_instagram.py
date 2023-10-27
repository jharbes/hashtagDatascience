"""
# Analisando o engajamento do Instagram


### O que queremos responder?
- Qual tipo de conteúdo **mais engaja** no Instagram da minha empresa?

- Temos a base de dados do Instagram **desde que o usuário começou a postar na marca até o dia 27/março**

- Ele também dá alguns direcionamentos:

    - Podem ignorar a coluna visualizações, queremos entender apenas curtidas, comentários e interações

    - Tags vazias é que realmente não possuem tag (favor tratar como vazio)

"""

### Vamos importar e visualizar a nossa base

# Importando o pandas
import pandas as pd


# Importar a base em excel
# - Base: 08. Analisando o engajamento no Instagram.xlsx
df=pd.read_excel('08-analisando_o_engajamento_do_instagram.xlsx')


# Visualizando as 5 primeiras linhas
print(df.head())




"""
### Como ele pediu para não considerar a coluna visualizações, vamos retirar essa coluna da base

O .drop() permite apagar uma coluna ou linha da base:
base.drop(nome_coluna,axis=1)

- O axis = 1 se refere a coluna, enquanto axis = 0 se refere a linha

- Devemos passar o nome da coluna que queremos apagar da base

- Em caso de mais de 1 coluna, passamos a lista entre colchetes

"""

# Apagando a coluna "Visualizações"
df=df.drop("Visualizações",axis=1)


# Visualizando novamente as 5 primeiras linhas
print(df.head())


# Visualizando as 5 últimas linhas
print(df.tail())


# Tamanho da base
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 52 entries, 0 to 51
Data columns (total 9 columns):
 #   Column       Non-Null Count  Dtype         
---  ------       --------------  -----         
 0   Tipo         52 non-null     object        
 1   Data         52 non-null     datetime64[ns]
 2   Curtidas     52 non-null     int64         
 3   Comentários  52 non-null     int64         
 4   Tags         44 non-null     object        
 5   Pessoas      52 non-null     object        
 6   Campanhas    52 non-null     object        
 7   Carrossel    8 non-null      object        
 8   Interacoes   52 non-null     int64         
dtypes: datetime64[ns](1), int64(3), object(5)
memory usage: 3.8+ KB
None
"""


# Se a base for pequena, o display mostra a base completa
print(df)