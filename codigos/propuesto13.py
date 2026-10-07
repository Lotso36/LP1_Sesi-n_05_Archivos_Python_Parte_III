import csv
from collections import defaultdict
from datetime import datetime

ARCHIVO, FORMATO = "gastos.txt", "%d/%m/%Y"

class Gasto:
    def __init__(self, descripcion, categoria, monto, fecha):
        self.descripcion, self.categoria = descripcion, categoria
        self.monto, self.fecha = monto, fecha

    @property
    def mes(self):
        return datetime.strptime(self.fecha, FORMATO).strftime("%Y-%m")

    def a_fila(self):
        return [self.descripcion, self.categoria, f"{self.monto:.2f}", self.fecha]

def cargar():
    try:
        with open(ARCHIVO, encoding="utf-8", newline="") as f:
            return [Gasto(d, c, float(m), fe) for d, c, m, fe in csv.reader(f, delimiter=";")]
    except FileNotFoundError:
        return []

def registrar():
    descripcion = input("Descripcion: ").strip()
    categoria = input("Categoria: ").strip().lower()
    try:
        monto = float(input("Monto: "))
        fecha = input("Fecha (dd/mm/aaaa): ").strip()
        datetime.strptime(fecha, FORMATO)
    except ValueError:
        return print("Monto o fecha no validos.")
    if monto <= 0 or not descripcion or not categoria or ";" in descripcion + categoria:
        return print("Datos no validos.")
    with open(ARCHIVO, "a", encoding="utf-8", newline="") as f:
        csv.writer(f, delimiter=";").writerow(Gasto(descripcion, categoria, monto, fecha).a_fila())
    print("Gasto registrado.")

def resumen():
    gastos = cargar()
    if not gastos:
        return print("No hay gastos registrados.")
    por_mes = defaultdict(lambda: defaultdict(float))
    for g in gastos:
        por_mes[g.mes][g.categoria] += g.monto
    for mes in sorted(por_mes):
        print(f"\n{mes}  (total: {sum(por_mes[mes].values()):.2f})")
        for cat, total in sorted(por_mes[mes].items()):
            print(f"  {cat:<15}{total:>10.2f}")

def exportar():
    gastos = cargar()
    if not gastos:
        return print("No hay gastos para exportar.")
    with open("gastos.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["descripcion", "categoria", "monto", "fecha"])
        w.writerows(g.a_fila() for g in gastos)
    print(f"{len(gastos)} gastos exportados a gastos.csv")

def main():
    acciones = {"1": registrar, "2": resumen, "3": exportar}
    while True:
        print("\n1. Registrar gasto\n2. Resumen por mes y categoria\n3. Exportar a CSV\n4. Salir")
        op = input("Opcion: ").strip()
        if op == "4":
            return print("Hasta pronto.")
        try:
            acciones.get(op, lambda: print("Opcion no valida."))()
        except (OSError, ValueError) as e:
            print("Error con el archivo:", e)

if __name__ == "__main__":
    main()