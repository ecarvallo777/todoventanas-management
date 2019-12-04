'''
Created on 3 dic. 2019

@author: Ecarvallo
'''
from tkinter import *
from tkinter import ttk
import datetime
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox



class AddPedido:
    def ventana_addPedido(self):
        
        
        self.add = Tk()
        
        self.add.geometry("300x350")
        self.add.title("Agregar pedido")
        self.add.resizable(False, False)

        self.a = datetime.datetime.now()
        self.timestampStr = self.a.strftime("%d-%b-%Y ")
        print(self.timestampStr)
        self.q= StringVar(self.add, value=self.timestampStr)

        ######## Fecha ingreso ########
        
        datee= ttk.Label(self.add, text="Fecha ingreso: ")
        datee.place(x=20, y=40)
        
        dateSelect=ttk.Entry(self.add)

        dateSelect.place(x=126, y=40)
        dateSelect.delete(0, END)
        dateSelect.insert(0, self.timestampStr)
        dateSelect.config(state='disabled')
        
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
        self.insertContacto=ttk.Entry(self.add, textvariable=t, width=6)
        self.insertContacto.place(x=126, y=130)
        
        self.insertContacto_=ttk.Entry(self.add, width=12)
        self.insertContacto_.place(x=172, y=130)
        
        ######## Dimensiones #########
        
        dimensiones= ttk.Label(self.add, text="Dimensiones: ")
        dimensiones.place(x=20, y=180)
        
        
        
        
        self.insertdimensionesX=ttk.Entry(self.add, width=5)
        self.insertdimensionesX.place(x=126, y=180)
        
        por= ttk.Label(self.add, text="x ")
        por.place(x=164, y=180)
        
        self.insertdimensionesY=ttk.Entry(self.add, width=5)
        self.insertdimensionesY.place(x=174, y=180)
        
        ####### LINEA ######
        lineaa= ttk.Label(self.add, text="Producto: ")
        lineaa.place(x=20, y=210)
        
        self.insertContacto=ttk.Entry(self.add)
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
                          

    def addPedidos(self):
        
        self.fecha=self.cal.get_date()
        self.fEntrega = self.fecha.strftime("%d-%b-%Y ")

        file = open("test.csv", "a")
        file.write(self.timestampStr+", " #
                   +self.insertName.get()+", " #
                   +self.insertDireccion.get()+", " #
                   +self.insertContacto_.get()+", " # 
                   +self.insertdimensionesX.get()+", "
                   +self.insertdimensionesY.get()+", "
                   +self.insertContacto.get()+", "
                   +self.fEntrega
                   +'\n')

        file.close()
        
        self.add.withdraw()
        messagebox.showinfo("BD Actualizada", "Se ha agregado el pedido correctamente")

