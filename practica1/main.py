from persona import Persona
from lugar import Lugar
from foto import Foto
from rol import Rol

def main():
    lugar1 = Lugar("Aeropueto", "Zona 12", "555-1234")
    lugar2 = Lugar("Universidad", "Zona 13", "555-5678")
    
    foto1 = Foto("C:/imagenes/imagen1.jpg", "JPG")
    
    persona1 = Persona("Iosef", "Canchan", foto1)
    persona1.agregar_lugar_frecuente(lugar1)
    persona1.agregar_lugar_frecuente(lugar2)
    persona1.set_rol(Rol.PROFESIONAL)

    print(persona1)

if __name__ == "__main__":
    main()
