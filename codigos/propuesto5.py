import unicodedata

def contar_vocales(texto):
    base = unicodedata.normalize("NFD", texto.lower())
    base = "".join(c for c in base if not unicodedata.combining(c))
    return {v: base.count(v) for v in "aeiou"}

def formatear(conteo):
    lineas = [f"{v}: {n}" for v, n in conteo.items()]
    return "\n".join(lineas + [f"Total: {sum(conteo.values())}"])

def opcion_cadena():
    oracion = input("Ingrese la oracion: ")
    if not oracion.strip():
        return print("La oracion no puede estar vacia.")
    resultado = formatear(contar_vocales(oracion))
    try:
        with open("vocales.txt", "w", encoding="utf-8") as f:
            f.write(f"Texto: {oracion}\n{resultado}\n")
    except OSError as e:
        return print("No se pudo escribir vocales.txt:", e.strerror)
    print("Archivo vocales.txt generado:\n" + open("vocales.txt", encoding="utf-8").read())

def opcion_archivo():
    ruta = input("Nombre del archivo con extension: ").strip()
    try:
        with open(ruta, encoding="utf-8") as f:
            texto = f.read()
    except FileNotFoundError:
        return print(f"El archivo '{ruta}' no existe.")
    except UnicodeDecodeError:
        return print("El archivo no es de texto UTF-8.")
    except OSError as e:
        return print("Error de lectura:", e.strerror)
    print(formatear(contar_vocales(texto)))

def main():
    acciones = {"1": opcion_cadena, "2": opcion_archivo}
    while True:
        print("\n1. Leer cadena de caracteres\n2. Leer archivo\n3. Salir")
        op = input("Elija una opcion: ").strip()
        if op == "3":
            return print("Programa terminado.")
        acciones.get(op, lambda: print("Opcion no valida."))()

if __name__ == "__main__":
    main()
