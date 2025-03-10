class Cola:
    def _init_(self, n):
        self.__arreglo = [None] * n
        self.__inicio = 0
        self.__fin = 0
        self.__n = n

    def insert(self, e):
        if self.isFull():
            print("Cola llena")
        else:
            self._arreglo[self._fin] = e
            self.__fin += 1

    def remove(self):
        if self.isEmpty():
            print("Cola vacía")
            return None
        else:
            e = self._arreglo[self._inicio]
            self.__inicio += 1
            return e

    def peek(self):
        if self.isEmpty():
            print("Cola vacía")
            return None
        else:
            return self._arreglo[self._inicio]

    def isEmpty(self):
        return self._inicio == self._fin

    def isFull(self):
        return self._fin == self._n

    def size(self):
        return self._fin - self._inicio