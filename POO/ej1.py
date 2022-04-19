from msilib.schema import Class
from re import L
class Perro:
    def _init_ (self):
        self._alimento = 0
        self._caricias = 0

    def energia (self):
        return self._alimento + (self._caricias *10)
    
    def comer (self, gramos):
        self._alimento += gramos

    def acariciar (self):
        self._caricias += 1
    
    def esta_debil(self):
        self._alimento <2