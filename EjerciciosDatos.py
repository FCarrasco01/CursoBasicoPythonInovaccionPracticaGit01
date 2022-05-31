# Ejercicio 1 Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

    #    print('¡Hola Mundo!')

#Ejercicio 2 Hola mundo en una variable y printearla

    #    Ejercicio2= 'Hola Mundo'
    #    print(Ejercicio2)

#Ejercicio 3 Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

    #     NombreEjercicio3 = input('¡Hola!, ¿cómo te llamas? ')
    #     print(NombreEjercicio3) 

    #4.- Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética .

    #    print(((3+2)/(2*5))**2)

#5.- Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

    #   Ej5HORAS = (input('¿Cuántas horas laboró hoy? Solo coloque el número: '))
    #   Ej5CostoPorHora = 45
    #   Ej5Paga = int(Ej5HORAS)*Ej5CostoPorHora

    #   print(Ej5HORAS)
    #   print(f'${Ej5Paga}.00 MXN')


#6.- Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n . La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

    # Ej6N = input('Inserte valor de n: ')
    # Ej6suma = ((int(Ej6N)*(int(Ej6N)+1))/2)

    # print(Ej6suma)

#7.- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

    #Nota: si usas INT en input y meten decimales, va a dar error. Usar FLOAT y después redonder al entero más cercano.
        
    # Ej7Peso = float(input('¿Cuál es su peso en kilogramos? Solo la cantidad, sin unidades: '))
    # Ej7Estatura = float(input('¿Cuál es su estatura en metros? Solo la cantidad, sin unidades: '))

    # Ej7IMC = round(Ej7Peso/((Ej7Estatura)**2),2)

    # print(f'Tu índice de masa corporal es {Ej7IMC}')

#8.- Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.


    # print('Calculadora de cociente y resto, n es el dividendo y m el divisor')
    # Ej8n1 = int(input('Ingresa n: '))
    # Ej8n2 = int(input('Ingresa m: '))

    # print('(Cociente,Resto)')
    # print(divmod(Ej8n1,Ej8n2)) #divmod es para una tupla de cociente y resto dada (x,y)
    
#9.- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual (compuesto) y el número de años, y muestre por pantalla el capital obtenido en la inversión.
    # print('CALCULADORA DE INVERSIONES')
    # print('Solo coloque números, sin signos ni unidades')

    # Ej9Capital = float(input('Cantidad a invertir: '))
    # Ej9IA = float(input('¿Cual es el interés anual?: '))
    # Ej9Tiempo = float(input('¿Por cuántos años planea invertir?: '))

    # Ej9Monto = round((Ej9Capital*((1 + (Ej9IA/100))**Ej9Tiempo)),2)
    # Ej9IntObtenido =  Ej9Monto-Ej9Capital

    # print(f'Su capital final será ${Ej9Monto} MXN')
    # print(f'La cantidad de interés obtenido es de ${Ej9IntObtenido} MXN')

#10.- Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

    # print('CALCULADORA DE PESO DE PAQUETE')
    # Ej10Pp= 112
    # Ej10Pm= 75
    # Ej10Vp = float(input('Cantidad de payasos vendidos: '))
    # Ej10Vm= float(input('Cantidad de muñecas vendidas: '))
    # Ej10R = (Ej10Pp*Ej10Vp)+(Ej10Pm*Ej10Vm)

    # print(f'El peso total del paquete es de {Ej10R} g')

#11.- Me dió flojera

#12.- Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

    # Ej12PBarras=3.49
    # Ej12BVendidas= float(input('Cantidad de barras vendidas que no son del día: '))
    # Ej12PCDesc= ((Ej12PBarras*Ej12BVendidas)*2/5)
    # Ej12Desc = (Ej12PBarras*Ej12BVendidas)-Ej12PCDesc


    # print('El precio de una barra fresca es de $3.49')
    # print(f'Descuento = ${Ej12Desc}')
    # print(f'Costo final = ${Ej12PCDesc}')

    # print('GRACIAS POR SU COMPRA <3')

