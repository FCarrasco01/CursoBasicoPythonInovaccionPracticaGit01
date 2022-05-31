#continuación de lo que tengo en mi casa
#6.- Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

    # _6frase = input('Por favor introduce una frase: ')
    # _6vocal= input('Por favor introduce una vocal: ')

    # print(_6frase.replace(_6vocal,_6vocal.upper()))

#7.- Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es

    # _7emailusuario= input('Por favor introduzca su correo electrónico: ')
    # _7eusplited= _7emailusuario.split('@')

    # print(f'{_7eusplited[0]}@ceu.es')

#8.- Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

    # _8PEuro= input('Por favor introduzca un precio en euros con dos decimales: ')
    # _8PEsplited= _8PEuro.split('.')

    # print(f'Euros: {_8PEsplited[0]}')
    # print(f'Céntimos: {_8PEsplited[1]}')

    # print('Gracias!')

#9.- Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

    # _9USfecha= input('Introduzca su fecha de nacimiento en formato dd/mm/aaaa: ')
    # _9Splitted= _9USfecha.split('/')

    # Meses = {
    #     1:'Enero',
    #     2:'Febrero',
    #     3:'Marzo',
    #     4:'Abril',
    #     5:'Mayo',
    #     6:'Junio',
    #     7:'Julio',
    #     8:'Agosto',
    #     9:'Septiembre',
    #     10:'Octubre',
    #     11:'Noviembre',
    #     12:'Diciembre'
    # }

    # print(f'Usted nació el {_9Splitted[0]} de {Meses[int(_9Splitted[1])]} del {_9Splitted[2]}')

#10.- Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

    # _10cesta = input('¿Qué planea comprar hoy? Sepárelo por comas: ')
    # _10items = _10cesta.split(', ')

    # for item in _10items:
    #     print(item)

#11.- Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.











