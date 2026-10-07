import pickle

ARCHIVO = "tareas.pckl"

class Tarea:
    def __init__(self, descripcion, vencimiento, estado="pendiente"):
        self.descripcion, self.vencimiento, self.estado = descripcion, vencimiento, estado

    def __str__(self):
        return f"{self.descripcion} | vence: {self.vencimiento} | {self.estado}"

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, vencimiento):
        self.tareas.append(Tarea(descripcion, vencimiento))

    def completar_tarea(self, indice):
        if not 0 <= indice < len(self.tareas):
            raise IndexError("No existe esa tarea.")
        self.tareas[indice].estado = "finalizada"

    def listar_tareas(self):
        for i, t in enumerate(self.tareas, 1):
            print(f"{i}. {t}")

    def guardar(self, ruta=ARCHIVO):
        with open(ruta, "wb") as f:
            pickle.dump(self.tareas, f)

def main():
    g = GestorTareas()
    g.agregar_tarea("Estudiar archivos en Python", "10/10/2026")
    g.agregar_tarea("Entregar informe de laboratorio", "06/10/2026")
    g.agregar_tarea("Practicar pickle", "12/10/2026")
    g.completar_tarea(1)
    g.listar_tareas()
    g.guardar()
    print(f"\n{len(g.tareas)} tareas serializadas en {ARCHIVO}")

if __name__ == "__main__":
    import propuesto18
    propuesto18.main()