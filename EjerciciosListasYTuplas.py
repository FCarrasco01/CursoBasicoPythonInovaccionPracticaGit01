#1.- Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

    # _1asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
    # print(type(_1asignaturas))

    # for asignatura in _1asignaturas:
    #     print(asignatura)

#2.- Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

    # _2asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

    # for asignatura in _2asignaturas:
    #     print(f'Yo estudio {asignatura}')

#3.-    Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

    # _3materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    # _3calificaciones = []
    # for materia in _3materias:
    #     _3cal = input("¿Qué nota has sacado en " + materia + "? ")
    #     _3calificaciones.append(_3cal)
    # for i in range(len(_3materias)):
    #     print("En " + _3materias[i] + " has sacado " + _3calificaciones[i])
    
#4.- Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

    # _4premiados = []
    # for i in range(6):
    #     _4premiados.append(int(input("Introduce un número ganador: ")))
    # _4premiados.sort()
    # print("Los números ganadores son " + str(_4premiados))

#5.- Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

    # _5numeros = [1,2,3,4,5,6,7,8,9,10]
    # _5numeros.reverse()
    # print(_5numeros)

#6.- Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


    # _6pasadas = []
    # _6asignaturas = ['Matemáticas','Física','Química','Historia','Lengua']

    # for asignatura in _6asignaturas:
    #     __6cal = float(input(f"¿Qué calificación tienes en {asignatura}? "))
    #     if __6cal >= 6:
    #         _6pasadas.append(asignatura)

    # for materia in _6pasadas:
    #     _6asignaturas.remove(materia)       
            
    # print(f'Tienes que repetir {_6asignaturas}')       
        
#7.- Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

    # _7abecedario = ['A','B','C','E','D','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    # for char in range(len(_7abecedario),1,-1):
    #     if char % 3 == 0:
    #         _7abecedario.pop(char-1)
    # print(_7abecedario)

#8.- Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

    # _8palindromo = input('Escribe un palíndromo: ')
    # _8pr =  _8palindromo

    # _8palindromo = list(_8palindromo)
    # _8pr = list(_8pr)
    # _8pr.reverse()

    # if _8palindromo == _8pr:
    #     print('Es un palíndromo')
    # else:
    #     print('No es un palíndromo')

#9.- Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

    # _9palabra= input('Introduce una palabra: ')
    # _9vocales = ['a','e','i','o','u']

    # for vocal in _9vocales:
    #     _9repeticiones = 0
    #     for letra in _9palabra:
    #         if letra == vocal:
    #             _9repeticiones = _9repeticiones + 1
    #     print(f'La {vocal} se repite {_9repeticiones} veces')
        
#10.- Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

    # _10precios = [50,75,46,22,80,65,8]

    # print(f'El menor es {min(_10precios)} y el máximo {max(_10precios)}')

#11.- Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.































