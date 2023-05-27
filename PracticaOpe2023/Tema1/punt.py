class Puntaje:
    __dniPatinador= ""
    __estilo= ""
    __juez1 = 1.0
    __juez2= 1.0
    __juez3= 1.0
    
    def __init__(self, dni, est, punt1, punt2, punt3):
        self.__dniPatinador = dni
        self.__estilo=est
        self.__juez1= punt1
        self.__juez2= punt2
        self.__juez3= punt3
    
    def getDniPatinador(self):
        return self.__dniPatinador
    def getEstilo(self):
        return self.__estilo
    def getValor(self):
        return self.__valor
    def getJuez1(self):
        return self.__juez1
    def getJuez2(self):
        return self.__juez2
    def getJuez3(self):
        return self.__juez3
    
    def getPuntaje(self):
        acum=0
        acum= self.__juez1 + self.__juez2 + self.__juez3
        return (acum/3)
    
    def __gt__(self, otro):
        if isinstance(otro,Puntaje):
            return self.getPuntaje() > otro.getPuntaje()
    