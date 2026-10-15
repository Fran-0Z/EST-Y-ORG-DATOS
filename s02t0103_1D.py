from array import array as arr
from s02t0101_1d import print_array

# Crear el array de enteros
my_array = arr('i', [2, 10, 15, 20]) 

print("--- ANTES DE LA INSERCIÓN ---")
print_array(my_array)

# Inserción en el índice 1
my_array.insert(1, 90)

print("--- SIMULAR UN APPEND CON INSERT ---")
# Simular un append insertando al final usando len()
my_array.insert(len(my_array), 9000)

print_array(my_array)