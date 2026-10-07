import pickle

ARCHIVO = "catalogo.pckl"

class Pelicula:
    def __init__(self, titulo, duracion, anio):
        self.titulo, self.duracion, self.anio = titulo, duracion, anio

    def mostrar(self):
        print(f"{self.titulo} | {self.duracion} min | {self.anio}")

class Catalogo:
    def __init__(self, ruta=ARCHIVO):
        self.ruta, self.peliculas = ruta, []
        self.cargar()

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)
        self.guardar()

    def mostrar(self):
        if not self.peliculas:
            return print("El catalogo esta vacio.")
        for p in self.peliculas:
            p.mostrar()

    def cargar(self):
        try:
            with open(self.ruta, "rb") as f:
                self.peliculas = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.peliculas = []

    def guardar(self):
        with open(self.ruta, "wb") as f:
            pickle.dump(self.peliculas, f)

def main():
    catalogo = Catalogo()
    print(f"Peliculas cargadas del archivo: {len(catalogo.peliculas)}")
    catalogo.agregar(Pelicula("El Padrino", 175, 1972))
    catalogo.agregar(Pelicula("Parasitos", 132, 2019))
    print("Catalogo actual:")
    catalogo.mostrar()

if __name__ == "__main__":
    main()