import math

class Punto:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        radio = math.sqrt(self.x ** 2 + self.y ** 2)
        angulo = math.atan2(self.y, self.x) 
        angulo = math.degrees(angulo)
        return radio, angulo

    def __str__(self):
        return "({:.2f},{:.2f})".format(self.x, self.y)

# Ejemplo de uso
p1 = Punto(1, 5)

print(p1)
x, y = p1.coord_cartesianas()
print(x, y)
r, a = p1.coord_polares()
print(r, a)