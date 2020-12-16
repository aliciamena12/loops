
#21. Leer un número entero y determinar a cuánto es igual al suma de sus dígitos.
num = int(input("Elige un número entero: "))
contador = 0
while num >= 1:
    unidad = int(num % 10)
    num = int(num / 10)
    contador = contador + unidad
print("La suma de los dígitos del número elegido es: " + str(contador))

#22. Leer un número entero y determinar cuántas veces tiene el dígito 1.
num = int(input("Elige un número entero: "))
contador = 0
while num >= 1:
    unidad = int(num % 10)
    num = int(num / 10)
    if unidad == 1:
        contador = contador + 1
print("El número elegido tiene tiene el 1 como dígito " + str(contador) + " veces.")

#23. Leer un número entero y determinar si la suma de sus dígitos es también un número primo.
num = int(input("Elige un número entero: "))
suma = 0
while num >= 1:
    unidad = int(num % 10)
    num = int(num / 10)
    suma = suma + unidad
contador = 0
for number in range(2, suma):
    if int(suma % number) == 0:
        contador = contador + 1
if contador !=0:
    print("La suma de los dígitos del número elegido no es un número primo.")
else:
    print("La suma de los dígitos del número elegido es un número primo.")

#24. Leer un número entero y determinar a cuánto es igual al suma de sus dígitos pares.
num = int(input("Elige un número entero: "))
suma = 0
while num >= 1:
    unidad = int(num % 10)
    num = int(num / 10)
    if unidad == int(unidad / 2) * 2:
        suma = suma + unidad
print("La suma de los dígitos pares del número elegido es: " + str(suma))

#25. Leer un número entero y determinar a cuánto es igual el promedio entero de sus dígitos.
num = int(input("Elige un número entero: "))
suma = 0
contador = 0
while num >= 1:
    unidad = int(num % 10)
    num = int(num / 10)
    contador = contador + 1
    suma = suma + unidad
promedio = int(suma / contador)
print("El promedio entero de los dígitos del número elegido es: " + str(promedio))

#26. Leer un número entero y determinar cuál es el mayor de sus dígitos.
num = int(input("Elige un número entero: "))
x = 0
y = 0
while num > 0:
    x = int(num % 10)
    num = int(num / 10)
    if x > y:
        y = x
print("El dígito mayor del número elegido es: " + str(y))

#27. Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos.
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige un segundo número entero: "))
contador1 = 1
contador2 = 1
while num1 > 10:
    num1 = num1 / 10
    contador1 = contador1 + 1
while num2 > 10:
    num2 = num2 / 10
    contador2 = contador2 + 1
if contador1 > contador2:
    print("El primer número tiene más dígitos que el segundo.")
elif contador2 > contador1:
    print("El segundo número tiene más dígitos que el primero.")
else:
    print("Los dos números tienen la misma cantidad de dígitos.")

#28. Leer 2 números enteros y determinar cual de los dos tiene mayor cantidad de dígitos primos.
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige un segundo número entero: "))
contador1 = 0
contador2 = 0
while num1 >= 1:
    unidad1 = int(num1 % 10)
    num1 = int(num1 / 10)
    if unidad1 == 2 or unidad1 == 3:
        contador1 = contador1 + 1
    for number1 in range (2, (unidad1 - 1)):
        if int(unidad1 % number1) == 0:
            break
        contador1 = contador1 + 1
        break
while num2 >= 1:
    unidad2 = int(num2 % 10)
    num2 = int(num2 / 10)
    if unidad2 == 2 or unidad2 == 3:
        contador2 = contador2 + 1
    for number2 in range (2, (unidad2 - 1)):
        if int(unidad2 % number2) == 0:
            break
        contador2 = contador2 + 1
        break
print("El primer número tiene " + str(contador1) + " dígitos que son primos.")
print("El segundo número tiene " + str(contador2) + " dígitos que son primos.")
if contador1 > contador2:
    print("El primer número tiene más dígitos primos que el segundo número.")
elif contador2 > contador1:
    print("El segundo número tiene más dígitos primos que el primer número.")
else:
    print("Los dos números tienen la misma cantidad de dígitos primos.")

#29. Leer un número entero y determinar a cuánto es igual el primero de sus dígitos.
num1 = int(input("Elige un número entero: "))
while num1 > 10:
    num1 = num1 / 10
unidad = int(num1 % 10)
print("El primer dígito es: " + str(unidad))

#30. Leer un número entero y mostrar todos sus componentes numéricos o sea aquellos para
# quienes el sea un múltiplo.
num = int(input("Elige un número entero: "))
for number in range(1, num):
    if num != int(num / number) * number:
        continue
    print(number)
