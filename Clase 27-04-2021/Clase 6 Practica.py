#!/usr/bin/env python
# coding: utf-8

# Clase 6 Practica

# Ejercicio 1
# 
# Dada la siguiente clase, identificá la interfaz y el estado de la misma:

# class Perro:
#     def __init__(self):
#         self._alimento = 0
#         self._caricias = 0
# 
#     def energia(self):
#         return self._alimento + (self._caricias * 10)
# 
#     def comer(self, gramos):
#         self._alimento += gramos
# 
#     def acariciar(self):
#         self._caricias += 1
# 
#     def estaDebil(self):
#         return self._caricias < 2

# La interfaz son los mensajes que entiende un objeto, en este caso, la funcion energia, comer, acariciar y la funcion esta debil. Es decir, todos los metodos que tiene dicho objeto.
# 
# Por otro lado, el estado es el atributo dentro de cada constructor. Entonces, este es alimento y caricias.

# Ejercicio 2
# 
# Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.

# In[13]:


class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms
    
  def nosepuedevolar(self, kms):
    if self.energia-(10 + kms)>=0:
        self.energia -= 10 + kms    
  


# Ejercicio 3
# 
# Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

# In[20]:


class Notebook:
    def __init__(self, marca, modelo, precio, numero):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
        self.numero=numero

    def aplicarDescuento(self, numero):
        descuento = (numero/100) * self.precio
        return (self.precio - descuento)


# In[21]:


computadora = Notebook("Asus", "Rog", 500, 500)


# In[23]:


computadora.aplicarDescuento()


# Ejercicio 4
# 
# Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:
# 
# inc()
# 
# dis()
# 
# reset()
# 
# valorActual()
# 
# valorNuevo(nuevoValor)
# 
# Como ejemplo el resultado de ejecutar las siguientes líneas tiene que ser 12 y 2

# In[24]:


class Contador:
    def __init__ (self, inc, dis, reset, valorActual, valorNuevo):
        self.inc=inc
        self.dis=dis
        self.reset=reset
        self.valorActual=valorActual
        self.valorNuevo=valorNuevo
    


# In[ ]:




