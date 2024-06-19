from crear import *

def Listar_estudiantes(df,archivo):
    while True:
        print("LISTANDO ESTUDIANTES")
        df=pd.read_csv(archivo)
        opcion=input("Digite una opcion \n1.Listar un estudiantes\n2.Listar todo el archivo\n3.filtrar muchos estudiantes\nDigite la opcion: ")
        if int(opcion) == 1:
            identificacion=input("Digite el numero de identificacion del estudiante: ")
            if identificacion.isdigit():
                identificacion=int(identificacion)
                fila =df.loc[df["Identificacion"]==identificacion]
                print(fila)
            
            else:
                print("La identificacion debe ser un numero")


        elif int(opcion)==2:    
            print("Listado de Estudiantes")
            print(df)
        elif int(opcion)==3:
            estudiantes=[]
            print("Filtrar estudiantes")
            N_estudiantes=input("Digite el numero de estudiantes que desea listar")
            if N_estudiantes.isdigit():
                N_estudiantes=int(N_estudiantes)
                for i in range(N_estudiantes):
                    identificacion=input(f"Digite el numero de identificacion del estudiante {i+1}: ")
                    if identificacion.isdigit():
                        identificacion=int(identificacion)
                        estudiantes.append(identificacion)
                    else:
                        print("La identificacion debe ser un numero")

                #comprueba si cada valor de la columna "Identificacion" está presente en la lista estudiantes
                #Serie booleana
                filtro = df["Identificacion"].isin(estudiantes)
                #creamos el data frame con la variable anterior
                df_filtrado = df[filtro]

                for estudiante in estudiantes:
                    #.tolist convierte la columna seleccionada en una lista de python
                    # el condicional verifica si estudiante no esta creado en lista que se creara con el
                    #tolist() La expresión estudiante not in lista devuelve True si estudiante no está en lista, y False si está en lista.
                    if estudiante not in df["Identificacion"].tolist():
                            print(f"El estudiante con identificación {estudiante} no existe en el registro")
                    else:continue  
                #Verificamos que el data frame que creamos con las identificaciones encontradas no esta vacio
                #si el data frame no esta vacio lo imprimimos
                if not df_filtrado.empty:
                    print(df_filtrado)
                
            else:
                print("El numero de estudiantes debe ser un numero")
                break



