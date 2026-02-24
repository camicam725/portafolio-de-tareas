# -------- Cami Cam --------

# R-2.4 Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its number
# of petals, and its price. Your class must include a constructor method that 
# initializes each variable to an appropriate value, and your class should 
# include methods for setting the value of each type, and retrieving the value 
# of each type.

class Flor:
    def __init__(self, nombre: str, petalos: int, precio: float):
        self.nombre = nombre
        self.petalos = petalos
        self.precio = precio

    # Métodos para obtener valores
    def obtener_nombre(self):
        return self.nombre

    def obtener_petalos(self):
        return self.petalos

    def obtener_precio(self):
        return self.precio

    # Métodos para modificar valores
    def establecer_nombre(self, nuevo_nombre: str):
        self.nombre = nuevo_nombre

    def establecer_petalos(self, nuevos_petalos: int):
        self.petalos = nuevos_petalos

    def establecer_precio(self, nuevo_precio: float):
        self.precio = nuevo_precio


# Ejemplo de uso:
flor1 = Flor("Rosa", 32, 15.5)

print(flor1.obtener_nombre())    
print(flor1.obtener_petalos())   
print(flor1.obtener_precio())    

flor1.establecer_precio(20.0)
print(flor1.obtener_precio())    