import csv
from fed import Federado
class manejadorF:
    __listaF: list
    def __init__(self) -> None:
        self.__listaF = []
    
    def cargaListaF(self):
        archivo= open("federados.csv")
        reader= csv.reader(archivo, delimiter=";")
        for fila in reader:
            unFederado= Federado(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__listaF.append(unFederado)
        archivo.close()
        
    def mostrarListaF(self):
        for i in range (len(self.__listaF)):
            print("Apellido: {}, Nombre: {}, Dni: {}, Edad: {}, Club: {}".format(self.__listaF[i].getApellido(), self.__listaF[i].getNombre(), self.__listaF[i].getDni(), self.__listaF[i].getEdad(), self.__listaF[i].getClub()))
            i+=1
            
    def listar(self, edad, dni):
        i=0
        for i in range(len(self.__listaF)):
            if self.__listaF[i].getDni() == dni and self.__listaF[i].getEdad()== edad:
                print("Apellido: {}".format (self.__listaF[i].getApellido()))
                print("Nombre: {}".format(self.__listaF[i].getNombre()))
                print("Dni:{}".format(self.__listaF[i].getDni()))
        
            
    def ListarMayor(self, max, dni, estilo):
        i=0
        print("Los Datos del Participante con Mayor Puntaje que es: {}\n".format(max))
        for i in range(len(self.__listaF)):
            if self.__listaF[i].getDni() == dni:
                print("Apellido: {}, Nombre:{}, Estilo:{}, Club:{}".format(self.__listaF[i].getApellido(), self.__listaF[i].getNombre(), estilo, self.__listaF[i].getClub()))
   
    def inciso3(self, evaluacion):
        i=0
        print("Listado de Patinadores que Participaron en Ambos Estilos \n")
        for i in range (len(self.__listaF)):
            dni= self.__listaF[i].getDni()
            a= evaluacion.buscarDni(dni)
            if a>1:
                print("Apellido: {}, Nombre: {}, Dni: {}, Edad: {}, Club: {}".format(self.__listaF[i].getApellido(), self.__listaF[i].getNombre(), self.__listaF[i].getDni(), self.__listaF[i].getEdad(), self.__listaF[i].getClub()))
                