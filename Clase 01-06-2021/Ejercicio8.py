#Ejercicio 8
#Realizá un programa que dado dos DataFrames genere otro que contenga solo las columnas en común.
import pandas as pd

Dic1 = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
Dic2 = {1: [6, 7, 8, 9], 2:[10, 11, 12, 13], 4: [14, 15, 16, 17]}
df1 = pd.DataFrame(Dic1)
df2 = pd.DataFrame(Dic2)

concatenados = pd.concat([df1, df2], axis=0)
print(concatenados.reset_index()) 

