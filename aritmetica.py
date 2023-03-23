from abstracto import Expresion

class Aritmetica(Expresion):

    def __init__(self, left, right, tipo, fila, columna):
        self.left= left
        self.right=right
        self.tipo= tipo
        super().__init__(fila,columna)

    def operar(self,arbol):
        valorIzquierdo=''
        valorDerecho=''
        if self.left !=None:
            valorIzquierdo=self.left.operar(arbol)
        if self.right != None:
            valorDerecho=self.right.operar(arbol)

         
        if self.tipo.operar(arbol)=='Suma':
            return valorIzquierdo + valorDerecho
        elif self.tipo.operar(arbol)=='Resta':
            return valorIzquierdo - valorDerecho
        elif self.tipo.operar(arbol)=='Multiplicacion':
            return valorIzquierdo * valorDerecho
        elif self. tipo.operar(arbol)=='Division':
            return valorIzquierdo/ valorDerecho
        elif self.tipo.operar(arbol)=='Modulo':
            return valorIzquierdo % valorDerecho
        elif self.tipo.operar(arbol)=='Potencia':
            return valorIzquierdo** valorDerecho
        elif self.tipo.operar(arbol)=='Raiz':
            return valorIzquierdo**(1/valorDerecho)
        elif self.tipo.operar(arbol)=='Inverso':
            return 1/valorIzquierdo
        
        else:
            return 0

    def getFila(self):
        return super().getFila()
   
    def getColumna(self):
        return super().getColumna()