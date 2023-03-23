from tkinter import *
from tkinter.filedialog import askopenfile


class Mi_ventan(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=520,height=370,bg='#04B45F')
        self.master=master
        self.pack()
        self.ventana_principal()
    
    def ventana_principal(self):
        self.label_ar= Label(self, text="Archivo", bg='#FFBF00', )
        self.boton_abrir=Button(self, text='Abrir', bg='#BDBDBD', command=self.buscar_archivo)
      #  self.imagen1=PhotoImage(self,file="carpeta.jpg")
      #  self.label_imagen1= Label(self,image=self.imagen1)
        self.boton_guardar=Button(self, text='Guardar',bg='#BDBDBD' )
        self.boton_Analizar=Button(self,text='Analizar',bg='#BDBDBD' )
        self.boton_errores=Button(self,text='Errores',bg='#BDBDBD' )
        self.boton_salir=Button(self,text='Salir',bg='#BDBDBD' , command=self.quit)


        self.label_ayuda=Label(self, text='Ayuda',bg='#FFBF00')
        self.boton_usuario=Button(self, text='Manual de Usuario',bg='#BDBDBD' )
        self.boton_tecnico=Button(self,text='Manual Técnico',bg='#BDBDBD' )
        self.boton_ayuda=Button(self,text='Temas de ayuda',bg='#BDBDBD' )
        
        



        self.label_ar.place(x=10,y=5, width=200, height=35)
        self.boton_abrir.place(x=50, y=70,width=100, height=30 )
       # self.label_imagen1.place(x=5,y=60,width=30, height=30)
        self.boton_guardar.place(x=50,y=110, width=100, height=30)
        self.boton_Analizar.place(x=50, y=150, width=100, height=30 )
        self.boton_errores.place(x=50, y=190, width=100, height=30)
        self.boton_salir.place(x=50,y=230, width=100, height=30)

        self.label_ayuda.place(x=270,y=5, width=200, height=35)
        self.boton_usuario.place(x=310, y=70,width=110, height=30 )
        self.boton_tecnico.place(x=310,y=110, width=110, height=30)
        self.boton_ayuda.place(x=310, y=150, width=110, height=30 )

    def buscar_archivo(self):
      ventana=askopenfile(title="seleccione el archivo")
      archivo_abierto=open(ventana)
      print('se cargo el archivo seleccionado')



root=Tk()
app=Mi_ventan(root)
app.mainloop()