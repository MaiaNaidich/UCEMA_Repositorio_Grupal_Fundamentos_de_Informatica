#Ejercicio 3
class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def adescuento(self, numero):
        descuento = (numero / 100) * self.precio
        return (self.precio - descuento)

        

computadora = Notebook("HP", "Rey", 500)
