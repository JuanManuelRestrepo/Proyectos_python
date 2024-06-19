import matplotlib.pyplot as plt
from crear import *

def Graficas(df, archivo):
    # Código para generar el gráfico
    aprobados = df[df['Estado'] == 'Aprobado']
    reprobados = df[df['Estado'] == 'Reprobado']
    
    # Crear el gráfico
    fig, ax = plt.subplots()
    ax.bar(['Aprobados', 'Reprobados'], [len(aprobados), len(reprobados)])
    ax.set_ylabel('Cantidad de Estudiantes')
    ax.set_title('Estudiantes Aprobados vs Reprobados')
    
    # Mostrar el gráfico
    plt.show()