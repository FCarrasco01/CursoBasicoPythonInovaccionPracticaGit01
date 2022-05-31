#1.- Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

    # _1divisas = {
    #     "Euro":'€',
    #     "Dolar":'$',
    #     "Yen":'¥'
    # }

    # input('Introduce una divisa: ')

#continuacion
#7.- Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

    # cesta = {}
    # continuar = True
    # while continuar:
    #     item = input('Introduce un artículo: ')
    #     precio = float(input('Introduce el precio de ' + item + ': '))
    #     cesta[item] = precio
    #     continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
    # coste = 0
    # print('Lista de la compra')
    # for item, precio in cesta.items():
    #     print(item, '\t', precio)
    #     coste += precio
    # print('Coste total: ', coste)

    # carrito = {}
    # continuar = True
    # while continuar == True:
    #     artículo = input('Introduce un artículo: ')
    #     precio= float(input(f'Introduce el precio de {artículo}: '))
    #     carrito[artículo] = precio
    #     continuar = input('¿Quieres añadir artículos a la lista? ') == 'Si'
    # costofinal = 0
    # print('Lista de compras')
    # for artículo, precio in carrito.items():
    #     print(artículo, '\t', precio)
    #     costofinal += precio
    # print(f'Coste total: {costofinal}')

#8.- Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir

    