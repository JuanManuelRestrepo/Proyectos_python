from crear import *
import Agregar_estudiante
import editar_estudiante 
import eliminar_estudiante
import listar_estudiantes
import Graficas

def Menu():
    #llamamos la funcion de crear csv y retornamos los valores necesarios para manipular los datos
    df,archivo,materias=crearCSV()
    #menu de opciones para gregar estudiantes
    while True:
        principal_opcion=input("DIGITE UNA OPCION\n1.Agregar estudiante\n2.Editar Estudiante\n3.Eliminar Estudiante\n4.Listar Estudiante\n5.Graficos y Estadisticas\nOPCION: ")
        if int(principal_opcion)==1:
            while True:
                opcion=input("1.agregar Dinamicamente\n2.Agregar Grupo definido\n3.Salir\nDigite una opcion: ")
                if int(opcion)==1:
                    while True:
                        subOpcion=input("1.Agregar\n2.Salir\nDigite una opcion: ")
                        if int(subOpcion)==1: 
                            #llamado a la funcion para agregar nuevo estudiantes al archivo
                            Agregar_estudiante.pedir_datos_estudiante(df,archivo, materias)
                        else:
                            break
                elif int(opcion)==2:
                    #agregar estudiantes masivamente por grupo definido
                    N_estudiantes=input("Digite el numero de estudiantes del grupo")
                    for k in range(int(N_estudiantes)):
                        print(f"ESTUDIANTE {k+1}")
                        #llamado a la funcion para agregar nuevo estudiantes al archivo
                        Agregar_estudiante.pedir_datos_estudiante(df,archivo, materias)
                    break
        elif int(principal_opcion)==2:
            #Llamado a la funcion para editar estudiante
            editar_estudiante.editar_estudiante(df,archivo, materias)
        elif int(principal_opcion)==3:
            eliminar_estudiante.Eliminar_estudiante(df,archivo)
        elif int(principal_opcion)==4:
            listar_estudiantes.Listar_estudiantes(df,archivo)
        elif int(principal_opcion)==4:
            Graficas.Graficas(df,archivo)

Menu()
