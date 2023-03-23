from tkinter import *

raiz=Tk()
raiz.title('primera venatana')
raiz.geometry("500x300")
raiz.config(bg='#009999')



imagen1=PhotoImage(file="carpeta.jpg")
fondo= Label(raiz,image=imagen1)
fondo.place(x=0,y=0)

raiz.mainloop() 