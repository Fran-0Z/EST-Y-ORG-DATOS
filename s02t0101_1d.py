#Array 
import array as arr

#Creacion de un arreglo
#i: Entero con signo
#i: Entero con signo
#i: Entero con signo
#i: Entero con signo
my_array = arr.array('i', [10, 22, 300,3,7,40,55,80,700,658,952])


#for num in my_array:
 #   print(num)


    #Acceso individual a los elementos
    # print(my_array[0])  # Acceso al primer elemento
    # print(my_array[1])  # Acceso al segundo elemento
    # print(my_array[2])  # Acceso al tercer elemento

print(len(my_array))

#Interaccion por indices
for i in range(len(my_array)):
  if my_array[i] % 2 == 0:
    print(f"Elemento {i+1}: {my_array[i]}")
      