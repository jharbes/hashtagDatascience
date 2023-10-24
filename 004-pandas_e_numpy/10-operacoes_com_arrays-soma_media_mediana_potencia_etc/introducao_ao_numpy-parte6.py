"""
# NumPy

- https://numpy.org/
- O nome NumPy vem de Numerical Python
    - Biblioteca de computação numérica
    - Otimizada para cálculos pesados

    
- No NumPy vamos trabalhar com **arrays**, que são mais rápidos e mais performáticos que listas

    - Arrays são estruturas de dados que guardam itens **do mesmo tipo** (diferente das listas)
        - **["As operações matemáticas que devem ser executadas em arrays seriam extremamente ineficientes se os arrays não fossem homogêneos."](https://numpy.org/doc/stable/user/absolute_beginners.html#whats-the-difference-between-a-python-list-and-a-numpy-array)** 

    - Assim como **listas**, são um conjunto de **elementos ordenados que são mutáveis e de comprimento variável**

    - Além disso, **podemos fazer várias operações com arrays (como multiplicação e soma) que não podem ser feitas com listas** mas são fundamentais para o nosso processo de Ciência de dados

    - Obs: listas são estrutudas de dados do Python e arrays não, **array é uma estrutura de dados própria do numpy**

"""
# Importar o numpy
import numpy as np




"""
- **A importância do NumPy**
    - Vamos supor que temos a venda e comissão (em percentual) de 5 vendedores e queremos saber qual vai ser o salário de cada um deles (para isso precisamos multiplicar a venda pela comissão dividida por 100)

"""
# Venda e comissão
venda_valor = [150000,230000,82000,143000,184000]
comissao = [5,8,8,5,12]

print(type(venda_valor)) # <class 'list'>
print(type(comissao)) # <class 'list'>

venda_valor=np.array(venda_valor)
comissao=np.array(comissao)

salarios=venda_valor*comissao/100
print(salarios) # [ 7500. 18400.  6560.  7150. 22080.]




# Qual o tipo desse dado?
print(type(salarios)) # <class 'numpy.ndarray'>




# Transformando em um array

venda_valor2 = [150000,230000,82000,143000,184000]
comissao2 = [5,8,8,5,12]

# o help imprime uma ajuda sobre o metodo ou atributo
help(np.array)

venda_valor2=np.array(venda_valor2)
comissao2=np.array(comissao2)

print(venda_valor2)
print(comissao2)



# Agora vamos conseguir fazer sendo um array
salarios2=venda_valor2*comissao2/100

print(salarios2)




# Copiando o exemplo
# criamos um array com o 'range' de 0 a 14 e colocamos em 3 linhas e 5 colunas
a = np.arange(15).reshape(3, 5)
print(a)
"""
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
"""

b = np.arange(2,7)
print(b) # [2 3 4 5 6]

c = np.arange(2,10,2)
print(c) # [2 4 6 8]

d = np.array([[1,2,3],[4,5,6]])
print(d)
# [[1 2 3]
#  [4 5 6]]




# Verificando a dimensão desse array
print(a.ndim) # 2
print(b.ndim) # 1
print(c.ndim) # 1
print(d.ndim) # 2




# Verificando a forma do array
print(a.shape) # (3, 5)
print(b.shape) # (5,)
print(c.shape) # (4,)
print(d.shape) # (2, 3)




# Verificando o tipo dos dados
print(a.dtype) # int32
print(b.dtype) # int32
print(c.dtype) # int32
print(d.dtype) # int32




# Considerando os 3 arrays abaixo
array1 = np.array([1,2,3,4,5])
array2 = np.array([1,2,3,4.5,5])
array3 = np.array([1,2,3,'4',5])


# Verificando o tipo de dado do primeiro array e retornando esse array
print(array1.dtype) # int32 
print(array1) # [1 2 3 4 5]


# Fazendo a mesma coisa para o array2
print(array2.dtype) # float64
print(array2) # [1.  2.  3.  4.5 5. ]


# E para o array3
print(array3.dtype) # <U11
print(array3) # ['1' '2' '3' '4' '5']




# Criando um array qualquer de números inteiros
vetor1=np.array([1,2,3,4,5])
print(vetor1) # [1 2 3 4 5]


# Criando um segundo array com valores decimais
vetor2=np.array([1,2,3,4.7,5])
print(vetor2) # [1.  2.  3.  4.7 5. ]


# Criando um array apenas de valores zero
vetor3=np.array([0,0,0,0])

# aqui forçamos o tipo para ser int32 (o default é float)
vetor4=np.zeros((4,4),dtype=np.int32)

vetor5=np.ones((2,2),dtype=np.float32)

# dtype é opcional
vetor6=np.zeros((4,))

print(vetor3) # [0 0 0 0]
print(vetor4)
"""
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
"""

print(vetor5)
"""
[[1. 1.]
 [1. 1.]]
"""

print(vetor6) # [0. 0. 0. 0.]




# Criando um array com uma lista de valores
vetor7=np.arange(101)

print(vetor7)
"""
[  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53
  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71
  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89
  90  91  92  93  94  95  96  97  98  99 100]
"""


# Adicionando um intervalo para o array
vetor8=np.arange(15,26)

print(vetor8) # [15 16 17 18 19 20 21 22 23 24 25]




# Adicionando um "passo" para o array
vetor9=np.arange(5,100,5)

