import pandas as pd
import os
#funcion para crear o leer un csv
def crearCSV():
    #variables donde almacenaramos los datos que utilizaremos
    materias=[]
    nombre_archivo = input("Digite el nombre que llevará el archivo: ")
    extension = ".csv"
    #nombre final del archivo csv
    archivo = nombre_archivo + extension
    # si el archivo no existe creo uno nuevo con las siguientes columnas
    if not os.path.isfile(archivo):
        # Si el archivo no existe, crea un DataFrame vacío
        print("EL archivo no existe y sera creado")
        N_materias=input("Digite el numero de materias que ven los estudiantes")
        for i in range(int(N_materias)):
            nombre=input(f"Digite el nombre de la meteria {i+1}: ")
            materias.append(nombre)
        #Creamos el data frame con las columnas respectivas
        df = pd.DataFrame(columns=['Nombre', 'Identificacion', 'Carrera',]+ materias)
        # Creamos el data csv con el data frame creado anteriormente y con el nombre dle archivo, y este no tendra el indice natural que viene por defecto
        df.to_csv(archivo, index=False)
        return df, archivo, materias
    else: 
        print("El archivo ya existe y sera leido")
        #Leemos el archivo en caso de que elarchivo ya exista
        df=pd.read_csv(archivo)
        #nos traera una lista, iterav por cada columna dentro del data frame y almacena en la lista aquellas columnas que no sean las indicadas en esta linea de codigo
        materias = [col for col in df.columns if col not in ['Nombre', 'Identificacion', 'Carrera']]
        return df, archivo, materias  # Devuelve el DataFrame y el nombre del archivo creado
