import sys

# Diccionario de prueba con los precios de los productos
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtrar_productos(precios, umbral, comparacion='mayor'):
    # Filtrar los productos según el umbral y la condición (mayor o menor)
    if comparacion == 'mayor':
        # Filtrar productos con precio mayor que el umbral
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio > umbral}
    elif comparacion == 'menor':
        # Filtrar productos con precio menor que el umbral
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio < umbral}
    else:
        # En caso de que la operación no sea válida
        return "Lo sentimos, no es una operación válida"

    # Devolver los nombres de los productos filtrados
    return ', '.join(productos_filtrados.keys())

def main():
    # Leer argumentos
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Uso: python filtro.py <umbral> [mayor|menor]")
        return

    # Umbral de precio
    umbral = int(sys.argv[1])

    # Comprobamos si hay un segundo argumento para la comparación
    comparacion = 'mayor'  # Valor por defecto
    if len(sys.argv) == 3:
        comparacion = sys.argv[2]

    # Obtener el resultado del filtro
    resultado = filtrar_productos(precios, umbral, comparacion)

    # Imprimir el resultado
    print(f"Los productos {comparacion} al umbral son: {resultado}")
    

if __name__ == "__main__":
    main()
