dict4={"Producto":["Mochila","Mochilita","Bolso","Bolsito","Cartera","Carterita","Billetera","Monedero"],
       "Color":["Azul","Celeste","Negro","Gris","Marrón","Beige","Verde Oscuro","Verde Claro"],
       "Precio":[500,250,1000,750,1500,1250,1100,400]}
df_original=pd.DataFrame(dict4)

df_original

def eliminar_filas(n):
  df_sin_filas=df_original.tail(len(df_original)-n)
  print(df_sin_filas)

eliminar_filas(3)

df_original #se imprime lo mismo que en la fila 6.