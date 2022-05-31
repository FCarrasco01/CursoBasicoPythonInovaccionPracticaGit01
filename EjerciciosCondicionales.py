#1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

    # _1edad= int(input('Por favor introduzca su edad: '))

    # if _1edad >= 18:
    #     print('Ya eres mayor de edad')
    # else:
    #     print('Todavía eres menor de edad')

#2.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

    # _2contraseña= input('Introduzca su contraseña: ')

    # _2cresp= input('¿Cuál es la contraseña? ')

    # if _2contraseña.casefold() == _2cresp.casefold():
    #     print('Bienvenido usuario')
    # else:
    #     print('Contraseña incorrecta')

#3.- Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

    # _3n1 = float(input('Introduzca el dividendo: '))
    # _3n2 = float(input('Introduzca el divisor: '))

    # if _3n2 == 0:
    #     print('Math error: zero division undefined')
    # else:
    #     print(_3n1/_3n2)

#4.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

    # _4n = int(input('Introduce un número entero: '))

    # if _4n%2 == 0:
    #     print(f'El número {_4n} es par')
    # else:
    #     print(f'El número {_4n} es impar')

#5.- Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

    # _5edad= int(input('¿Cuál es tu edad? '))
    # _5ingresos = float(input('¿Cuáles son tus ingresos mensuales? '))

    # if _5edad > 16 and _5ingresos >= 1000:
    #     print('Tienes que declarar impuestos')
    # else:
    #     print('No tienes que declarar impuestos')

#6.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

    # _6nombre= input('¿Cuál es tu nombre?')
    # _6sexo = input('¿Cuál es tu sexo? (M o H) ')

    # if _6sexo == 'M':
    #     if _6nombre.lower() < 'm':
    #         _6grupo = 'A'
    #     else:
    #         _6grupo = 'B'
    # else:
    #     if _6nombre.lower() > 'n':
    #         _6grupo = 'A'
    #     else:
    #         _6grupo = 'B'
    # print(f'Tu grupo es el {_6grupo}')

#7.-Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	                   Tipo impositivo
# Menos de 10000€	           5%
# Entre 10000€ y 20000€        15%
# Entre 20000€ y 35000€	       20%
# Entre 35000€ y 60000€	       30%
# Más de 60000€	               45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

    # _7renta= float(input('¿Cuánto paga de renta al año? '))

    # if _7renta <= 60000:
    #     if _7renta < 35000:
    #         if _7renta < 20000:
    #             if _7renta < 10000:
    #                 print('Impositivo = 5%')
    #             else:
    #                 print('Impositivo = 15%')
    #         else:
    #             print('Impositivo = 20%')
    #     else:
    #         print('Impositivo = 30%')
    # else:
    #     print('Impositivo = 45%')

#8.- En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable 	0.4
# Meritorio 	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

    # _8puntuacion = float(input('¿Cuál es la puntuación del usuario? '))
    # _8dinero= _8puntuacion * 2400

    # if _8puntuacion < 0.6:
    #     if _8puntuacion == 0.4:
    #         print('Nivel de rendimiento: Aceptable')
    #         print(f'Su bono será de {_8dinero} euros')
    #     else:
    #         if _8puntuacion  == 0.0:
    #             print('Nivel de rendimiento: Inaceptable')
    #             print(f'Su bono será de {_8dinero} euros')
    # else:
    #     print('Nivel de rendimiento: Meritorio')
    #     print(f'Su bono será de {_8dinero} euros')
    
#9.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€
    # _9costo = int(input('¿Cuál es su edad? '))

    # if _9costo < 18:
    #     if _9costo < 4:
    #         print('La entrada es totalmente gratis!')
    #     else:
    #         print('El costo de entrada es de 5 euros')
    # else:
    #     print('El costo de entrada es de 10 euros')   
        
#10.- La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos:    Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.



    # _9elec = input('¿Desea una pizza vegetariana? ')
    # _9contador = 1

    # while (_9contador == 1):
    #     if  _9elec.casefold() == 'si' or _9elec.casefold() == 'sí':
    #         print('Contamos con los siguientes ingredientes: pimiento y tofu. ')
    #         _9ving = input('¿Cuál desea? ')
    #         if _9ving.casefold() == 'pimiento':
    #             print('Tipo de pizza: vegetariana')
    #             print('Ingredientes: pimiento, mozzarella, salsa de tomate')
    #             print('En un momento estará lista')
    #             print('Gracias por su compra! ') 
    #             _9contador = 0
    #         else:
    #             if _9ving.casefold() == 'tofu':
    #                 print('Tipo de pizza: vegetariana')
    #                 print('Ingredientes: tofu, mozzarella, salsa de tomate')
    #                 print('En un momento estará lista')
    #                 print('Gracias por su compra!') 
    #                 _9contador = 0
    #             else:
    #                 print('Porfavor introduzca un ingrediente válido')
    #                 _9contador = 1
    #     else:
    #         print('Contamos con los siguientes ingredientes: peperoni, jamón y salmón')
    #         _9noving = input('¿Cuál desea? ')
    #         if _9noving.casefold() == 'peperoni' or _9noving.casefold() == 'pepperoni':
    #             print('Tipo de pizza: no vegetariana')
    #             print('Ingredientes: peperoni, mozzarella, salsa de tomate')
    #             print('En un momento estará lista')
    #             print('Gracias por su compra!') 
    #             _9contador = 0
    #         else:
    #             if _9noving.casefold() == 'jamon' or _9noving.casefold() == 'jamón':
    #                 print('Tipo de pizza: no vegetariana')
    #                 print('Ingredientes: jamón, mozzarella, salsa de tomate')
    #                 print('En un momento estará lista')
    #                 print('Gracias por su compra!') 
    #                 _9contador = 0
    #             else:
    #                 if _9noving.casefold() == 'salmon' or _9noving.casefold() == 'salmón':
    #                     print('Tipo de pizza: no vegetariana')
    #                     print('Ingredientes: salmón, mozzarella, salsa de tomate')
    #                     print('En un momento estará lista')
    #                     print('Gracias por su compra!') 
    #                     _9contador = 0
    #                 else:
    #                     print('Por favor introduzca un ingrediente válido. ')
    #                     _9contador = 1



    



 
    
    