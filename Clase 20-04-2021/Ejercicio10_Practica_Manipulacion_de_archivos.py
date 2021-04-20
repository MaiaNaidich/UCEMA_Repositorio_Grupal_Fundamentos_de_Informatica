#Ejercicio 10
#Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.

carpeta="F:\\Fundamentos_de_Informática\\Textos"
texto_destino="F:\\Fundamentos_de_Informática\\Textos\\Texto_Destino"
texto_a_combinar=""
with open(carpeta,"r") as carpeta:
    for texto in carpeta:
        texto_leido=texto.read()
        texto_a_combinar+=texto_leido
        texto_a_combinar+="\n"
    print(texto_a_combinar)
with open(texto_destino,"w") as texto_destino:
    texto_destino.write(texto_a_combinar)