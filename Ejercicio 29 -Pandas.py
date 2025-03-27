import pandas as pd

lista = (list (range (1, 55)))
lista_1 = pd.Series(lista)
print (lista_1) 
#obtener primeros elementos de una serie 
print (lista_1.head(11))
#obtener ultimos elementos de uan serie 
print (lista_1.tail(11))