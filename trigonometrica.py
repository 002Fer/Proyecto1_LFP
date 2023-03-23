from abstracto import Expresion
from math import *

class Trigonometrica(Expresion):
    
    def __init__(self, left,tipo,fila, columna):
        self.left=left
        self.tipo=tipo

        super().__init__(fila, columna)

    def operar(self,arbol):
        valorIzquierdo=''
        if self.left !=None:
            valorIzquierdo=self.left.operar(arbol)
        
        if self.tipo.operar(arbol)=='Seno':
            return sin(valorIzquierdo)
        elif self.tipo.operar(arbol)=='Coseno':
            return cos(valorIzquierdo)
        elif self.tipo.operar(arbol) =='Tangente':
            return tan(valorIzquierdo)
        else:
            return None
    
    def getFila(self):
        return super().getFila()
    
    
    def getColumna(self):
        return super().getColumna()