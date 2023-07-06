from claseAtencion import Atencion
import csv

class manejadorAT: 
    __listaAT: list
    
    def __init__(self):
        self.__listaAT= []
    
    def cargarListaAT(self):
        archivo= open("atenciones.csv")
        reader= csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            unaAtencion= Atencion(fila[0], fila[1], int(fila[2]), fila[3], int(fila[4]))
            self.__listaAT.append(unaAtencion)
        archivo.close()
    
    def mostrarListaAT(self):
        for i in range (len(self.__listaAT)):
            print("Dni: {}, Fecha: {}, Importe: {}, Entidad: {}, Porcentaje: {}".format(self.__listaAT[i].getDni(), self.__listaAT[i].getFecha(), self.__listaAT[i].getImporte(), self.__listaAT[i].getEntidad(), self.__listaAT[i].getPorcentaje()))
    
    def inciso1(self, fecha, entidad, afiliado):
        i=0
        total=0
        imp=0
        while i < len(self.__listaAT):
            if self.__listaAT[i].getFecha() == fecha and self.__listaAT[i].getEntidad() == entidad:

                dni= self.__listaAT[i].getDni()
                nombre= afiliado.ObtenerNombre(dni)
                imp= self.__listaAT[i].getImporte() - ((self.__listaAT[i].getImporte() * self.__listaAT[i].getPorcentaje())/100)
                total += imp
                print("ATENCIONES  \t Fecha: {}".format(self.__listaAT[i].getFecha()))
                print("Dni: {}  \t\t NombreApellido: {}   \t\t\t Importe: {}".format(self.__listaAT[i].getDni(), nombre, imp))
            i+=1
       
        print(" \t \t \t \t \t TOTAL: {}".format(total))
    
    def inciso2(self, dni, afiliado):
        i=0
        c=0
        while i < len(self.__listaAT):
            if self.__listaAT[i].getDni() == dni:
                nombre= afiliado.ObtenerNombre(dni)
                c+=1
            i+=1
        print("El Afiliado: {} tuvo una cantidad de atenciones de {}".format(nombre, c))
    
    def contar(self, dni):
        c=0
        for i in range(len(self.__listaAT)):
            if self.__listaAT[i].getDni() == dni:
                c+=1
        return c
            
                
    
    
                
   