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