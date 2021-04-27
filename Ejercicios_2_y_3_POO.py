#Ejercicio 2
def volar(self, kms):
    if self.energia-(10 + kms)>=0:
        self.energia -= 10 + kms

#Ejercicio 3
class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio

    def desceunto(self, descuento):
        self.precio-=(descuento/100)*precio