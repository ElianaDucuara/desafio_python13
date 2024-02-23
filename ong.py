# Función para calcular el factorial de un número
def calcular_factorial(n):
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Función para calcular la productoria de una lista de números
def calcular_productoria(lista):
    productoria = 1
    for numero in lista:
        productoria *= numero
    return productoria

# Función de control para realizar los cálculos basados en argumentos variables
def calcular(**kwargs):
    resultados = []
    for clave, valor in kwargs.items():
        if 'fact_' in clave:
            resultado = calcular_factorial(valor)
            resultados.append(f"El factorial de {valor} es {resultado}")
        elif 'prod_' in clave:
            resultado = calcular_productoria(valor)
            resultados.append(f"La productoria de {valor} es {resultado}")
    return resultados

# Ejemplo de uso de la función calcular
def main():
    resultados = calcular(fact_1=5, prod_1=[3,6,4,2,8], fact_2=6)
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
