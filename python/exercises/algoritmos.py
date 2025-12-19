#Crear un programa que cuente cuántos números hay en una lista.
lista = [10,2,3,4,5,6,8,7,9,10]
contador = 0

for i in lista:
    contador += 1

print(f"la Cantidad de numeros en la lista es {contador}")

#Crear un programa que encuentre el menor número de una lista.

menor = lista[0]

for i in lista:
    if i < menor:
        menor = i
print(f"El numero menor de la lista es {menor}")

#contar cada letra de la palabra
texto = "programacion"
contador = 0

for i in texto:
    contador += 1
    
print(f"la cantidad de palabras que tiene {texto} Son: {contador}")

#cuentra cuantas vocales tiene la palabra
texto = "estructura y algoritmo"
contador = 0
vocales = "aeiouAEIOU"

for i in texto:
    if i in vocales:
        contador += 1
print(f"la cantidad de vocales que contiene la oracion {texto} son {contador}")

#fizz buzz

for i in range(1, 20):
    if i %3 == 0 and i % 5 == 0:
        print("fizz buzz")
    elif i %3 ==0:
        print("buzz")
    elif i % 5 == 0:
        print("fizz")
    else:
        print(i)