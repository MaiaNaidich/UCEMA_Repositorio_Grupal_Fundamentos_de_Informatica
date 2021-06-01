#Ejercicio 7
#Creá un programa que dado un diccionario y una lista añada está última al DataFrame generado a partir del diccionario.

import pandas as pd
Dic = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
Lista = [10, 20, 30, 40, 50]

df = pd.DataFrame(Dic)
'''df.assign(Lista = Lista)
print(df.assign(Lista = Lista)) #Inserta la lista como columna'''

result = df.append(Lista, ignore_index=True )
print(result)

