from crear import*
def Eliminar_estudiante(df,archivo):
    df=pd.read_csv(archivo)
    print("ELIMINANDO ESTUDIANTE")
    while True:
        Identificacion=input("Digite el numero de identificacion del estudiante:")
        if Identificacion.isdigit():
            Identificacion=int(Identificacion)
            
            #Si identificacion esta en la columna del data frame devuelve True en esa fila
            if Identificacion in df["Identificacion"].values:
                print("El estudiante se encuentra registrado")
                #Creamos un data frame, con todos los valores del otro data frame excluyendo 
                # la fila de identificacion dada
                df=df[df['Identificacion'] != Identificacion]
                print("Estudiante eliminado con exito")
                #Creamos el data frame
                df.to_csv(archivo, index=False)
                break
            else:
                print("El estudiante no se encuentra registrado")

        else:print("Error, ingrese un numero de identificacion valido")
        break
    while True:
        try:
            respuesta=input("¿Desea eliminar otro estudiante?\n1.si\n2.No \nDigite la opcion:  ")
            if int(respuesta)==1:
                Eliminar_estudiante(df,archivo)
            
            elif int(respuesta) != 1:
                print("Opcion no valida")
                break
        except ValueError:
            print("Error, ingrese una opcion valida")
            