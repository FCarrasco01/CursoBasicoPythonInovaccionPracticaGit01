#1.- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
    # _1contador = 1 
    # _1palabra= input('Introduzca una palabra: ')
    # while _1contador <= 10:
    #     print(_1palabra)
    #     _1contador = _1contador + 1
    
#2.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

    # _2edad = int(input('¿Cuál es su edad? '))
    # _2contador = 1

    # print('Usted ha pasado por estos años: ')

    # while _2contador <= _2edad:
    #     print(_2contador)
    #     _2contador = _2contador + 1

#3.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

    # _3n = int(input("Introduce un número entero positivo: "))
    # for i in range(1, _3n+1, 2):
    #     print(i, end=", ")
    
#4.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

    # _4n = int(input('Introduzca un número entero positivo: '))

    # for i in range(_4n, -1, -1):
    #     print(i, end=', ')
    
#5.- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

    # _5cantidad = float(input('¿Cuáll será a cantidad a invertir? '))
    # _5int_anual= float(input('¿Cuál será el interés anual? '))/100
    # _5años = float(input('¿Por cuantos años planea invertir?'))

    # _5ixc = _5cantidad * _5int_anual
    # _5contador = 1
    # _5cont_año = 1

    # while _5contador <= _5años:
    #     _5int_obt = _5ixc * _5contador
    #     _5cap_obt = _5int_obt + _5cantidad
    #     print(f'Año: {_5cont_año}')
    #     print(f'Interés: {_5int_obt}')
    #     print(f'Capital obtenido: {_5cap_obt}')
    #     _5contador = _5contador + 1
    #     _5cont_año = _5cont_año + 1
    
#6.- Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

    # _6n = int(input("Introduce la altura del triángulo (entero positivo): "))
    # for i in range(_6n):
    #    print("*"*(i+1))

#7.-  Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

    # _7tabla = int(input('Inserte el número de la tabla de multiplicar que desea: '))

    # _7contador = 1

    # while _7contador <= 10:
    #     _7mult = _7contador * _7tabla
    #     print(_7mult)
    #     _7contador = _7contador + 1
    
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")





 
    