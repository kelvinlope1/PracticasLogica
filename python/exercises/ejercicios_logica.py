#determinar si un numero es par o impar
# declaracion de una variable para alojar el valor 
a = 5

#condicional que hace el calculo donde con para que el valor sea dividido por 2 para saber si es par o impar
if a % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

#determinar el numero mayor entre dos numeros ingresados por el usuario

#controlador de errores 
try:
    
    #declaracion de variables para ingresar datos por el usuario
    ingresar_numero = float(input("Ingresar un primer valor:"))
    ingresar_numero2 = float(input("Ingresar un segundo valor:"))
    ingresar_numero3 = float(input("Ingresar un tercer valor:"))

    #condicionales para determinar si los datos ingresados son iguales o mayores
    if ingresar_numero == ingresar_numero2 == ingresar_numero3:
        print("Todos los numeros Son iguales")
    elif ingresar_numero > ingresar_numero2 and ingresar_numero > ingresar_numero3:
        print("El numero mayor es:", ingresar_numero)
    elif ingresar_numero2 > ingresar_numero and ingresar_numero2 > ingresar_numero3:
        print("El numero mayor es:", ingresar_numero2)
    elif ingresar_numero3 > ingresar_numero and ingresar_numero3 > ingresar_numero2:
        print("El numero mayor es:", ingresar_numero3)
    else:
        print("hay mas de un numero mayor")
        # cierre del controlador de errores con mensaje si el usuario intenta ingresar datos que no sean numeros
except ValueError:
    print("Error: Solo se aceptan valor en numeros")
    
valor_inicial = int(input("ingresa el valor inicial:"))
Valor_suma = int(input("ingresar numero para sumar: "))
valor_final = int(input("ingresa valor Final: "))
for x in range(valor_inicial, valor_final, Valor_suma ):
    print(x)
    
    
#calcular edad
try:    
    registrar_nombre = input("Nombre:")
    edad = int(input("Registrar la edad: "))
    entreda = 1000
    
    if edad >= 60:
        resultado = entreda * 0.10
        pagar_entreda = 1000 - resultado
        print("puedes pasar con descuento del 10%")
        print(f"Total a pagar de entreda es {pagar_entreda}")
    elif edad >= 40:
        resultado =entreda * 0.005
        pagar_entreda = 1000 - resultado
        print("Puedes entrar pero con un descuento del 5%")
        print(f"Total a Pagar de entreda es {pagar_entreda}")
    elif edad >  18:
        print("Puedes pasar Felicidades")
    else:
        print("No puedes entrar no cumples con la edad Suficiente")
        
except ValueError:
    print("A sucedido algun error Favor de intentar de nuevo")