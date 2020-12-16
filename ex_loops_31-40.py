
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
