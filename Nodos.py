class Nodos:
    def __init__(self,datos):
        self.datos=datos
        self.siguiente=None

class lista_simple:
    def __init__(self):
        self.cabeza=None
        self.tamaño=0

    def insertar(self,datos):
        nuevoNodo=Nodos(datos)
        if self.tamaño==0 :
            self.cabeza=nuevoNodo

        else:
            aux=self.cabeza
            while aux.siguiente !=None:
                aux=aux.siguiente
            aux.siguiente=nuevoNodo
        self.tamaño+=1

    def mostrar(self):
        aux=self.cabeza
        while aux != None:
            print (aux.datos+' ')

            aux=aux.siguiente
    
    def eliminar(self,dato):
        if int(self.cabeza.dato)==int(dato):
            self.cabeza=self.cabeza.siguiente
            return True
      




