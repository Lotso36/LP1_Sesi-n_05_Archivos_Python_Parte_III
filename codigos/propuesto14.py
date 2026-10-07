from datetime import datetime

ARCHIVO, FORMATO = "reservas.txt", "%d/%m/%Y"

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero, self.tipo, self.precio = numero, tipo, precio

HABITACIONES = {h.numero: h for h in (Habitacion(101, "Simple", 80.0), Habitacion(102, "Doble", 120.0),
                                      Habitacion(201, "Suite", 250.0), Habitacion(202, "Familiar", 180.0))}

def cargar():
    try:
        with open(ARCHIVO, encoding="utf-8") as f:
            filas = (l.rstrip("\n").split(";") for l in f if l.count(";") == 3)
            return [(c, int(h), datetime.strptime(e, FORMATO), datetime.strptime(s, FORMATO)) for c, h, e, s in filas]
    except FileNotFoundError:
        return []

def disponible(numero, entrada, salida, reservas):
    return all(h != numero or salida <= e or entrada >= s for _, h, e, s in reservas)

def pedir_fechas():
    try:
        entrada = datetime.strptime(input("Fecha de entrada (dd/mm/aaaa): ").strip(), FORMATO)
        salida = datetime.strptime(input("Fecha de salida (dd/mm/aaaa): ").strip(), FORMATO)
    except ValueError:
        return print("Fecha no valida."), None
    if salida <= entrada or entrada < datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
        return print("Rango de fechas no valido (salida > entrada y no en el pasado)."), None
    return entrada, salida

def ver_disponibilidad():
    entrada, salida = pedir_fechas()
    if entrada is None:
        return
    reservas = cargar()
    for h in HABITACIONES.values():
        estado = "Disponible" if disponible(h.numero, entrada, salida, reservas) else "Ocupada"
        print(f"{h.numero} {h.tipo:<9} S/ {h.precio:>7.2f}/noche  {estado}")

def reservar():
    cliente = input("Nombre del cliente: ").strip()
    try:
        numero = int(input("N° de habitacion: "))
        habitacion = HABITACIONES[numero]
    except (ValueError, KeyError):
        return print("Habitacion no existente.")
    if not cliente or ";" in cliente:
        return print("Nombre no valido.")
    entrada, salida = pedir_fechas()
    if entrada is None:
        return
    if not disponible(numero, entrada, salida, cargar()):
        return print("La habitacion no esta disponible en esas fechas.")
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"{cliente};{numero};{entrada:{FORMATO}};{salida:{FORMATO}}\n")
    noches = (salida - entrada).days
    print(f"Reserva registrada. {noches} noche(s) en la {habitacion.tipo} {numero}.")

def factura():
    cliente = input("Nombre del cliente: ").strip().lower()
    propias = [r for r in cargar() if r[0].lower() == cliente]
    if not propias:
        return print("El cliente no tiene reservas.")
    total = 0
    print(f"\n{'FACTURA':^50}\nCliente: {propias[0][0]}\n" + "-" * 50)
    for _, h, e, s in propias:
        noches, hab = (s - e).days, HABITACIONES[h]
        subtotal = noches * hab.precio
        total += subtotal
        print(f"{hab.tipo} {h}  {e:{FORMATO}}-{s:{FORMATO}}  {noches} x {hab.precio:.2f} = {subtotal:.2f}")
    print("-" * 50 + f"\nTOTAL: S/ {total:.2f}")

def main():
    acciones = {"1": reservar, "2": ver_disponibilidad, "3": factura}
    while True:
        print("\n1. Realizar reserva\n2. Verificar disponibilidad\n3. Generar factura\n4. Salir")
        op = input("Opcion: ").strip()
        if op == "4":
            return print("Hasta pronto.")
        try:
            acciones.get(op, lambda: print("Opcion no valida."))()
        except (OSError, ValueError) as e:
            print("Error con el archivo:", e)

if __name__ == "__main__":
    main()
