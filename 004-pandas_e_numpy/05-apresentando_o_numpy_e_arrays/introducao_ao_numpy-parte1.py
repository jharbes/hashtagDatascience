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