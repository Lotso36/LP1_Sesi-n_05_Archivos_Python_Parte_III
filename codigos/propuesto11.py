ARCHIVO = "estudiantes.txt"

class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        self.nombre, self.edad, self.calificaciones = nombre, edad, calificaciones

    @property
    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones) if self.calificaciones else 0.0

    def a_linea(self):
        return f"{self.nombre};{self.edad};{','.join(map(str, self.calificaciones))}\n"

    @classmethod
    def desde_linea(cls, linea):
        nombre, edad, notas = linea.rstrip("\n").split(";")
        return cls(nombre, int(edad), [float(n) for n in notas.split(",") if n])

    def __str__(self):
        return f"{self.nombre:<20} Edad: {self.edad:<3} Notas: {self.calificaciones}"

def cargar():
    try:
        with open(ARCHIVO, encoding="utf-8") as f:
            return [Estudiante.desde_linea(l) for l in f if l.strip()]
    except FileNotFoundError:
        return []

def leer_numero(msg, tipo, minimo, maximo):
    while True:
        try:
            valor = tipo(input(msg))
            if minimo <= valor <= maximo:
                return valor
            print(f"Debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Valor no valido.")

def agregar():
    nombre = input("Nombre: ").strip()
    if not nombre or ";" in nombre:
        return print("Nombre no valido.")
    edad = leer_numero("Edad (5-100): ", int, 5, 100)
    cantidad = leer_numero("¿Cuantas calificaciones? (1-10): ", int, 1, 10)
    notas = [leer_numero(f"  Nota {i} (0-20): ", float, 0, 20) for i in range(1, cantidad + 1)]
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(Estudiante(nombre, edad, notas).a_linea())
    print("Estudiante registrado.")

def listar():
    estudiantes = cargar()
    print(*estudiantes, sep="\n") if estudiantes else print("No hay estudiantes registrados.")

def promedio():
    nombre = input("Nombre del estudiante: ").strip().lower()
    for e in cargar():
        if e.nombre.lower() == nombre:
            return print(f"Promedio de {e.nombre}: {e.promedio:.2f}")
    print("Estudiante no encontrado.")

def main():
    acciones = {"1": agregar, "2": listar, "3": promedio}
    while True:
        print("\n1. Agregar estudiante\n2. Ver estudiantes\n3. Promedio de un estudiante\n4. Salir")
        op = input("Opcion: ").strip()
        if op == "4":
            return print("Hasta pronto.")
        try:
            acciones.get(op, lambda: print("Opcion no valida."))()
        except (OSError, ValueError) as e:
            print("Error con el archivo:", e)

if __name__ == "__main__":
    main()