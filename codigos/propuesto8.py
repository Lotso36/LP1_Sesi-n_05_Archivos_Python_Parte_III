import os

ARCHIVO = "agenda.txt"

def cargar():
    try:
        with open(ARCHIVO, encoding="utf-8") as f:
            return dict(l.rstrip("\n").split(";", 1) for l in f if ";" in l)
    except FileNotFoundError:
        return {}

def guardar(agenda):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.writelines(f"{n};{c}\n" for n, c in agenda.items())

def pedir_nombre():
    nombre = input("Nombre del cliente: ").strip()
    return nombre if nombre and ";" not in nombre else None

def consultar():
    agenda, nombre = cargar(), pedir_nombre()
    if nombre is None:
        return print("Nombre no valido.")
    print(f"Celular de {nombre}: {agenda[nombre]}" if nombre in agenda
          else "No existe el cliente en la agenda.")

def anadir():
    nombre = pedir_nombre()
    celular = input("Celular (9 digitos): ").strip()
    if nombre is None or not (celular.isdigit() and len(celular) == 9):
        return print("Datos no válidos: nombre no vacio y celular de 9 digitos.")
    agenda = cargar()
    agenda[nombre] = celular
    guardar(agenda)
    print("Cliente registrado.")

def eliminar():
    agenda, nombre = cargar(), pedir_nombre()
    if nombre in agenda:
        del agenda[nombre]
        guardar(agenda)
        print("Cliente eliminado.")
    else:
        print("No existe el cliente en la agenda.")

def crear():
    if os.path.exists(ARCHIVO) and input("agenda.txt ya existe. Eliminarla e iniciar una nueva? (s/n): ").lower() != "s":
        return print("Operacion cancelada.")
    guardar({})
    print("Agenda creada.")

def main():
    acciones = {"1": consultar, "2": anadir, "3": eliminar, "4": crear}
    while True:
        print("\n1. Consultar un celular\n2. Añadir un celular\n3. Eliminar un celular\n4. Crear la agenda\n5. Salir")
        op = input("Elija una opción: ").strip()
        if op == "5":
            return print("Hasta pronto.")
        try:
            acciones.get(op, lambda: print("Opcion no valida."))()
        except OSError as e:
            print("Error de archivo:", e.strerror)

if __name__ == "__main__":
    main()
