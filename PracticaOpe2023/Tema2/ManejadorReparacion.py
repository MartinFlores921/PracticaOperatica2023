import csv
from claseReaparacion import Reparacion
class manejadorR:
    __listaR: list
    
    def __init__(self):
        self.__listaR = []
    
    def cargarListaR(self):
        archivo= open("reparaciones.csv")
        reader= csv.reader(archivo, delimiter=";")
        next (reader)
        for fila in reader:
            unaReparacion = Reparacion(fila[0], fila[1], int( fila[2]), int(fila[3]), fila[4])
            self.__listaR.append(unaReparacion)
        archivo.close()
    
    def mostrarListaR(self):
        i=0
        for i in range (len(self.__listaR)):
            print("Patente: {}, Reparacion: {}, PrecioRepuesto: {}, PrecioManodeObra: {}, Estado: {}".format(self.__listaR[i].getPat(),self.__listaR[i].getReparacion(), self.__listaR[i].getPrecioRepuesto(), self.__listaR[i].getPrecioManodeObra(), self.__listaR[i].getEst()))
   
        
    def ListarporPatente(self, patente):
        subtotal= 0
        acum=0
        for i in range (len(self.__listaR)):
            if self.__listaR[i].getPat() == patente:
                #print("Patente: {}".format(self.__listaR[i].getPat()))
                subtotal = self.__listaR[i].getPrecioRepuesto() + self.__listaR[i].getPrecioManodeObra()
                print("Reparacion: {}  Precio Repuesto: {} \t \t Precio Mano de Obra: {}  Subtotal:{}\t \t \t  ".format(self.__listaR[i].getReparacion(),self.__listaR[i].getPrecioRepuesto(), self.__listaR[i].getPrecioManodeObra(), subtotal))
                #print("\t Precio Repuesto: {}".format(self.__listaR[i].getPrecioRepuesto()))
                #print("\t \t Precio Mano de Obra: {}".format(self.__listaR[i].getPrecioManodeObra()))
                #subtotal = self.__listaR[i].getPrecioRepuesto() + self.__listaR[i].getPrecioManodeObra()
                #print("El Subtotal es: {}".format(subtotal))
                acum += subtotal
        print(" \t \t \t \t El total a pagar es: {} ".format(acum))
    
    def inciso2(self, patente, cliente):
        subtotal=0
        acum=0
        for i in range(len(self.__listaR)):
            if self.__listaR[i].getPat() == patente:
                if self.__listaR[i].getEst() == "T":
                  estado = self.__listaR[i].getEst()
                  cliente.Comparar(patente, estado)
                  cliente.mostrar(patente)
                  subtotal = self.__listaR[i].getPrecioRepuesto() + self.__listaR[i].getPrecioManodeObra()
                  acum +=subtotal
            print("El Total a Pagar es: {}".format(acum))
    
    def listarPendientes(self, cliente):
        for i in range (len(self.__listaR)):
            if self.__listaR[i].getEst() == "P":
                patente= self.__listaR[i].getPat()
                cliente.ListarClientesPendientes(patente)
                print("Reparacion: {}".format(self.__listaR[i].getReparacion()))