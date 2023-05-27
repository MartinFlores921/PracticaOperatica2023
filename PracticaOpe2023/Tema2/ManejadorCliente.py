import csv
from claseCliente import Cliente
class manejadorC:
    __listaC: list
    
    def __init__(self):
        self.__listaC = []
    
    
    def cargarListaC(self):
        archivo= open("clientes.csv")
        reader= csv.reader(archivo, delimiter=";")
        next (reader)
        for fila in reader:
            unCliente = Cliente(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
            self.__listaC.append(unCliente)
        archivo.close()
    
    def mostrarListaC(self):
        i=0
        for i in range (len(self.__listaC)):
            print("Apellido: {}, Nombre: {}, Dni: {}, Telefono: {}, Patente: {}, Vehiculo: {}, Estado: {}".format(self.__listaC[i].getApellido(), self.__listaC[i].getNombre(), self.__listaC[i].getDni(), self.__listaC[i].getTelefono(), self.__listaC[i].getPatente(), self.__listaC[i].getVehiculo(), self.__listaC[i].getEstado()))
    
    def inciso1(self, dni, reparacion):
        print("\n")
        i=0
        while i < len(self.__listaC):
            if self.__listaC[i].getDni() == dni:
                print("Dni: {} \t \t \t Apellido y Nombre: {}".format(self.__listaC[i].getDni(),  self.__listaC[i].getAyN() ))
               # print(f"Apellido y Nombre: {self.__listaC[i].getAyN() :<20}")
               # print("Vehiculo: {}".format(self.__listaC[i].getVehiculo()))
                patente= self.__listaC[i].getPatente()
                print("Patente: {} \t \t Vehiculo: {}".format(patente, self.__listaC[i].getVehiculo()))
                reparacion.ListarporPatente(patente)
            i+=1
    def Comparar(self, patente, estado):
        for i in range(len(self.__listaC)):
            if self.__listaC[i].getPatente() == patente:
                if self.__listaC[i].getEstado() == "P":
                    self.__listaC[i].setEstado(estado)
    
    def mostrar(self, patente):
        for i in range(len(self.__listaC)):
          if self.__listaC[i].getPatente() == patente:
            print("Apellido y Nombre: {}".format(self.__listaC[i].getAyN()))
            print("Telefono:{}".format(self.__listaC[i].getTelefono()))
            print("Vehiculo: {}".format(self.__listaC[i].getVehiculo()))
    
    def ListarClientesPendientes(self, patente):
        for i in range(len(self.__listaC)):
            if self.__listaC[i].getPatente() == patente:
                print("Apellido y Nombre: {} Telefono: {} \t \t".format(self.__listaC[i].getAyN(), self.__listaC[i].getTelefono())) 
                print("Patente: {}, Vehiculo: {} \t \t".format(patente, self.__listaC[i].getVehiculo()))
    
    def ListarServicio(self):
        dat= self.__listaC[0]
        for i in range(len(self.__listaC)):
            if dat == self.__listaC[i]:
                dat = self.__listaC[i]
                print("Apellido y Nombre: {}, Dni: {}, Telefono: {}, Patente: {}, Vehiculo: {}".format(self.__listaC[i].getAyN(), self.__listaC[i].getDni(), self.__listaC[i].getTelefono(), self.__listaC[i].getPatente(),self.__listaC[i].getVehiculo()))
 
""" def inciso2(self,patente, reparacion):
        for i in range (len(self.__listaC)):
            if self.__listaC[i].getPatente() == patente:
                if self.__listaC[i].getEstado() == 
                """
