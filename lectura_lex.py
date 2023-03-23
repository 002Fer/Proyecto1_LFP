from Nodos import lista_simple
from aritmetica import *
from trigonometrica import *
from lexema import *
from numero import*


global numero_lin
global numero_col
global instrucciones
global lista_lexemas

numero_lin=1
numero_col=1
lista_lexemas=lista_simple()
instrucciones=[]

def leer(cadena):
    global numero_lin
    global numero_col
    global lista_lexemas
 
    lexema=''
    puntero=0
    while cadena:
        char =cadena[puntero]
        puntero+=1

        if char =='\"' :
            lexema, cadena= armar_lexema(cadena[puntero:])
            if lexema and cadena:
                numero_col +=1
                #armado de lexema como clase
                armado=Lexema(lexema,numero_lin, numero_lin)


                lista_lexemas.insertar(armado)
                numero_col += len(lexema)+1
                puntero=0

        elif char.isdigit():
            token, cadena= armar_numero(cadena)
            if token and cadena:
                numero_col +=1
                #armado de lexema como clase
                num_clase=Numero(token, numero_lin,numero_col)
                #se agrega el lexema a la lista
                lista_lexemas.insertar(num_clase)
                numero_col +=len(str(token))+1
                puntero=0


        elif char =='[' or char==']':

            caracter=Lexema(char, numero_lin, numero_col)

            lista_lexemas.insertar(caracter)
            cadena= cadena[1:]
            puntero=0
            numero_col +=1

        elif char =='\t':
            numero_col+=4
            cadena=cadena[4:]
            puntero=0
        elif char =='\n':
            cadena=cadena[1:]
            puntero=0
            numero_lin +=1
            numero_col=1

        else:
            cadena=cadena[1:]
            puntero=0
            numero_col+=1



def armar_lexema(cadena):
    global numero_lin
    global numero_col
    global lista_lexemas
    lexema =''
    puntero =''
    for char in cadena:
        puntero +=char
        if char =='\"':
            return lexema, cadena[len(puntero):]
        else:
            lexema+=char
    return None, None
        
def armar_numero(cadena):
    numero=''
    puntero=''
    decimal= False
    #se puede cambiar por un while
    for char in cadena:
        puntero +=char
        if char =='.':
            decimal=True
        if char=='"' or char==' ' or char== '\n' or char== '\t':
            if decimal:
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:] 
        else:
            numero +=char
    return None, None

def operar():
    global lista_lexemas
    global instrucciones
    operacion=''
    n1=''
    n2=''
    while lista_lexemas:
        lexema=lista_lexemas.eliminar(0)
        if lexema.operar(None)=='Operacion':
            operacion=lista_lexemas.eliminar(0)
        elif lexema.operar(None)=='Valor1':
            n1=lista_lexemas.eliminar(0)
            if n1.operar(None)=='[':
                n1=operar()
        elif lexema.operar(None)=='Valor2':
            n2=lista_lexemas.eliminar(0)
            if n2.operar(None)=='[':
                n2=operar()
        if operacion and n1 and n2:
            return Aritmetica( n1, n2,operacion,f'Inicio: {operacion.gerFila()}:{operacion.getColumna()}',f'Fin: {n2.getFila()}:{n2.getColumna()}')
        
        elif operacion and n1 and operacion.operar(None)== ('Seno' or 'Coseno' or 'Tangente'):
            return Trigonometrica(n1, operacion,f'Inicio: {operacion.getFila()}:{operacion.getColumna()}',f'Fin: {n1.getFila()}:{n1.getColumna()}')
        
    return None

def operar2():
    global instrucciones
    while True:
        operacion=operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
    for instruccion in instrucciones:
        print(instruccion.operar(None))

entrada='''
{ 
 {"Operacion":"Suma"
 "Valor1":4.5
 "Valor2":5.32
 },
 {"Operacion":"Resta"
 "Valor1":4.5
 "Valor2":[
    "Operacion":"Potencia"
    "Valor1":10
    "Valor2":3
 ]},
 {"Operacion":"Suma"
 "Valor1":[
    "Operacion":"Seno"
    "Valor1":90
 ]
 "Valor2":5.32
 }
 "Texto":"Realizacion de Operaciones"
 "Color-Fondo-Nodo":"Amarillo"
 "Color-Fuente-Nodo":"Rojo"
 "Forma-Nodo":"Circulo"'''

leer(entrada)