from MF import manejadorF
from ME import manejadorE
from Menu import menudeopciones
if __name__ == "__main__":
    federado= manejadorF()
    evaluacion= manejadorE()
    menudeopciones(federado,evaluacion)


"""Lote de Prueba 
Para empezar, colocar la opcion 1 para cargar la lista y luego la opcion 2 para verificar que se muestra y se trabaja con la lista bien cargadas

Opcion 3:
-Estilo: L
-Edad: 17
Me deberia mostrar:
-Apellido: Martinez 
-Nombre:Milagros
-Edad: 17
-Apellido: Lara
-Nombre:Julieta
-Edad: 17

Opcion 4:
Me deberia mostrar:
Que el mayor puntaje es de 9.83 y que pertenece a Castro Valentina con Estilo Libre y del Club Laprida

Opcion 5:
Me deberia mostrar.
Los participantes que participaron en ambos estilos tanto como Libre y Escuela son:
-Lara Julieta con Dni: 48890755, Edad: 17 y Club Aberastain
-Castro Valentina con Dni: 50080987, Edad 15 y Club Laprida



opcion 6
-Dni: 48890755
-Estilo: L
Me deberia mostrar 9.0, 9.5 y 8.9
"""