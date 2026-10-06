# Creando las listas de estudiantes 
students_list_01 = ['kevin', 'musculoso', 'becerro', 'alvin']
students_list_02 = ['piglet', 'fran', 'mowgli', 'kiyo']

# Verificando la presencia de un estudiante 
def check_student(input_student, students_list):
    for student in students_list:
        if student == input_student:
            print("✅Estudiante encontrado")
            return student
            
    # El caso "no encontrado" va fuera del bucle for
    print("❌Estudiante no encontrado")
    return None

# Probando el algoritmo 
check_student('kevin', students_list_01)