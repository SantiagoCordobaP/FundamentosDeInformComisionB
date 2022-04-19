from tkinter.tix import NoteBook
from tkinter.ttk import Notebook
from Fundamentos_informaticaANA.POO.Teoria.materiales.aves import Golondrina


class Golondrina:
    def _init_ (self,energia):
        self.energia = energia
    def comer_alpiste(self,gramos):
        self.energia+=4 *gramos
    def volar_en_circulos (self):
        self.volar(0)