'''
Created on 29 nov. 2019

@author: Ecarvallo
'''
from tkinter import *
from tkinter import messagebox

from tkinter import ttk
import datetime
from tkcalendar import Calendar, DateEntry
from verPedidos import TestApp


class Form:
    def __init__ (self):

        
        
        self.root = Tk()
        self.root.geometry("300x250")
        
        #self.prueba.geometry("300x250")

        ######### Seleccionar linea ######
        
        self.linea= ttk.Combobox(self.root, state="readonly")
        self.linea.place(x=126, y=10)
        self.linea["values"] = ["", "Linea 20", "Linea 25"]
        
        self.insertLinea= ttk.Label(self.root, text="Seleccione linea: ")
        self.insertLinea.place(x=20, y=10)
        ######## Ingresar Ancho ########
        
        self.insertX= ttk.Label(self.root, text="Ingrese ancho (X): ")
        self.insertX.place(x=20, y=40)
        
        self.eDimensionsX=ttk.Entry(self.root)
        self.eDimensionsX.place(x=126, y=40)
        
        ######## Ingresar Alto #########
        
        self.insertY= ttk.Label(self.root, text="Ingrese alto (Y): ")
        self.insertY.place(x=20, y=70)
        
        self.eDimensionsY=ttk.Entry(self.root)
        self.eDimensionsY.place(x=126, y=70)
        
        #self.printar()

        
        ######### Boton calcular #########

        calcuteButton= ttk.Button(self.root, text="Calcular", 
                          command= self.calculateDimensions, 
                          ).place(x=33, y=110)
        verPedidos= ttk.Button(self.root, text="Ver Pedidos", 
                          command= self.viewPedidos, 
                          ).place(x=33, y=170)
        addButton= ttk.Button(self.root, text="Agregar Pedido", 
                    command= self.addForm, 
                    ).place(x=33, y=140)
        clean = ttk.Button(self.root, text="Limpiar", 
                    command= self.limpiar, 
                    ).place(x=33, y=200)           
        ######### Boton calcular #########


                          
        ##### Mainloop ##### 
        self.root.mainloop()
  
    def calculateDimensions(self):
        self.lineaa = self.linea.get()
        
        self.x=self.eDimensionsX.get()
        self.x=float(self.x)
        self.y=self.eDimensionsY.get()
        self.y =float(self.y)
        
        if self.lineaa=="Linea 20":
            jamba=self.x
            pierna=self.x-3.6
            traslapo=self.x-3.6
            zocalo= (self.y/2)-0.2
            cabezal=(self.y/2)-0.2
            rieles= self.y-1.2
        elif self.lineaa=="Linea 25":
            jamba= self.x
            pierna= self.x-4.6
            traslapo= self.x-4.6
            zocalo= (self.y/2)
            cabezal= (self.y/2)
            rieles= self.y-1.6
            
        
        self.jambaL = ttk.Label(self.root, text="Jamba: "+str(jamba)+" cm")
        self.jambaL.place(x=126, y=100)
        
        self.piernaL = ttk.Label(self.root, text="Pierna: "+str(pierna)+" cm")
        self.piernaL.place(x=126, y=120)
        
        self.traslapoL = ttk.Label(self.root, text="Traslapo: "+str(traslapo)+" cm")
        self.traslapoL.place(x=126, y=140)
        
        self.zocaloL = ttk.Label(self.root, text="Zocalo: "+str(zocalo)+" cm")
        self.zocaloL.place(x=126, y=160)
        
        self.cabezalL = ttk.Label(self.root, text="Cabezal: "+str(cabezal)+" cm")
        self.cabezalL.place(x=126, y=180)
        
        self.rielesL = ttk.Label(self.root, text="Rieles: "+str(rieles)+" cm")
        self.rielesL.place(x=126, y=200)
        
         
    
        #self.printar()
