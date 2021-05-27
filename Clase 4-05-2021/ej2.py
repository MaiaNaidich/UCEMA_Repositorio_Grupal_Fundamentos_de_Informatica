class Golondrina:
    def __init__(self, energia):
        self.energia = energia    
                              
    def comer_alpiste(self, gramos):
        self.energia += 4 * gramos
    
    def volar_en_circulos(self):
        self.volar(0)
    
    def volar(self, kms):
        self.energia -= 10 + kms
    
    def esta_debil(self):
        if self.energia <= 10:
            return True
            else:
                return False

    def saciar(self):
        self.comer_alpiste(100)
    
    def esta_en_equilibrio(self):
        if 150 <= self.energia <= 300:
            return True
            else:
                return False
