class contador:
    def _init_(self, valor):
        self.valor = valor
    
    def inc (self):    
        self.valor +=1

    def dis(self):
        self.valor -= 1  

    def reset(self):
        self.valor =0

    def valor_actual(self):
        print(self.valor)

    def valor_nuevo (self,nuevovalor):
        self.valor = nuevovalor