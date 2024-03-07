import json

class Menu:

  def __init__(self):
    self.completado = False
    self.items = []

  def listar_items(self):
    for item in self.items:
      print(f"**Nombre:** {item['nombre']}")
      print(f"**Fecha:** {item['fecha']}")
      print(f"**Estado:** {'Completada' if item['estado'] else 'Pendiente'}")
      print("-" * 20)

  def agregar_item(self, nombre, fecha):
    nuevo_item = {"nombre": nombre, "fecha": fecha, "estado": False}
    self.items.append(nuevo_item)

  def modificar_item(self, indice, nombre, fecha):
    self.items[indice]["nombre"] = nombre
    self.items[indice]["fecha"] = fecha

  def eliminar_item(self, indice):
    del self.items[indice]

  def guardar_items(self, archivo_json):
    with open(archivo_json, "w") as archivo:
      json.dump(self.items, archivo)

  def mostrar_menu(self):
    while True:
      print("**Opciones:**")
      print("1. Mostrar tareas")
      print("2. Agregar tarea")
      print("3. Modificar tarea")
      print("4. Eliminar tarea")
      print("5. Marcar como completada")
      print("6. Buscar tarea")
      print("7. Salir")

      opcion = int(input("Ingrese la opción deseada: "))

      if opcion == 1:
        self.listar_items()
      elif opcion == 2:
        nombre = input("Ingrese el nombre de la tarea: ")
        fecha = input("Ingrese la fecha de la tarea (YYYY-MM-DD): ")
        self.agregar_item(nombre, fecha)
      elif opcion == 3:
        indice = int(input("Ingrese el indice de la tarea a modificar: "))
        nombre = input("Ingrese el nuevo nombre de la tarea: ")
        fecha = input("Ingrese la nueva fecha de la tarea (YYYY-MM-DD): ")
        self.modificar_item(indice, nombre, fecha)
      elif opcion == 4:
        indice = int(input("Ingrese el indice de la tarea a eliminar: "))
        self.eliminar_item(indice)
      elif opcion == 5:
        indice = int(input("Ingrese el indice de la tarea a marcar como completada: "))
        self.items[indice]["estado"] = True
      elif opcion == 6:
        opcion_busqueda = int(input("¿Desea buscar por nombre (1) o por fecha (2)?: "))
        if opcion_busqueda == 1:
          nombre = input("Ingrese el nombre de la tarea a buscar: ")
          self.buscar_item_por_nombre(nombre)
        elif opcion_busqueda == 2:
          fecha = input("Ingrese la fecha de la tarea a buscar (YYYY-MM-DD): ")
          self.buscar_item_por_fecha(fecha)
        else:
          print("Opción de búsqueda inválida.")
      elif opcion == 7:
        print("¡Hasta luego!")
        break
      else:
        print("Opción inválida. Ingrese un número del 1 al 7.")

  def buscar_item_por_nombre(self, nombre):
    for item in self.items:
      if item["nombre"] == nombre:
        print(f"**Nombre:** {item['nombre']}")
        print(f"**Fecha:** {item['fecha']}")
        print(f"**Estado:** {'Completada' if item['estado'] else 'Pendiente'}")
        print("-" * 20)

  def buscar_item_por_fecha(self, fecha):
    for item in self.items:
      if item["fecha"] == fecha:
        print(f"**Nombre:** {item['nombre']}")
        print(f"**Fecha:** {item['fecha']}")
        print(f"**Estado:** {'Completada' if item['estado'] else 'Pendiente'}")
        print("-" * 20)

