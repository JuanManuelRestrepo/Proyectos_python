print("BIENVENIDO")
N_productos=int(input("Digite el numero de productos: "))
productos=[]
def IngresarProductos():
    for i in range(1,N_productos+1):
            precio=float(input(f"Digite el precio del producto {i}: "))
            descuento=float(input(f"Digite el descuento del producto {i} en porcentaje:"))
            dic_producto={"Precio": precio , 
                        "descuento": descuento,}
            productos.append(dic_producto)
    return productos
