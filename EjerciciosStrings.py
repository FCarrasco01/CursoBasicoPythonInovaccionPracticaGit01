#1.-Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

    # _1nombre=input('¿Cuál es tu nombre? ')
    # _1num=round(float(input('Introduce un número: ')))
    # _1count=1
    # while _1count <= _1num:
    #     print(_1nombre)
    #     _1count= _1count+1

#2.- Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

    # _2nombre=input('¿Cuál es tu nombre? ')

    # print(_2nombre.upper())
    # print(_2nombre.lower())
    # print(_2nombre.title())

#3.-Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

    # _3nombre= input('¿Cuál es tu nombre? ')
    # _3nombrenum= len(_3nombre)
    # print(f'{_3nombre} tiene {_3nombrenum} letras')
    
#4.-Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

    # _4numtelefono= input('¿Cuál es el número de teléfono? +_ _ - _ _ _ _ _ _ _ _ _ - _ _: ')
    # _4ntcentro= _4numtelefono.split('-')

    # print(_4ntcentro[1])
    
#5.- Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

    # _5nombre= input('Introduce una oración ')[::-1]

    # print(_5nombre)
    
#6.- Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

