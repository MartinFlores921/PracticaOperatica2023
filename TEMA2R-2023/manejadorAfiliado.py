from claseAfiliados import Afiliado
import csv

class manejadorA: 
    __listaA: list
    
    def __init__(self):
        self.__listaA= []
    
    def cargarListaA(self):
        archivo= open("afiliados.csv")
        reader= csv.reader(archivo, delimiter=";")
        next (reader)
        for fila in reader:
            unAfiliado= Afiliado(fila[0], fila[1], fila[2])
            self.__listaA.append(unAfiliado)
        archivo.close()
    
    def mostrarListaA(self):
        for i in range (len(self.__listaA)):
            print("Dni: {}, NombreyApellido: {}, Unidad: {}".format(self.__listaA[i].getDni(), self.__listaA[i].getNombreyApellido(), self.__listaA[i].getUnidad()))
    
    def ObtenerNombre(self, dni):
        for i in range(len(self.__listaA)):
            if self.__listaA[i].getDni() == dni:
                nombre= self.__listaA[i].getNombreyApellido()
        return nombre
    
    def ordenar(self):
        self.__listaA.sort()
        for i in range (len(self.__listaA)):
            print("Nombre y Apellido: {}  Unidad: {}".format(self.__listaA[i].getNombreyApellido(), self.__listaA[i].getUnidad()))
    
    def inciso4(self, atencion):
        for i in range (len(self.__listaA)):
            dni= self.__listaA[i].getDni()
            c= atencion.contar(dni)
        
            if c == 0:
             print("El afiliado: {} no tiene atenciones ".format(self.__listaA[i].getNombreyApellido()))
                
            