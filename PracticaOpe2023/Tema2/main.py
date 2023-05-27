


from ManejadorCliente import manejadorC
from ManejadorReparacion import manejadorR
from menu import menudeopciones
if __name__ == '__main__':
    cliente= manejadorC()
    cliente.cargarListaC()
    reparacion= manejadorR()
    reparacion.cargarListaR()
    menudeopciones(cliente, reparacion)

"""Lote de Prueba

Para el Inciso a)

-Dni: 21111223
Me debe mostrar lo siguiente:
-Apellido y Nombre: Carmona Maria
-Patente: AB000BA
-Vehiculo: Fiat Mobi
Recordemos que el subtotal se calcula como: precio de repuesto + precio de mano de obra
-Reparacion: Cambio de pastillas de freno con precio de repuesto 230000 y mano de obra 11000, la cual su subtotal es 34000
-Reparacion: Reparacion de arranque con precio de repuesto 380000 y mano de obra 3800, la cual su subtotal es 41800
-Reparacion: Recarga de liquido de freno con precio de repuesto 6900 y mano de obra 2300, la cual su subtotal es 9200
-El total a pagar que es la suma de los subtotales de cada reparacion debe ser de 85000.

-Dni: 14205123
Me debe mostrar lo siguiente:
-Apellido y Nombre: Romero Hector
-Patente: AF341JM
-Vehiculo: Chevrolet Prisma
Recordemos que el subtotal se calcula como: precio de repuesto + precio de mano de obra
-Reparacion: Reparacion de tren delantero con precio de repuesto 56700 y mano de obra 23000, la cual su subtotal es 79700
-El total a pagar que es la suma de los subtotales de cada reparacion es de 79700

-Dni: 41234567
Me debe mostrar lo siguiente:
-Apellido y Nombre: Ferrez Carlos
-Patente: AE355BA
-Vehiculo: VW Polo
Recordemos que el subtotal se calcula como: precio de repuesto + precio de mano de obra
-Reparacion: Cambio de aceite y filtro con precio de repuesto 19800 y mano de obra 7990, la cual su subtotal es 27790
-Reparacion: Cambio de filtro de combustible con precio de repuesto 23000 y mano de obra 7990, la cual su subtotal es 30990
-El total a pagar que es la suma de los subtotales de cada reparacion es de 58780

Para el inciso B)
Para el inciso B, debemos prestar atencion que en el archivo "reparaciones. csv" para algunas patentes se encuentra en estado T(terminado) pero en el archivo clientes sale como P (pendiente),
el inciso nos pide que mostremos los datos de esa patente y que modifiquemos su estado en el archivo cliente

-Patente: AC300CC
Me debe mostrar:
-Apellido y Nombre: Dobro Carla
-Telefono: 264566789
-Vehiculo: Toyota Corola
-Total a pagar es: 51000 (que es la suma de los subtotales)
Luego, se va a mostrar la Lista de Clientes, en la cual vamos a verificar que antes el Estado para la Patente AC300CC era P(pendiente) y ahora es T (terminado)

-Patente: AC001CA
Me debe mostrar:
-Apellido y Nombre: Fernandez, Andrea
-Telefono: 2644561987
-Vehiculo: Renault Kangoo
-Total a Pagar: 39770(que es la suma de los subtotales)
Luego, se va a mostrar la Lista de Clientes, en la cual vamos a verificar que antes el Estado para la Patente AC300CC era P(pendiente) y ahora es T (terminado)

Para el Inciso C)
-Apellido y Nombre: Ferrez Carlos      Telefono: 2645712341
-Patente: AE355BA                      -Vehiculo: VW Polo
-Reparacion: Cambio de Aceite y filtro
-Reparacion: Cambio de filtro de Combustible

-Apellido y Nombre: Romero Hector    Telefono: 2645234561;
-Patente: AF341JM                  -Vehiculo: Chevrolet Prisma
-Reparacion: reparacion de tren delantero

Luego, se mostrata los datos de las patentes VXN231

Para el Inciso D)
Me deberia mostrar Rivas Elias pero me muestra Carmona Maria, but idk


"""""