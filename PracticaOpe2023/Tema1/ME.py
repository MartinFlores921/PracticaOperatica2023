import csv
from punt import Puntaje

class manejadorE:
    __listaE: list
    
    def __init__(self):
        self.__listaE = []
    
    def cargaListaE(self):
        archivo= open("evaluacion.csv")
        reader= csv.reader(archivo, delimiter=";")
        for fila in reader:
            unaEvaluacion= Puntaje(fila[0], fila[1], float(fila[2]), float(fila[3]), float(fila[4]))
            self.__listaE.append(unaEvaluacion)
        archivo.close()
    
    def mostrarListaE(self):
        for i in range(len(self.__listaE)):
            print("Dni: {}, Estilo: {}, Juez1: {}, Juez2: {}, Juez3: {}".format(self.__listaE[i].getDniPatinador(), self.__listaE[i].getEstilo(), self.__listaE[i].getJuez1(), self.__listaE[i].getJuez2(), self.__listaE[i].getJuez3()))
            i+=1
    
    def inciso1(self, est, edad, federado):
        i=0
        print("Listar Patinadores por Estilo \n")
        for i in range (len(self.__listaE)):
            if self.__listaE[i].getEstilo() == est:
                dni= self.__listaE[i].getDniPatinador()
                federado.listar(edad, dni)
          
    def mayorpuntaje(self, federado):
        i=0
        max= self.__listaE[0].getPuntaje()
        for i in range (len(self.__listaE)-1):
            if self.__listaE[i].getPuntaje() > max:
                max= self.__listaE[i].getPuntaje()
                dni= self.__listaE[i].getDniPatinador()
                estilo= self.__listaE[i].getEstilo()
        federado.ListarMayor(max,dni,estilo)
    
    def buscarDni(self, dni):
        i=0
        c=0
        while i < len(self.__listaE):
            if self.__listaE[i].getDniPatinador() == dni:
                c+=1
            i+=1
        return c
    
    def inciso4(self, dni, estilo):
        i=0
        while i < len(self.__listaE):
            if (self.__listaE[i].getDniPatinador() == dni ) and (self.__listaE[i].getEstilo() == estilo):
                print("Juez1: {}, Juez2: {}, Juez3: {}".format(self.__listaE[i].getJuez1(), self.__listaE[i].getJuez2(), self.__listaE[i].getJuez3()))
            i+=1
    
            