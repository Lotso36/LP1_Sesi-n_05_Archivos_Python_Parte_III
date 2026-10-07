from datetime import datetime

ARCHIVO = "peliculas.txt"

class Pelicula:
    def __init__(self, titulo, director, anio):
        self.titulo, self.director, self.anio = titulo, director, int(anio)

    def a_linea(self):
        return f"{self.titulo};{self.director};{self.anio}\n"

    def __str__(self):
        return f"{self.titulo} - {self.director} ({self.anio})"

def cargar():
    try:
        with open(ARCHIVO, encoding="utf-8") as f:
            return [Pelicula(*l.rstrip("\n").split(";")) for l in f if l.count(";") == 2]
    except FileNotFoundError:
        return []

def agregar():
    titulo, director = input("Titulo: ").strip(), input("Director: ").strip()
    try:
        anio = int(input("Año de lanzamiento: "))
    except ValueError:
        return print("El año debe ser un numero entero.")
    if not (1888 <= anio <= datetime.now().year + 5):
        return print("Año fuera de rango.")
    if not titulo or not director or ";" in titulo + director:
        return print("Titulo y director no validos.")
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(Pelicula(titulo, director, anio).a_linea())
    print("Pelicula agregada.")

def buscar():
    criterio = input("Buscar por (1) titulo o (2) director: ").strip()
    if criterio not in ("1", "2"):
        return print("Opcion no valida.")
    texto = input("Texto a buscar: ").strip().lower()
    campo = "titulo" if criterio == "1" else "director"
    hallados = [p for p in cargar() if texto in getattr(p, campo).lower()]
    print(*hallados, sep="\n") if hallados else print("Sin resultados.")

def listar():
    peliculas = cargar()
    print(*peliculas, sep="\n") if peliculas else print("No hay peliculas registradas.")

def main():
    acciones = {"1": agregar, "2": buscar, "3": listar}
    while True:
        print("\n1. Agregar pelicula\n2. Buscar pelicula\n3. Listar peliculas\n4. Salir")
        op = input("Opcion: ").strip()
        if op == "4":
            return print("Hasta pronto.")
        try:
            acciones.get(op, lambda: print("Opcion no valida."))()
        except (OSError, ValueError) as e:
            print("Error con el archivo:", e)

if __name__ == "__main__":
    main()