import pandas as pd

lista = [2,5,8,-1,3,-5,-7, 12]

lista_1 = pd.Series(lista)

print (lista_1)
#Valor absoluto
print (lista_1.abs())
print (lista_1.agg(max))
print (lista_1.agg(min))
print (lista_1.agg(abs))

#Ejercicio 1 

from math import sqrt
print (lista_1.agg(abs).agg(sqrt))
print (lista_1.agg(abs).agg(hex))

#Ejercicio 2

def cuadrado (y):
    return y*y
print (lista_1.agg(cuadrado))
print (lista_1.agg(lambda x: x**3))

import numpy as np
print (lista_1.agg(np.sin))
print (lista_1.agg(np.cbrt))