class Acciones(Form): 
    def limpiar(self):
            self.linea.current(0)
        
            self.eDimensionsX.delete(0, END)
            self.eDimensionsX.insert(0, "")
            
            self.eDimensionsY.delete(0, END)
            self.eDimensionsY.insert(0, "")

    def addPedidos(self):
        
        self.fecha=self.cal.get_date()
        self.fEntrega = self.fecha.strftime("%d-%b-%Y ")

        file = open("test.csv", "a")
        file.write(self.timestampStr+", "+self.insertName.get()+", "+self.insertDireccion.get()+", "+self.insertContacto_.get()+", "+str(self.eDimensionsX.get())+", "+str(self.eDimensionsY.get())+", "+self.linea.get()+", "+self.fEntrega+'\n')

        file.close()
        
        self.add.withdraw()
        messagebox.showinfo("BD Actualizada", "Se ha agregado el pedido correctamente")

        self.limpiar()
    def viewPedidos(self):
        nuevo = TestApp()


        
    def addForm(self):
        self.add = Tk()
        
        self.add.geometry("300x350")

        self.a = datetime.datetime.now()
        self.timestampStr = self.a.strftime("%d-%b-%Y ")

        self.q= StringVar(self.add, value=self.timestampStr)

        ######## Fecha ingreso ########
        
        datee= ttk.Label(self.add, text="Fecha ingreso: ")
        datee.place(x=20, y=40)
        
        self.dateSelect=ttk.Entry(self.add,
                                      textvariable=self.q,
                                      state=DISABLED)

        self.dateSelect.place(x=126, y=40)
        
        

        ######## Ingresar nombre #########
        
        name= ttk.Label(self.add, text="Nombre: ")
        name.place(x=20, y=70)
        
        self.insertName=ttk.Entry(self.add)
        self.insertName.place(x=126, y=70)
        ######## Direccion #########
        
        direccion= ttk.Label(self.add, text="Direccion: ")
        direccion.place(x=20, y=100)
        
        self.insertDireccion=ttk.Entry(self.add)
        self.insertDireccion.place(x=126, y=100)
        
        ######## Contacto #########
        
        contacto= ttk.Label(self.add, text="Tel. Contacto: ")
        contacto.place(x=20, y=130)
        
        t=StringVar(self.add, value="+56 9 ")
        self.insertContacto=ttk.Entry(self.add, textvariable=t, width=6, state=DISABLED)
        self.insertContacto.place(x=126, y=130)
        
        self.insertContacto_=ttk.Entry(self.add, width=12)
        self.insertContacto_.place(x=172, y=130)
        
        ######## Dimensiones #########
        
        dimensiones= ttk.Label(self.add, text="Dimensiones: ")
        dimensiones.place(x=20, y=180)
        
        self.dX=StringVar(self.add, value=self.eDimensionsX.get())
        self.dY=StringVar(self.add, value=self.eDimensionsY.get())
        self.dL= StringVar(self.add, value=self.linea.get())
        self.insertdimensionesX=ttk.Entry(self.add, textvariable=self.dX, width=5, state=DISABLED)
        self.insertdimensionesX.place(x=126, y=180)
        
        por= ttk.Label(self.add, text="x ")
        por.place(x=164, y=180)
        
        self.insertdimensionesY=ttk.Entry(self.add, textvariable=self.dY, width=5, state=DISABLED)
        self.insertdimensionesY.place(x=174, y=180)
        
        ####### LINEA ######
        lineaa= ttk.Label(self.add, text="Linea: ")
        lineaa.place(x=20, y=210)
        
        self.insertContacto=ttk.Entry(self.add, textvariable=self.dL, state=DISABLED)
        self.insertContacto.place(x=126, y=210)
        
        ###### FECHA COMPROMISO ##### 
        
        lineaa= ttk.Label(self.add, text="Fecha entrega: ")
        lineaa.place(x=20, y=270)

        self.cal = DateEntry(self.add, width=12, background='darkblue',
                    foreground='white', borderwidth=2, year=2019)
        self.cal.place(x=126, y=270)
        
        addPedido= ttk.Button(self.add, text="Agregar", 
                          command= self.addPedidos, 
                          ).place(x=126, y=300)
         
        self.add.mainloop()
    
if __name__ == '__main__':   
     agregar= Acciones()
