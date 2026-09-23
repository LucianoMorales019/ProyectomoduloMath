# El objetivo de este scrip es demostrar como importar y utilizar un modulo propio de funciones matematicas
# Para ello se creo un modulo llamado modulomath.py que contiene funciones para calcular:
#  si un número es par, el factorial de un número, el promedio de una lista de números y el área de un círculo.
import ModuloMath

print("--- EJECUCIÓN DEL PROGRAMA PRINCIPAL ---")

numero_evaluar = 10
resultado_par = ModuloMath.es_par(numero_evaluar)
print(f"¿El número {numero_evaluar} es par?: {resultado_par}")

numero_factorial = 5
resultado_factorial = ModuloMath.factorial(numero_factorial)
print(f"El factorial de {numero_factorial} es: {resultado_factorial}")

lista_datos = [4, 8, 15, 16, 23, 42]
resultado_promedio = ModuloMath.promedio(lista_datos)
print(f"El promedio de la lista {lista_datos} es: {resultado_promedio}")

radio_circulo = 3
resultado_area = ModuloMath.area_circulo(radio_circulo)
print(f"El área del círculo con radio {radio_circulo} es: {resultado_area}")