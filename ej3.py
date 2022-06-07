'''
Crear un arreglo de dos dimensiones de 3 x 3 con números ceros, 
excepto la diagonal principal que debe contener en el mismo orden 
los siguientes elementos 1, 2 y 3.
'''
import numpy as np

matrizCeros = np.zeros((3,3), dtype=int)
print(matrizCeros)

cont = 1
for i in range(3):
    for j in range(3):
        if i == j:
            matrizCeros[i][j] = cont
            cont = cont + 1
print(matrizCeros)