print(vetor9) # [ 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]




# Criando um novo array com os valores igualmente espaçados (utilizando o linspace)
# O primeiro argumento será o primeiro elemento, o segundo será o ultimo elemento e o terceiro argumento será o numero de elementos desejados nesse intervalo
vetor10=np.linspace(5,10,4)

print(vetor10) # [ 5.          6.66666667  8.33333333 10.        ]




# - O array de uma dimensão é o que chamamos de vetor e o de duas dimensões de matriz

# Vamos considerar esses dados abaixo
dados_venda = np.array([[150000,230000,82000,143000,184000],[5,8,8,5,12]])

# Verificando a forma do array
print(dados_venda.shape) # (2, 5)

# Verificando o tipo dos dados
print(dados_venda.dtype) # int32




# Agora considerando esses novos dados
dados_venda1 = np.array([['Lucas','Bia','Jean','Gabi','Pedro'],[150000,230000,82000,143000,184000]])

# Verificando a forma do array
print(dados_venda1)
"""
[['Lucas' 'Bia' 'Jean' 'Gabi' 'Pedro']
 ['150000' '230000' '82000' '143000' '184000']]
"""

# Verificando o tipo dos dados
# observe que o dado mais generico sera escolhido como o tipo de dado (todos os elementos do array tem que ter o mesmo tipo)
print(dados_venda1.dtype) # <U11




# - **Assim como listas, também podemos buscar elementos no array utilizando seus índices**
    # - https://numpy.org/doc/stable/user/basics.indexing.html

# Utilizando o mesmo array do exemplo
array_busca = np.arange(15).reshape(3, 5)

print(array_busca)
"""
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
"""


# Buscando a primeira linha
print(array_busca[0]) # [0 1 2 3 4]


# Na primeira linha, buscando o elemento de índice 3
print(array_busca[0,3]) # 3
print(array_busca[0][3]) # 3


# Buscando os elementos de índice 1 a 3 (incluindo o 3) na primeira linha
print(array_busca[0,1:4]) # [1 2 3]
print(array_busca[0][1:4]) # [1 2 3]


# Buscando apenas os valores maiores que 5
print(array_busca > 5)
"""
[[False False False False False]
 [False  True  True  True  True]
 [ True  True  True  True  True]]
"""

print(array_busca[array_busca > 5]) # [ 6  7  8  9 10 11 12 13 14]


# Buscando valores maiores que 5 E (&) menores que 11
print(array_busca[(array_busca > 5) & (array_busca < 11)]) # [ 6  7  8  9 10]

print(array_busca[(array_busca > 5) | (array_busca < 11)]) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]


# Visualizando o array
novo_array=array_busca[(array_busca > 5) & (array_busca < 11)]

print(novo_array) # [ 6  7  8  9 10]




# - **Operações com array**
    # - https://numpy.org/doc/stable/user/absolute_beginners.html#basic-array-operations

# Considerando o array abaixo
dados = np.arange(6).reshape(2, 3)

print(dados)
"""
[[0 1 2]
 [3 4 5]]
"""



# Somando todos os valores
print(np.sum(dados)) # 15



# Somando apenas os valores da linha

# soma os valores da primeira linha
print(np.sum(dados[0])) # 3

# soma os valores da segunda linha
print(np.sum(dados[1])) # 12

# soma os valores de cada uma das linhas
print(np.sum(dados,axis=1)) # [ 3 12]

# soma os valores de cada uma das colunas
print(np.sum(dados, axis=0)) # [3 5 7]




# Fazendo a soma acumulada desses valores
print(np.cumsum(dados,axis=1))
"""
[[ 0  1  3]
 [ 3  7 12]]
"""

print(dados.cumsum(axis=1))
"""
[[ 0  1  3]
 [ 3  7 12]]
"""



# Somando apenas os valores da coluna
print(np.sum(dados, axis=0)) # [3 5 7]

print(dados.sum(axis=0)) # [3 5 7]



# Somando 1 em todos os valores
print(dados + 1)
"""
[[1 2 3]
 [4 5 6]]
"""



# Multiplicando 2 em todos os valores do array
print(dados * 2)
"""
[[ 0  2  4]
 [ 6  8 10]]
"""



# Verificando o menor valor desse array
print(np.min(dados)) # 0

print(np.min(dados,axis=0)) # [0 1 2]

print(dados.min(axis=1)) # [0 3]



# E agora o maior valor
print(np.max(dados)) # 5

print(np.max(dados,axis=0)) # [3 4 5]

print(dados.max(axis=1)) # [2 5]



# Calculando a média da primeira linha
print(dados[0].mean()) # 1.0
print(dados.mean(axis=1)[0]) # 1.0

# E da segunda linha
print(dados[1].mean()) # 4.0
print(dados.mean(axis=1)[1]) # 4.0



# Verificando a mediana
print(np.median(dados)) # 2.5




# - Inclusive podemos fazer operação entre arrays

# Considerando esses 2 arrays
array1 = np.array([1,2,3,4,5])
array2 = np.array([7,8,9,10,11])



# Somando os arrays
print(array1 + array2) # [ 8 10 12 14 16]



# Multiplicando esses arrays
print(array1 * array2) # [ 7 16 27 40 55]



# Potência
print(array1 ** array2) # [       1      256    19683  1048576 48828125]