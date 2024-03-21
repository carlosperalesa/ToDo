class Menu:
    def __init__(self, texto="seleccione: ", error="Error: ", opciones={1: "opcion", 2: "opcion"}):
        self.texto = texto
        self.error = error
        self.opciones = opciones
        self.opcion = None

    def mostrar_menu(self):
        print(self.texto)
        for key, value in self.opciones.items():
            print(f"{key}: {value}")

    def seleccionar_opcion(self):
        while True:
            try:
                self.opcion = int(input(self.texto))
                if self.opcion in self.opciones:
                    print(f"Has seleccionado la opción {self.opcion}")
                    break
                else:
                    print(self.error)
            except ValueError:
                print(self.error)
        return self.opcion

# IMPLEMENTACION:

# Menu(texto="Por favor, seleccione una opción: ",
# error="Por favor, seleccione una opción válida: ",
# opciones={
#     1: "Primera opción",
#     2: "Segunda opción",
#     3: "Tercera opción",
#     4: "Cuarta opción",
#     5: "Quinta opción"
# }

# if menu.opcion == 5:
#     print("Hasta luego!")

# Menu.mostrar_menu()
# Menu.seleccionar_opcion()
