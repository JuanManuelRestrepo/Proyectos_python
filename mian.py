import entrada_productos
import calculo_descuento
import calculo_iva
import mostrarProductos

def main():
    productos = entrada_productos.IngresarProductos()
    while True:
        try:  
            desicion=input("Opciones\n1.Calcular descuento\n2.Calcular valor con Iva\n3.Mostrar datos\nDigite la opcion: ")
            if int(desicion)==1:   
                calculo_descuento.calcular_precios_con_descuento(productos)
                mostrarProductos.mostrar_productos(productos)
            elif int(desicion)==2:
                calculo_iva.calcular_precios_con_iva(productos)
                mostrarProductos.mostrar_productos(productos)
            elif int(desicion)==3:
                mostrarProductos.mostrar_productos(productos)
        except ValueError:
             print("debe ingresar números en el rango")

if __name__ == "__main__":
    main()
