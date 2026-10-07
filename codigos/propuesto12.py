from datetime import datetime

ARCHIVO = "tareas.txt"
FORMATO = "%d/%m/%Y"

class Tarea:
    def __init__(self, descripcion, vencimiento, estado="pendiente"):
        self.descripcion, self.vencimiento, self.estado = descripcion, vencimiento, estado

    def a_linea(self):
        return f"{self.descripcion};{self.vencimiento};{self.estado}\n"

    def __str__(self):
        return f"{self.descripcion} (vence: {self.vencimiento}) [{self.estado}]"

def cargar():
    try:
        with open(ARCHIVO, encoding="utf-8") as f:
            return [Tarea(*l.rstrip("\n").split(";")) for l in f if l.count(";") == 2]
    except FileNotFoundError:
        return []

def guardar(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.writelines(t.a_linea() for t in tareas)

def agregar():
    descripcion = input("Descripcion: ").strip()
    fecha = input("Fecha de vencimiento (dd/mm/aaaa): ").strip()
    try:
        datetime.strptime(fecha, FORMATO)
    except ValueError:
        return print("Fecha no valida.")
    if not descripcion or ";" in descripcion:
        return print("Descripcion no valida.")
    tareas = cargar()
    tareas.append(Tarea(descripcion, fecha))
    guardar(tareas)
    print("Tarea agregada.")

def pendientes(tareas):
    return [(i, t) for i, t in enumerate(tareas, 1) if t.estado == "pendiente"]

def listar():
    lista = pendientes(cargar())
    for i, t in lista:
        print(f"{i}. {t}")
    if not lista:
        print("No hay tareas pendientes.")

def completar():
    tareas = cargar()
    lista = pendientes(tareas)
    if not lista:
        return print("No hay tareas pendientes.")
    for i, t in lista:
        print(f"{i}. {t}")
    try:
        n = int(input("Numero de tarea a completar: "))
        if n not in dict(lista):
            raise ValueError
    except ValueError:
        return print("Numero no valido.")
    tareas[n - 1].estado = "completada"
    guardar(tareas)
    print("Tarea completada.")

def main():
    acciones = {"1": agregar, "2": completar, "3": listar}
    while True:
        print("\n1. Agregar tarea\n2. Marcar como completada\n3. Listar pendientes\n4. Salir")
        op = input("Opcion: ").strip()
        if op == "4":
            return print("Hasta pronto.")
        try:
            acciones.get(op, lambda: print("Opcion no valida."))()
        except OSError as e:
            print("Error de archivo:", e.strerror)

if __name__ == "__main__":
    main()