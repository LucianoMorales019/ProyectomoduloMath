# Este es mi primer modulo de funciones basicas de matematicas
# El objetivo es aprender a crear modulos y funciones en Python
# Y poder importarlas en otros scripts
# Sin la necesidad de copiar y pegar el codigo nuevamente


def es_par(numero):
    """Retorna True si el número es par, False si es impar."""
    return numero % 2 == 0


def factorial(n):
    """Retorna el factorial de un número n calculado con un bucle."""
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado


def promedio(lista_numeros):
    """Retorna el promedio aritmético de una lista de números."""
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

PI = 3.14159
def area_circulo(radio):
    """Calcula el área de un círculo (PI * radio^2) desde cero."""
    return PI * (radio ** 2)


if __name__ == "__main__":
    print("----- PRUEBAS INTERNAS DE MI_MATEMATICA.PY -----")
    print(f"PI utilizado: {PI}")
    print(f"¿Es par el 8?: {es_par(8)}")
    print(f"Factorial de 4: {factorial(4)}")
    print(f"Promedio de [10, 20, 30]: {promedio([10, 20, 30])}")
    print(f"Área del círculo con radio 2: {area_circulo(2)}")