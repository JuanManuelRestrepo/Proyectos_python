from crear import *
def pedir_datos_estudiante(df, archivo,materias): 
    nombre = input("Digite el nombre del estudiante: ")
    while True:
            identificacion = input("Digite el número de identificación: ")
            #comprobamos que la identificación sean solo en valores numericos
            if identificacion.isdigit():
                #convertimos la cadena en un numero enetero
                identificacion = int(identificacion)
                #leemos el data frame
                df = pd.read_csv(archivo)
                columna_identificacion = df['Identificacion']
                #condicional para comprobar que no hayan identificaciones repetidas
                if identificacion in columna_identificacion.values:
                    print("La identificación ya existe.")
                else:
                    break  # Salir del bucle interior si la identificación es válida y no existe
            else:
                print("Identificación inválida. Por favor, ingrese solo números.")

        # Si llegamos aquí, la identificación es válida y única
        # Podemos proceder a pedir otros datos del estudiante, guardar en el DataFrame, etc.

    carrera = input("Digite la carrera del estudiante: ")
    notas = {}
    #Ciclo para pedir las materias 
    N_materias=0
    for materia in materias:
        if materia == "Nota Final":
                continue
        if materia == "Estado":
            continue
        while True:
            try:
                #pedir la nota la la materia en el bucle
                nota_materia = float(input(f"Digite la nota de la materia {materia}: "))
                if 0.0 <= nota_materia <= 5.0:  # Suponiendo notas entre 0 y 5
                    #la key del diccionario sera la coolumna materia y su valor correspondera a la nota dada, todo se guarda dentro del diccionario
                    notas[materia] = nota_materia
                    N_materias+=1
                    break
                else:
                    print("La nota debe estar entre 0.0 y 5.0")
            except ValueError:
                print("Por favor, ingrese un valor numérico para la nota.")
    # Calcular la suma de las notas
    suma_notas = sum(notas.values())/N_materias
    if suma_notas >= 3.0:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    nueva_fila = {'Nombre': nombre, 'Identificacion': identificacion, 'Carrera': carrera}
    # Aquí podrías agregar más campos como las notas de las materias
    nueva_fila.update(notas)
    # Agregar la Nota Final al diccionario
    nueva_fila['Nota Final'] = suma_notas
    nueva_fila['Estado'] = estado
    # Crear un DataFrame temporal con la nueva fila
    nueva_fila_df = pd.DataFrame([nueva_fila])

    # Concatenar el nuevo DataFrame con el DataFrame principal `df`
    df = pd.concat([df, nueva_fila_df], ignore_index=True)
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv(archivo, index=False)

