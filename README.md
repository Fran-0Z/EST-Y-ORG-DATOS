# EST-Y-ORG-DATOS

"""
Escribir un programa que calcule la suma de los N números naturales.
Por ejemplo, si n = 100, el programa calculará la suma del 1 al 100.
"""

import time

# Marca de tiempo
start_time = time.time()

n = 100
suma = 0

# Ciclo for para sumar los números del 1 hasta n
for number in range(1, n + 1):
    suma += number

print(f"La suma de los números del 1 al {n} es: {suma}")
print(f"Tiempo de ejecución: {time.time() - start_time:.6f} segundos")
