
def menudeopciones( federado, evaluacion):
        print("Menu de Opciones")
        print("1- Cargar Listas")
        print("2 - Mostrar Listas Cargadas ")
        print("3- Listar Patinadores  ")
        print("4-Mostrar Datos del Patinador con Mayor Puntaje")
        print("5- Listar Datos de Patinadores que participaron en ambos estilos")
        print("6-Mostrar las Valoraciones de los 3 jueces")
        print("0-SALIR")
        opcion= input("Ingrese una Opcion: \n")
        while opcion != "0":
            if opcion ==  "1":
                federado.cargaListaF()
                evaluacion.cargaListaE()
            elif opcion == "2":
                print("Lista de Federados \n \n")
                federado.mostrarListaF()
                print("Lista de Evaluaciones \n \n")
                evaluacion.mostrarListaE()
            elif opcion == "3":
                est= input("Ingrese un Estilo \n")
                edad= input("Ingrese una Edad: \n")
                evaluacion.inciso1(est,edad,federado)
            elif opcion == "4":
                evaluacion.mayorpuntaje(federado)
            elif opcion == "5":
                federado.inciso3(evaluacion)
            elif opcion == "6":
                dni= input("Ingrese el Dni del Patinador: \n")
                estilo= input("Ingrese el Estilo del Patinador: \n")
                evaluacion.inciso4(dni,estilo)
            opcion= input("Ingrese una Opcion, 0 para Salir \n")
            
           