'''
Created on 3 dic. 2019

@author: Ecarvallo
'''

############### Libraries
from tkinter import *
from tkinter import ttk
##############

from calculate import Calculator
from addpedido import AddPedido
from viewpedido import  TestApp


class Main:
    
    
    def menu(self):
    ########## Create window menu
        self.root = Tk()
        self.root.geometry("450x200")
        self.root.title("TodoVentanas Management")
        self.root.resizable(False, False)
    ##########
    
    ########## Create buttons
        cutsCalculator= ttk.Button(self.root, text="Calcular cortes", command= self.callCalculator).place(x=33, y=90)
                          
        addPedido= ttk.Button(self.root, text="Agregar pedido", command= self.callAdd).place(x=183, y=90)
    
        viewPedido= ttk.Button(self.root, text="Ver pedidos", 
                              command= self.callView, 
                              ).place(x=333, y=90)
    
    
    
    
    
    
        self.root.mainloop() #Set visible graphic interface.
        
    def callCalculator(self):
        callCalculator = Calculator()
        callCalculator.ventana_Calculator()
        # self.root.destroy()

    def callAdd(self):
        callAdd = AddPedido()
        callAdd.ventana_addPedido()    
    def callView(self):
        callView = TestApp()
        
menu = Main()
menu.menu()