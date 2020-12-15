
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