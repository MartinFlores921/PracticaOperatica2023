def menudeopciones(afiliado, atencion):
    print("MENU DE OPCIONES")
    print("1-Cargar Listas")
    print("2-Mostrar Listas")
    print("3.Listar Total del Importe de una Fecha determinada")
    print("4- Mostrar cantidad de pacientes atendidos por Dni")
    print("5- Mostrar Ordenado de menor a mayor los afiliados")
    print("6. Listar los que no tuvieron ninguna atencion")
    opcion= input("Ingrese una opcion \n")
    while opcion !=0:
        if opcion == "1":
            afiliado.cargarListaA()
            atencion.cargarListaAT()
            print("")
        elif opcion == "2":
            afiliado.mostrarListaA()
            atencion.mostrarListaAT()
        elif opcion == "3":
            fecha= input("Ingrese una Fecha \n")
            entidad= input("Ingrese una Entidad \n")
            atencion.inciso1(fecha, entidad, afiliado)
        elif opcion == "4":
            dni= input("Ingrese Dni \n")
            atencion.inciso2(dni, afiliado)
        elif opcion == "5":
            afiliado.ordenar()
        
        elif opcion == "6":
            afiliado.inciso4(atencion)
        
        opcion = input("Ingrese una opcion, finalice con 0 \n")
        
        
    