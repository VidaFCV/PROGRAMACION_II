import math

def area(*args):
    if len(args) == 1:  # Círculo
        radio = args[0]
        return math.pi * radio ** 2
    elif len(args) == 2 and isinstance(args[1], (int, float)):  # Rectángulo
        base, altura = args
        return base * altura
    elif len(args) == 3 and isinstance(args[2], str):  # Triángulo rectángulo
        baseTR, alturaTR, _ = args
        return (baseTR * alturaTR) / 2
    elif len(args) == 3:  # Trapecio
        base1, base2, altura = args
        return ((base1 + base2) * altura) / 2
    elif len(args) == 2 and isinstance(args[1], str):  # Pentágono
        lado, _ = args
        return (lado ** 2) * math.sqrt(25 + 10 * math.sqrt(5)) / 4
    else:
        raise ValueError("Parámetros inválidos para calcular el área")

if __name__ == "__main__":
    print("Círculo:", area(5))
    print("Rectángulo:", area(4, 6))
    print("Triángulo rectángulo:", area(3, 8, "triangulo"))
    print("Trapecio:", area(2, 4, 5))
    print("Pentágono:", area(5, "pentagono"))
