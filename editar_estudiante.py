from crear import *
def editar_estudiante(df, archivo,materias):
    df=pd.read_csv(archivo) 
    print("EDITANDO ESTUDIANTE")
    identificacion = input("Digite el número de identificación: ")
    if identificacion.isdigit():  # Verifica si la identificación es numérica
        identificacion = int(identificacion)
        #Comprobamos que la identificacion se encuentre dentro del data frame
        fila = df.loc[df['Identificacion'] == identificacion]
        #Si la fila no esta vacia procedemos a pedir los datos para editar al estudiante
        if not fila.empty:
            #Pedimmos los datos del nombre y la carrera
            print(f"Editando estudiante con identificación {identificacion}")
            nombre = input("Digite el nuevo nombre del estudiante: ")
            carrera = input("Digite la nueva carrera del estudiante: ")
            # Actualizar datos del estudiante
            #Accedemoa al columna y fila que sea igual a la identificacion buscada y depespues entramos al nombre y lo actualiazamos, igual con la carrera
            df.loc[df['Identificacion'] == identificacion, 'Nombre'] = nombre
            df.loc[df['Identificacion'] == identificacion, 'Carrera'] = carrera
            N_materias=0
            total_notas=0
            # Actualizar notas
            for materia in materias:
                if materia == "Nota Final":
                    continue
                if materia == "Estado":
                    continue
                #Comprobando que las notas esten dentro del rango
                while True:
                    nueva_nota = float(input(f"Digite la nueva nota de la materia {materia}: "))
                    if 0.0<= nueva_nota <= 5.0:
                        #por cada materia agregamos la nota en la columna correspondiente
                        df.loc[df['Identificacion'] == identificacion, materia] = nueva_nota
                        #Aumentamos en uno por cada materia para calcular la Nota final de todas las materias
                        N_materias+=1
                        #Sumamos las notas para calcular la Nota final
                        total_notas+=nueva_nota
                        break
                    else:
                        print("Digite una nota valida")

            if N_materias>0:
                #Calculamos la nota final
                Nota_Final=total_notas/N_materias
                #Agregamos a la columna Nota Final el valor de la Nota Final 
                df.loc[df['Identificacion'] == identificacion, "Nota Final" ] = Nota_Final
                if Nota_Final >= 3.0:
                    #Condicional para saber si el estudiante aprobo
                    df.loc[df['Identificacion'] == identificacion, 'Estado'] = 'Aprobado'
                else:
                    df.loc[df['Identificacion'] == identificacion, 'Estado'] = 'Reprobado'
            else:
                print("No hay Materias registradas")

            # Guarda los cambios en el archivo CSV
            df.to_csv(archivo, index=False)
            print("¡Información del estudiante actualizada exitosamente!")
        else:
            print(f"No se encontró ningún estudiante con identificación {identificacion}")  
    else:
        print("Identificación no valida")
        #Menu para volver a editar
    while True:
        opcion=input("Digite una opcion\n1.Seguir editando\n2.Salir\nDigite la opcion ")   
        if int(opcion)==1:
            #Aplicación de la recursividad
            editar_estudiante(df, archivo,materias)
        elif int(opcion)>1 or int(input)<1:
            break
        else:
            break