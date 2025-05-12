class Foto:
    def __init__(self, ubicacion_archivo: str, tipo_archivo: str):
        self.ubicacion_archivo = ubicacion_archivo
        self.tipo_archivo = tipo_archivo

    def __str__(self):
        return f"foto tipo {self.tipo_archivo} ubicada en {self.ubicacion_archivo}"