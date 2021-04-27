class contador:
    def __init__(self, valor_inicial):
        self.valor=valor_inicial
    
    def inc(self):
        self.valor+=1
    
    def dis(self):
        self.valor-=1
    
    def reset(self):
        self.valor=0
    
    def valorActual(self):
        self.valor
    
    def valorNuevo(self, valor_nuevo):
        self.valor=valor_nuevo

Numero = contador(20)