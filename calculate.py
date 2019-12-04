'''
Created on 3 dic. 2019

@author: Ecarvallo
#v1.0
'''
from tkinter import *
from tkinter import ttk


class Calculator:
    def ventana_Calculator(self):
        ########## Create window menu
        self.calculator = Tk()
        self.calculator.geometry("300x250")
        self.calculator.title("Calcular cortes")
        self.calculator.resizable(False, False)
        
        ######### Seleccionar linea ######
        
        self.linea= ttk.Combobox(self.calculator, state="readonly")
        self.linea.place(x=126, y=10)
        self.linea["values"] = ["", "Linea 20", "Linea 25"]
        
        self.insertLinea= ttk.Label(self.calculator, text="Seleccione linea: ")
        self.insertLinea.place(x=20, y=10)
        ######## Ingresar Ancho ########
        
        self.insertX= ttk.Label(self.calculator, text="Ingrese ancho (X): ")
        self.insertX.place(x=20, y=40)
        
        self.eDimensionsX=ttk.Entry(self.calculator)
        self.eDimensionsX.place(x=126, y=40)
        
        ######## Ingresar Alto #########
        
        self.insertY= ttk.Label(self.calculator, text="Ingrese alto (Y): ")
        self.insertY.place(x=20, y=70)
        
        self.eDimensionsY=ttk.Entry(self.calculator)
        self.eDimensionsY.place(x=126, y=70)
        
        
        calcuteButton= ttk.Button(self.calculator, text="Calcular", 
                          command= self.calcular, 
                          ).place(x=33, y=110)
        
        
        self.calculator.mainloop()
    def calcular(self):
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
            
        
        self.jambaL = ttk.Label(self.calculator, text="Jamba: "+str(jamba)+" cm")
        self.jambaL.place(x=126, y=100)
        
        self.piernaL = ttk.Label(self.calculator, text="Pierna: "+str(pierna)+" cm")
        self.piernaL.place(x=126, y=120)
        
        self.traslapoL = ttk.Label(self.calculator, text="Traslapo: "+str(traslapo)+" cm")
        self.traslapoL.place(x=126, y=140)
        
        self.zocaloL = ttk.Label(self.calculator, text="Zocalo: "+str(zocalo)+" cm")
        self.zocaloL.place(x=126, y=160)
        
        self.cabezalL = ttk.Label(self.calculator, text="Cabezal: "+str(cabezal)+" cm")
        self.cabezalL.place(x=126, y=180)
        
        self.rielesL = ttk.Label(self.calculator, text="Rieles: "+str(rieles)+" cm")
        self.rielesL.place(x=126, y=200)