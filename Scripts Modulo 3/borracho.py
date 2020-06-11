# Creamos un archivo borracho.py
import random

# Creamos nuestra Clase borracho.


class Borracho:

    def __init__(self, nombre):
        self.nomber = nombre

# Creamos la clase BorrachoTradicional que extiende de Borracho.


class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    # Y tendrá un método caminar que devolverá la dirección a la que ira.
    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])


class BorrachoRandom(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0, random.randint(0, 10)), 
                              (0, -random.randint(0, 10)), 
                              (random.randint(0, 10), 0), 
                              (-random.randint(0, 10), 0)])
