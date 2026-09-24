import time 

# Función que suma los n números naturales 
def sum_of_n(n):
    total_sum = 0
    for number in range(1, n + 1):
        total_sum += number
    return total_sum

dataset = []

for repeticion in range(1, 11):
    n = repeticion * 500  # Puedes subir esto a repeticion * 100000 para tiempos más altos
    
    # Marcador de tiempo de alta precisión
    timestamp_01 = time.perf_counter()
    
    result = sum_of_n(n)
    
    timestamp_02 = time.perf_counter()
    
    # Tiempo transcurrido en microsegundos (µs)
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)
    
    dataset.append((n, elapsed_time, result))

# Imprimir el dataset
for tup in dataset:
    print(tup)