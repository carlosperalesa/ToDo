from menu.menu import Menu
from db.app_db import leer_archivos


contactos, telefonos, ultimo_id = leer_archivos()

opciones = {}
for i, (contacto, telefono) in enumerate(zip(contactos, telefonos)):
    opciones[i+1] = f"{contacto.strip()} - {telefono.strip()}"

opciones[len(contactos)+1] = "Volver al menú principal"

menu = Menu(texto="Elija el contacto a modificar: ",
            error="Ese contacto no existe, intente nuevamente: ",
            opciones=opciones)

            opcion = menu.obtener_opcion_seleccionada()

            if opcion == len(contactos) + 1:
                # Volver al menú principal
                pass
            else:
                contacto_seleccionado = contactos[opcion - 1]
                telefono_seleccionado = telefonos[opcion - 1]

                print(f"Contacto seleccionado: {contacto_seleccionado.strip()} - {telefono_seleccionado.strip()}")

                # Aquí puedes implementar la lógica para modificar el ID, nombre, apellido y teléfonos del contacto seleccionado
                # Puedes mostrar un submenú con las opciones disponibles y solicitar al usuario que ingrese los nuevos valores

                # Por ejemplo:
                # nuevo_id = input("Ingrese el nuevo ID: ")
                # nuevo_nombre = input("Ingrese el nuevo nombre: ")
                # nuevo_apellido = input("Ingrese el nuevo apellido: ")
                # nuevos_telefonos = input("Ingrese los nuevos teléfonos separados por comas: ").split(",")

                # Luego, puedes actualizar los valores del contacto seleccionado en las listas contactos y telefonos

                # contactos[opcion - 1] = nuevo_id + " " + nuevo_nombre + " " + nuevo_apellido
                # telefonos[opcion - 1] = nuevos_telefonos

                # Finalmente, puedes guardar los cambios en los archivos correspondientes utilizando la función escribir_archivos()

                # escribir_archivos(contactos, telefonos, ultimo_id)






menu.mostrar_menu()
menu.seleccionar_opcion()
