
#1. Leer un número entero y mostrar todos los enteros comprendidos entre 1 y el número leído.
num1 = int(input("Elige un númer entero: "))
num2 = 0
while num1 != num1:
    num2 = num2 + 1
    print(num1)


#2. Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.
num = int(input("Elige un número entero: "))
for number in range(1, num):
    if number != int(number / 2) * 2:
        continue
    print(number)


#3. Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1
# y el número leído.
num = int(input("Elige un número entero: "))
for number in range(1, num):
    if num != int(num / number) * number:
        continue
    print(number)

#4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige un segundo número entero: "))
for number in range(num1, num2):
    if number == num1:
        continue
    print(number)

#5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige un segundo número entero: "))
for number in range(num1, num2):
    unidad = int(number % 10)
    if unidad != 4:
        continue
    print(number)

#6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada
# uno de los dígitos.
num = int(input("Elige un número entero de tres dígitos: "))
centenas = int(num / 100)
decenas = int(num / 10) % 10
unidad = int(num % 10)
if num >= 100 and num <= 999:
    for number in range(1, centenas):
        print(number)
    print(centenas)
    for number in range(1, decenas):
        print(number)
    print(decenas)
    for number in range(1, unidad):
        print(number)
    print(unidad)
else:
    print("El número elegido no tiene tres dígitos.")

#7. Mostrar en pantalla todos los enteros comprendidos entre 1 y 100.
num = 0
while num != 100:
    num = num + 1
    print(num)

#8. Mostrar en pantalla todos los pares comprendidos entre 20 y 200.
for number in range(20, 200):
    if number != int(number / 2) * 2 or number == 20:
        continue
    print(number)

#9. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.
for number in range(25, 205):
    unidad = int(number % 10)
    if unidad != 6:
        continue
    print(number)

#10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros
# comprendidos entre 1 y el número leído.
num = int(input("Elige un número entero de tres dígitos: "))
contador = 0
for number in range(1, num):
    contador = contador + number
print(contador)

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

#31. Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números
# terminados en 5.
num = int(input("Elige un número entero: "))
suma = 0
contador = 0
for number in range(num, 0, -1):
    if number == int(number / 5) * 5:
        contador = contador + 1
        suma = suma + number
promedio = int(suma / contador)
print("El promedio de los números terminados en 5 desde el número elegido a 0 es: " + str(promedio))

#32. Leer números hasta que digiten 0 y determinar a cuanto es igual el promedio entero de los
# número primos leídos.
x = int(input("Elige un número entero: "))
suma = 0
contador = 0
for num in range((x-1), 1, -1):
    for number in range((num - 1), 1, -1):
        if int(num % number) == 0:
            is_prime = False
            break
        is_prime = True
    if is_prime == True:
        suma = suma + num
        contador = contador + 1
promedio = int(suma / contador)  
print("El promedio entero de los números primos desde el número elegido hasta 0 es: " + str(promedio))

#33. Si 32768 es el tope superior para los números entero cortos, determinar cuál es el número
# primo mas cercano por debajo de él.
for num in range((32768-1), 0, -1):
    for number in range((num - 1), 2, -1):
        if int(num % number) == 0:
            is_prime = False
            break
        is_prime = True
    if is_prime == True:
        print("El número primo más cercano por debajo a 32768 es: " + str(num))
        break

#34. Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1.
contador = 0
for number in range(10, 0, -1):
    contador = contador + 1
    print(contador)

#35. Leer dos números enteros y determinar a cuánto es igual el producto mutuo del primer dígito
de cada uno.
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige un segundo número entero: "))
while num1 > 10:
    num1 = num1 / 10
unidad1 = int(num1 % 10)
while num2 > 10:
    num2 = num2 / 10
unidad2 = int(num2 % 10)
producto = unidad1 * unidad2
print("El producto del primer dígito de cada número es: " + str(producto))

#36. Mostrar en pantalla la tabla de multiplicar del número 5.
num = 1
for number in range(1, 11):
    num = number * 5
    print(str(5) + " x " + str(number) + " = " + str(num))

#37. Generar todas las tablas de multiplicar del 1 al 10.
num = 1
serie = 1
for multiplicador in range(1, 11):
    print("Tabla de multiplicar del " + str(serie))
    for number in range(1, 11):
        num = number * serie
        print(str(multiplicador) + " x " + str(number) + " = " + str(num))
        if serie == 11:
            break
    serie = serie + 1

#38. Leer un número entero y mostrar en pantalla su tabla de multiplicar.
x = int(input("Elige un número entero: "))
num = 1
for number in range(1, 11):
    num = number * x
    print(str(x) + " x " + str(number) + " = " + str(num))

