import math

def promedio(numeros):
    return sum(numeros) / len(numeros)

def desviacion(numeros):
    prom = promedio(numeros)
    suma_cuadrados = sum((x - prom) ** 2 for x in numeros)
    return math.sqrt(suma_cuadrados / (len(numeros) - 1))

print("Ingrese 10 números:")
entrada = input()
numeros = [float(num) for num in entrada.split()]

if len(numeros) != 10:
    print("Debe ingresar exactamente 10 números.")
else:
    prom = promedio(numeros)
    desv = desviacion(numeros)

    print(f"El promedio es {prom:.2f}")
    print(f"La desviación estándar es {desv:.6f}")
