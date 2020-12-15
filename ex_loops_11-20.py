
#11. Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos
# entre un dígito y otro.
num = int(input("Elige un número entero de dos dígitos: "))
decenas = int(num / 10)
unidad = int(num % 10)
if num >= 10 and num <= 99:
    for number in range(decenas, unidad):
        if number == decenas:
            continue
        print(number)
else:
    print("El número elegido no tiene tres dígitos.")

#12. Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.
num = int(input("Elige un número entero de tres dígitos: "))
contador = 0
while num >= 1:
    unidad = int(num % 10)
    num = int(num / 10)
    if unidad == 1:
        contador = contador + 1
print("El número elegido tiene " + str(contador) + " con el dígito 1.")

#13. Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.
num = int(input("Elige un número entero: "))
for number in range(1, num):
    if number != int(number / 5) * 5:
        continue
    print(number)

#14. Mostrar en pantalla los primeros 20 múltiplos de 3.
num = 3
contador = 0
while contador < 20:
    contador = contador + 1
    print(num * contador)

#15. Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.
num = 3
contador = 0
suma = 0
while contador < 20:
    contador = contador + 1
    suma = suma + int(num * contador)
print(suma)


#16. Mostrar en pantalla el promedio entero de los n primeros múltiplos de 3 para un número n
# leído.
num = int(input("Elige un número entero: "))
num1 = 3
contador = 0
suma = 0
while contador < num:
    contador = contador + 1
    suma = suma + int(num1 * contador)
    promedio = int(suma / contador)
print(promedio)

# 17. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y
# primeros múltiplos de 5 para valores de x y y leídos.
numx = int(input("Elige un número entero: "))
numy = int(input("Elige un número entero: "))
mult2 = 2
mult5 = 5
contadorx = 0
contadory = 0
sumax = 0
sumay = 0
while contadorx < numx:
    contadorx = contadorx + 1
    sumax = sumax + int(mult2 * contadorx)
    promediox = int(sumax / contadorx)
print(promediox)
while contadory < numy:
    contadory = contadory + 1
    sumay = sumay + int(mult5 * contadory)
    promedioy = int(sumay / contadory)
print(promedioy)
if promediox > promedioy:
    print("El primer número tiene un promedio de múltiplos de 2 más alto que el segundo con múltiplos de 5.")
elif promediox < promedioy:
    print("El segundo número tiene un promedio de múltiplos de 5 más alto que el primero con múltiplos de 2.")
else:
    print("Los dos tienen el mismo promedio de multiplos de 2 y 5 respectivamente.")

#18. Leer dos números enteros y mostrar todos los múltiplos de 5 comprendidos entre el menor y el
# mayor.
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige un número entero: "))
if num1 < num2:
    for number in range(num1, num2):
        if number != int(number / 5) * 5:
            continue
        print(number)
elif num2 < num1:
    for number in range(num1, num2):
        if number != int(number / 5) * 5:
            continue
        print(number)   
else:
    print("Los dos números elegidos son iguales.")

#19. Leer un número entero y determinar si es primo.
num = int(input("Elige un número entero: "))
contador = 0
for number in range(2, (num-1)):
    if int(num % number) == 0:
        contador = contador + 1
if contador !=0:
    print("El número elegido no es un número primo.")
else:
    print("El número elegido es un número primo.")


#20. Leer un número entero y determinar cuántos dígitos tiene.
num = int(input("Elige un número entero: "))
contador = 1
while num >= 10:
    num = num / 10
    contador = contador + 1
print("El número elegido tiene " + str(contador) + " dígitos.")
