import pandas as pd

lista_1 = [2,4,6,8,10]
lista_2 = [1,3,5,7,9]

lista_total_1 = pd.Series(lista_1)
lista_total_2 = pd.Series(lista_2)
print (lista_total_1)
print (lista_total_2)

print (lista_total_1.lt (lista_total_2))
print (lista_total_1.le (lista_total_2))
print (lista_total_1.eq (lista_total_2))
print (lista_total_1.gt (lista_total_2))
print (lista_total_1.ge (lista_total_2))