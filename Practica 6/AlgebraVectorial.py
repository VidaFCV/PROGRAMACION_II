import numpy as np

class AlgebraVectorial:
    def __init__(self, vector):
        self.vector = np.array(vector)

    def __add__(self, other):
        return AlgebraVectorial(self.vector + other.vector)

    def __sub__(self, other):
        return AlgebraVectorial(self.vector - other.vector)

    def __mul__(self, scalar):
        return AlgebraVectorial(self.vector * scalar)
    
    def dot(self, other):
        return np.dot(self.vector, other.vector)
    
    def cross(self, other):
        v1_3d = self._to_3d(self.vector)
        v2_3d = self._to_3d(other.vector)
        
        return np.cross(v1_3d, v2_3d)
    
    def _to_3d(self, vector):
        if len(vector) == 2:
            return np.append(vector, 0)
        return vector

    def norm(self):
        return np.linalg.norm(self.vector)
    
    def normalize(self):
        norm_value = self.norm()
        return AlgebraVectorial(self.vector / norm_value) if norm_value != 0 else None
    
    def es_perpendicular(self, other):
        return self.dot(other) == 0
    
    def es_paralelo(self, other):
        v1_3d = self._to_3d(self.vector)
        v2_3d = self._to_3d(other.vector)
        return np.all(np.cross(v1_3d, v2_3d) == 0)
    
    def proyeccion(self, other):
        return (self.dot(other) / np.dot(other.vector, other.vector)) * other.vector
    
    def componente(self, other):
        return (self.dot(other) / np.linalg.norm(other.vector))

vector1 = list(map(float, input("Ingrese los componentes del vector 1: ").split()))
vector2 = list(map(float, input("Ingrese los componentes del vector 2: ").split()))

v1 = AlgebraVectorial(vector1)
v2 = AlgebraVectorial(vector2)

print("Perpendicular:", v1.es_perpendicular(v2))
print("Paralelo:", v1.es_paralelo(v2))
print("Proyección de v1 sobre v2:", v1.proyeccion(v2))
print("Componente de v1 en la dirección de v2:", v1.componente(v2))
print("Suma de v1 y v2:", (v1 + v2).vector)
print("Multiplicación de v1 por 2:", (v1 * 2).vector)
print("Norma de v1:", v1.norm())
print("Vector unitario de v1:", v1.normalize().vector if v1.normalize() else "No se puede normalizar")
print("Producto escalar v1 · v2:", v1.dot(v2))
print("Producto vectorial v1 × v2:", v1.cross(v2))

