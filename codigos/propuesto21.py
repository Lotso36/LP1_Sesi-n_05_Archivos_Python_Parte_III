import pickle

ARCHIVO = "personajes.pickl"

class Personaje:
    def __init__(self, nombre, vida, ofensiva, proteccion, alcance):
        stats = (vida, ofensiva, proteccion, alcance)
        if not all(isinstance(s, int) and not isinstance(s, bool) and s > 0 for s in stats):
            raise ValueError("Las propiedades deben ser enteros positivos.")
        self.nombre, self.vida, self.ofensiva = nombre, vida, ofensiva
        self.proteccion, self.alcance = proteccion, alcance

    def __str__(self):
        return (f"{self.nombre:<12} Vida: {self.vida}  Ofensiva: {self.ofensiva}  "
                f"Proteccion: {self.proteccion}  Alcance: {self.alcance}")

class Gestor:
    def __init__(self, ruta=ARCHIVO):
        self.ruta = ruta
        try:
            with open(ruta, "rb") as f:
                self.personajes = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.personajes = {}

    def _guardar(self):
        with open(self.ruta, "wb") as f:
            pickle.dump(self.personajes, f)

    def anadir(self, personaje):
        if personaje.nombre in self.personajes:
            return print(f"{personaje.nombre} ya existe: no se crea.")
        self.personajes[personaje.nombre] = personaje
        self._guardar()

    def borrar(self, nombre):
        if self.personajes.pop(nombre, None) is None:
            return print(f"{nombre} no existe.")
        self._guardar()

    def mostrar(self):
        print(*self.personajes.values(), sep="\n") if self.personajes else print("Sin personajes.")

def main():
    g = Gestor()
    g.personajes.clear()
    for datos in (("Personaje1", 4, 2, 4, 2), ("Personaje2", 2, 4, 2, 4), ("Personaje3", 2, 4, 1, 8)):
        g.anadir(Personaje(*datos))
    g.anadir(Personaje("Personaje1", 9, 9, 9, 9))
    print("Personajes del Gestor:")
    g.mostrar()
    g.borrar("Personaje3")
    print("\nTras borrar Personaje3:")
    g.mostrar()
    print("\nRecargado desde personajes.pickl:")
    Gestor().mostrar()

if __name__ == "__main__":
    main()