#39. Se define la serie de Fibonacci como la serie que comienza con los dígitos 1 y 0 y va sumando
# progresivamente los dos últimos elementos de la serie, así:
# 0 1 1 2 3 5 8 13 21 34....... Utilizando el concepto de ciclo generar la serie de Fibonacci hasta
# llegar o sobrepasar el número 10000.
x = 0
y = 1
for number in range(0, 20):
    print(str(x) + ", " + str(y))
    x = x + y
    y = x + y
    if x >= 10000:
        break

#40. Leer un número de dos dígitos y determinar si pertenece a la serie de Fibonacci.
num = int(input("Elige un número entero de dos dígitos: "))
x = 0
y = 1
if num >= 10 and num <= 99:
    for number in range(0, 20):
        x = x + y
        y = x + y
        if x == num or y == num:
            print("El número elegido pertenece a la serie de Fibonacci.")
            break
    if x != num and y != num:
        print("El número elegido no pertenece a la serie de Fibonacci.")
else:
    print("El número elegido no tiene dos dígitos.")

#41. Determinar a cuánto es igual la suma de los elementos de la serie de Fibonacci entre 0 y 100.
x = 0
y = 1
suma = 0
for number in range(0, 20):
    suma = suma + x + y
    print(str(x) + ", " + str(y))
    x = x + y
    y = x + y
    if x >= 100:
        break
print("La suma de los elementos de la serie de Fibonacci entre 0 y 100 es: " + str(suma))

# 42. Determinar a cuánto es igual el promedio entero de los elementos de la serie de Fibonacci
# entre 0 y 1000.
x = 0
y = 1
suma = 0
contador = 0
for number in range(0, 20):
    suma = suma + x + y
    contador = contador + 2
    print(str(x) + ", " + str(y))
    x = x + y
    y = x + y
    if y >= 1000:
        break
promedio = int(suma / contador)
print("El promedio de los elementos de la serie de Fibonacci entre 0 y 1000 es: " + str(promedio))

#43. Determinar cuántos elementos de la serie de Fibonacci se encuentran entre 1000 y 2000.
x = 0
y = 1
suma = 0
contador = 0
for number in range(0, 20):
    x = x + y
    y = x + y
    if x >= 1000 and x <= 2000:
        contador = contador + 1
    elif y >= 1000 and y <= 2000:   
        contador = contador + 1
print("Entre el número 1000 y el 2000, en la serie de Fibonacci hay " + str(contador) + " números.")

#44. Leer un número y calcularle su factorial.
num = int(input("Elige un número entero: "))
factorial = 1
for number in range(1, (num + 1)):
    factorial = factorial * number
print(factorial)

#45. Leer un número y calcularle el factorial a todos los enteros comprendidos entre 1 y el número
# leído.
num = int(input("Elige un número entero: "))
factorial = 1
for number in range(1, (num + 1)):
    factorial = factorial * number
    print(factorial)

#46. Leer un número entero y calcular el promedio entero de los factoriales de los enteros
# comprendidos entre 1 y el número leído.
num = int(input("Elige un número entero: "))
factorial = 1
suma = 0
for number in range(1, (num + 1)):
    factorial = factorial * number
    suma = suma + factorial
promedio = int(suma / num)
print(promedio)

#47. Leer un número entero y calcular a cuánto es igual la sumatoria de todos los factoriales de los
# números comprendidos entre 1 y el número leído.
num = int(input("Elige un número entero: "))
factorial = 1
suma = 0
for number in range(1, (num + 1)):
    factorial = factorial * number
    suma = suma + factorial
print(suma)

#48. Utilizando ciclos anidados generar las siguientes parejas de enteros
#        0 1
#        1 1
#        2 2
#        3 2
#        4 3
#        5 3
#        6 4
#        7 4
#        8 5
#        9 5
y = 0
for number in range(0, 10):
    if number == int(number / 2) * 2:
        y = y + 1
    print(str(number) + " " + str(y))

#49. Utilizando ciclos anidados generar las siguientes ternas de números
#        1 1 1
#        2 1 2
#        3 1 3
#        4 2 1
#        5 2 2
#        6 2 3
#        7 3 1
#        8 3 2
#        9 3 3
x = 1
y = 0
for number in range(1, 10):
    y = y + 1
    if y == 4:
        x = x + 1
    if y == 4:
        y = 1
    print(str(number) + " " + str(x) + " " + str(y))

#50. Utilizando ciclos anidados generar las siguientes parejas de números
#        0 1
#        1 1
#        2 1
#        3 1
#        4 2
#        5 2
#        6 2
#        7 2
y = 0
for number in range(0, 8):
    if number == int(number / 4) * 4:
        y = y + 1
    print(str(number) + " " + str(y))
