def menudeopciones (cliente,reparacion):
    print("---- MENU DE OPCIONES ----")
    print("1-Mostrar las Listas ")
    print("2- Mostrar Datos de un Cliente")
    print("3- Mostrar Datos del Cliente a partir de una Patente que se encuentra en estado T(terminado) ")
    print("4- Listar Clientes con Reparaciones en estado P(pendiente)")
    print("5-")
    opcion = input("Ingrese una Opcion \n")
    while opcion != "0":
        if opcion == "1":
            print("A continuacion se mostrara la Lista de Clientes \n")
            cliente.mostrarListaC()
            print("A continuacion se mostrara la Lista de Reparaciones \n")
            reparacion.mostrarListaR()

        elif opcion == "2":
            dni= input("Ingrese el Dni de un Cliente: \n")
            cliente.inciso1(dni,reparacion)
        elif opcion == "3":
            pat= input("Ingrese una Patente de un Vehiculo: \n")
            reparacion.inciso2(pat, cliente)
            cliente.mostrarListaC()
        elif opcion == "4":
            print("Listado de los Datos de losVehiculos con Estado Pendiente \n")
            reparacion.listarPendientes(cliente)
        elif opcion == "5":
            print("Listado de aquellos usuarios que tienen en serivico mas de un vehiculo \n")
            cliente.ListarServicio()
        
        opcion= input("Ingrese una Opcion, 0 para Finalizar \n")
            