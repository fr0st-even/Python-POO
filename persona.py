from lugar import Lugar
from foto import Foto
from rol import Rol

class Persona:
    def __init__(self, nombre: str, apellido: str, foto: Foto):
        self.nombre = nombre
        self.apellido = apellido
        self.lugares_frecuentes = []
        self.rol = None
        self.foto = foto

    def agregar_lugar_frecuente(self, lugar: Lugar):
        self.lugares_frecuentes.append(lugar)

    def set_rol(self, rol: Rol):
        self.rol = rol

    def __str__(self):
        lugares = ', '.join(str(lugar) for lugar in self.lugares_frecuentes)
        return (f"La persona con nombre: {self.nombre} {self.apellido}, "
                f"{self.foto}, y rol de {self.rol}, tiene los siguientes lugares: {lugares}")
