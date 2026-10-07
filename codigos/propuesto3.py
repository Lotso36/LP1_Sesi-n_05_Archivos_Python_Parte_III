import sys

ARCHIVO = "contador.txt"

def leer():
    try:
        with open(ARCHIVO, encoding="utf-8") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def guardar(valor):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write(str(valor))

def main(args):
    if len(args) > 1:
        return print("Uso: python propuesto3.py [inc | dec]")
    contador = leer()
    if args:
        if args[0] == "inc":
            contador += 1
        elif args[0] == "dec":
            contador -= 1
        else:
            return print(f"Argumento '{args[0]}' no válido. Use inc o dec.")
    try:
        guardar(contador)
    except OSError as e:
        return print("No se pudo guardar el contador:", e.strerror)
    print("Contador:", contador)

if __name__ == "__main__":
    main(sys.argv[1:])
