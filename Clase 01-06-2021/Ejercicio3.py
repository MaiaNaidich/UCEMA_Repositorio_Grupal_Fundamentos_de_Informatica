df_vacio=pd.DataFrame()
def agregar_columna(header,datos):
  df_vacio[header]=datos
def agregar_fila(index,datos):
  df_vacio.loc[index]=datos

agregar_columna("Nombre",["Máximo","Maia","Mateo","Valentina","Sofía"])
agregar_columna("Apellido",["Cabezas Fernández","Naidich","Sceia","Kelly","Gramuglia"])
agregar_fila(5,["Juana","Llaneza Manzo"])

df_vacio