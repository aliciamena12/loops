
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
