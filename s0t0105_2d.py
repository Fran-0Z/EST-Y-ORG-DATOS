from array import array as arr

#Impresion de una tabla 
def print_table(inpunt_table):
#Imprimiendo cada elemento 
 for row in inpunt_table:
    for column in row:
        print(column, end=",")
    print("\b ")

table = [
    arr("i",[1,2,3]),
    arr("i",[4,5,6]),
    arr("i",[7,8,9]),
]

print_table(table)

#insercion
row = 1
column = 2
value = 99

#insertar en la fila 1 colum 2 el valor 99
table[row].insert(column, value)

#imprimiendo mensaje 
print("---Despues de la insercion---")
print_table(table)

new_row = arr('i', [100,200,300])
pos = 1
table.insert(pos, new_row)

print ("--- Despues de la insercion de fila---")
print_table(table)

#Eliminacion de elementos
del table[2]

print ("--- Despues de la eliminacion---")
print_table(table)