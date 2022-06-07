'''
Crear un arreglo de dos dimensiones de tamaño 3 x 3, 
con elementos aleatorios de números enteros del 0 al 100.
'''
import numpy as np
import random

print("Bienvenidos a la bi-dimensión")
matriz = np.diag([1,1,1])
print(matriz)

for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(0,100)
        
print(matriz)

#Promedio de los elementos.
acumulador = 0
for i in range(3):
    for j in range(3):
        acumulador = acumulador + matriz[i][j]
        
promedio = acumulador / 9
print(f"suma: {acumulador}")
print(f"promedio: {promedio}")

#Suma de los elementos.
sum2 = matriz.sum()
print(f"suma 2: {sum2}")

#Mostrar el elemento mayor y menor.
mayor = 0
menor = 100
for i in range(3):
    for j in range(3):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]

print(f"mayor: {mayor}")
print(f"menor: {menor}")

#Mostrar sólo los elementos de la diagonal principal.
print(".....DIAGONAL.....")
for i in range(3):
    for j in range(3):
        if i == j:
            print(matriz[i][j])

