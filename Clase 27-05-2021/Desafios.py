path = r"C:\Users\Mateo Sceia\Downloads\Personas_2011.csv"
import pandas as pd
df = pd.read_csv(path, sep=";")
df['seniority_level'].value_counts()

#Desafío III: averiguá para qué sirve cada uno de los métodos y qué parámetros podés pasarseles. ¡Esta información nos será útil para más adelante!
'''
- set_index(): es un método para establecer una lista, una serie o un marco de datos 
como índice de un marco de datos. La columna de índice también se puede configurar mientras se crea un marco de datos.
- tail(): se usa para obtener las últimas n filas. Esta función devuelve las últimas n filas del objeto según la posición
- fillna () se usa para completar los valores NA / NaN usando el método especificado.
- dropna () se usa para devolver una nueva serie con los valores faltantes eliminados
- notna () se utiliza para detectar valores existentes (no perdidos).Devuelve un objeto booleano del mismo tamaño que indica si los valores
no son NA. Los valores que no faltan se asignan a True.
- head () se usa para obtener las primeras n filas. Esta función devuelve las primeras n filas del objeto según la posición.
- escribe()se utiliza para ver algunos detalles estadísticos básicos como percentil, media, estándar, etc. de un marco de datos o una serie de valores numéricos.
- sample()se utiliza para generar una fila o columna aleatoria de muestra a partir del marco de datos del llamador de funciones.
- corr()se usa para encontrar la correlación por pares de todas las columnas en el marco de datos. Todos los navalores se excluyen automáticamente. 
Para cualquier columna de tipo de datos no numéricos en el marco de datos, se ignora
- hist() generará un gráfico de histograma que muestra la distribución de valores dentro de su serie
'''