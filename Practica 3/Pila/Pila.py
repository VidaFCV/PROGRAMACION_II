class Pila:
    def _init_(self, n):
        self.__arreglo = [None] * n
        self.__top = -1
        self.__n = n

    def push(self, e):
        if self.isFull():
            print("Pila llena")
        else:
            self.__top += 1
            self._arreglo[self._top] = e

    def pop(self):
        if self.isEmpty():
            print("Pila vacía")
            return None
        else:
            e = self._arreglo[self._top]
            self.__top -= 1
            return e

    def peek(self):
        if self.isEmpty():
            print("Pila vacía")
            return None
        else:
            return self._arreglo[self._top]

    def isEmpty(self):
        return self.__top == -1

    def isFull(self):
        return self._top == self._n - 1