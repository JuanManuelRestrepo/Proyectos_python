def calcular_precios_con_descuento(productos):
    for producto in productos:
        precio = producto["Precio"]
        descuento = producto["descuento"]
        precio_descuento = precio - (precio * (descuento / 100))
        producto["Precio con descuento"] = precio_descuento
        
