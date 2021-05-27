path = r"C:\Users\Mateo Sceia\Downloads\Personas_2011.csv"
import pandas as pd
df = pd.read_csv(path, sep=";")
df['seniority_level'].value_counts()