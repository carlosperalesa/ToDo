from assets.db.app_db import agregar_contacto


class Contacto:
    id = 1

    def __init__(self, nombre, apellido, telefonos):
        self.id = Contacto.id
        self.nombre = nombre
        self.apellido = apellido
        self.telefonos = telefonos
        Contacto.id += 1

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Teléfonos: {', '.join(self.telefonos)}"


def crear_contacto():
    nombre = input("Ingrese su nombre: ").capitalize()
    apellido = input("Ingrese su apellido: ").capitalize()

    telefonos = []
    while True:
        telefono = input("Ingrese un número de teléfono, o 0 para terminar: ")
        if telefono == "0":
            break
        telefonos.append(telefono)

    contacto = Contacto(nombre, apellido, telefonos)

    print(str(contacto))

    respuesta = ''
    while respuesta not in ['s', 'n']:
        respuesta = input("¿Desea guardar? s/n: ").lower()
        if respuesta not in ['s', 'n']:
            print("Por favor, ingrese S/N")
        elif respuesta == 's':
            agregar_contacto(contacto, telefonos)
        elif respuesta == 'n':
            print("Contacto no guardado")
            break
