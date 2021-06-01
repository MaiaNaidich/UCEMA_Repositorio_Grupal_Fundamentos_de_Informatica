#!/usr/bin/env python
# coding: utf-8

# Ejercicio 2
# 
# Escribí un programa que guarde en una lista una columna de un DataFrame.

# In[1]:


import pandas as pd
paises_latam = pd.DataFrame(data ={"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Lengua oficial primaria": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}, index = [1,2,3,4,5,6])

df = pd.DataFrame(paises_latam, columns= ['Pais', 'Lengua oficial primaria'])
lista_paises = df.values.tolist()

print(lista_paises)


# In[ ]:




