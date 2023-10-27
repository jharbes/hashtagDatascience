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