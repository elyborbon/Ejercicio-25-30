import pandas as pd 
lista = list(range (1,8))
lista_total_1 = pd.Series(lista)
print (lista_total_1)
print (lista_total_1.where(lista_total_1 > 3))
print (lista_total_1.where(lista_total_1 > 1, -5 ))
print (lista_total_1.where(lista_total_1 >= 2)).dropna()