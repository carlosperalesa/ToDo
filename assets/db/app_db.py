from os import path


def leer_archivos():
    with open('assets/db/contactos.txt', 'r', encoding='utf-8') as f:
        contactos = f.readlines()

    with open('assets/db/telefonos.txt', 'r', encoding='utf-8') as f:
        telefonos = f.readlines()

    ultimo_id = int(contactos[-1].split(',')[0])

    return contactos, telefonos, ultimo_id


def agregar_contacto(contacto, telefonos):
    contactos, _, ultimo_id = leer_archivos()
    nuevo_id = ultimo_id + 1

    with open('assets/db/contactos.txt', 'a', encoding='utf-8') as f:
        f.write(f"{nuevo_id}, {contacto.nombre}, {contacto.apellido}\n")

    with open('assets/db/telefonos.txt', 'a', encoding='utf-8') as f:
        f.write(f"{nuevo_id}, {telefonos}\n")
