# _ El principio nos indica que una clase debe de implementar únicamente
# __ las interfaces que necesita, es decir, que no necesite tener que implementar
# ___ métodos que no utilice.
# _ El propósito de este principio es obligarnos a escribir interfaces pequeñas
# __  buscando aplicar el principio de cohesión en cada interfaz.

from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass

class Aircraft(Flyable):
    def go(self):
        print(f"Taxiing {self}")
    
    def go(self, placas):
        print(f"Taxiing {self}")
    
    def fly(self):
        print("Flying")

class Car(Movable):
    def go(self):
        print("Going")

if __name__ == '__main__':
    Aircraft.go("tochito")
    Car.go("tochito")