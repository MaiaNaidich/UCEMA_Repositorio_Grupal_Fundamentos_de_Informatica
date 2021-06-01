# Realizá un programa que verifique si una columna dada se encuentra presente en un DataFrame.
import pandas as pd
def verif_columna(dataframe, columna):
    if columna in dataframe:
        print("esta presente")
