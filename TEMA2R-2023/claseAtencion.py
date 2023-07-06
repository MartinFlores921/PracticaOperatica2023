
class Atencion:
    __dni: str
    __fecha: str
    __importe: int
    __entidad: str
    __porc: int

    
    def __init__(self, dni, fech, imp, ent, porc):
        self.__dni= dni
        self.__fecha= fech
        self.__importe= imp
        self.__entidad= ent
        self.__porc= porc
    
        
    
    def getDni(self):
        return self.__dni
    
    def getFecha(self):
        return self.__fecha
    def getImporte(self):
        return self.__importe
    
    def getEntidad(self):
        return self.__entidad
    
    def getPorcentaje(self):
        return self.__porc
    

