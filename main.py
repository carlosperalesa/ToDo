from assets.menu.menu import Menu
from assets.crear_contacto import crear_contacto
from assets.modificar_contacto import modificar_contacto


def main():
    menu = Menu(texto="Por favor, seleccione una opción: ",
                error="Por favor, seleccione una opción válida: ",
                opciones={
                    1: "Agregar item",
                    2: "Modificar item",
                    3: "Eliminar item",
                    4: "Salir",
                })

    menu.mostrar_menu()
    menu.seleccionar_opcion()

    if menu.opcion == 1:
        crear_contacto()

    elif menu.opcion == 4:
        print("Hasta luego!")
        exit()


main()
