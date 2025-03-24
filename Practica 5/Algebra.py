import math

def getDiscriminante(a, b, c):
    return b**2 - 4*a*c

def getRaiz1(a, b, c):
    return (-b + math.sqrt(getDiscriminante(a, b, c))) / (2*a)

def getRaiz2(a, b, c):
    return (-b - math.sqrt(getDiscriminante(a, b, c))) / (2*a)

print("Ingrese los valores de a, b, c: ")
entrada = input()
valores = [float(num) for num in entrada.split()]

if len(valores) != 3:
    print("Debe ingresar exactamente 3 valores para a, b y c.")
else:
    a, b, c = valores
    discriminante = getDiscriminante(a, b, c)

    if discriminante > 0:
        r1 = getRaiz1(a, b, c)
        r2 = getRaiz2(a, b, c)
        print(f"La ecuación tiene dos raíces {r1:.6f} y {r2:.6f}")
    elif discriminante == 0:
        r = getRaiz1(a, b, c)
        print(f"La ecuación tiene una raíz {r}")
    else:
        print("La ecuación no tiene raíces reales")
