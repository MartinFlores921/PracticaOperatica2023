class Afiliado:
    __dni: str
    __nombreyApellido: str
    __unidad: str
    
    def __init__(self, dni, nombreya, unidad):
        self.__dni= dni
        self.__nombreyApellido= nombreya
        self.__unidad= unidad
      
    
    def getDni(self):
        return self.__dni
    
    def getNombreyApellido(self):
        return self.__nombreyApellido
    def getUnidad(self):
        return self.__unidad
    
    def __lt__(self, otro):
        band= None
        if (type(self)== type(otro)):
            a= self.__nombreyApellido + self.__unidad
            b= otro.__nombreyApellido + otro.__unidad
            band= a < b
        return (band)