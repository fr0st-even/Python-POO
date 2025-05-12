from enum import Enum

class Rol(Enum):
    PROFESIONAL = "Profesional"
    USUARIO = "Usuario"

    def __str__(self):
        return self.value
