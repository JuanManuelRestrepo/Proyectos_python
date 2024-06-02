Iva=0.19
def calcular_precios_con_iva(productos):
    for producto in productos:
        precio = producto.get("Precio con descuento", producto["Precio"])
        precio_con_iva = precio + (precio * Iva)
        producto["Precio con IVA"] = precio_con_iva
