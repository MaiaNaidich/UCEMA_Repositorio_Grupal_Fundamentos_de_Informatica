path = r"C:\Users\Mateo Sceia\Downloads\Personas_2011.csv"
import pandas as pd
df = pd.read_csv(path, sep=";")
df['seniority_level'].value_counts()
anio2011=df[df["anio"]==2011]
anio2011[anio2011["edad"]==30]
path2 = r"C:\Users\Mateo Sceia\Downloads\ref_categoria_conicet.csv"
df_cat = pd.read_csv(path2, sep=";")
columnas_en_comun = []
for columna in list(df):
    if columna in list(df_cat):
        columnas_en_comun.append(columna)
columnas_en_comun
