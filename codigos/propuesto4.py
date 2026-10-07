import re

def analizar(ruta, buscada):
    total = coincidencias = 0
    buscada = buscada.lower()
    with open(ruta, encoding="utf-8") as f:
        for linea in f:                                    
            palabras = re.findall(r"\w+", linea.lower())
            total += len(palabras)
            coincidencias += palabras.count(buscada)
    return total, coincidencias

def main():
    ruta = input("Nombre del archivo a leer: ").strip()
    buscada = input("Palabra a buscar: ").strip()
    if not buscada or len(buscada.split()) != 1:
        return print("Debe ingresar una única palabra.")
    try:
        total, coinc = analizar(ruta, buscada)
    except FileNotFoundError:
        return print(f"El archivo '{ruta}' no existe.")
    except UnicodeDecodeError:
        return print("El archivo no es de texto UTF-8.")
    except OSError as e:
        return print("Error de lectura:", e.strerror)
    print(f"Palabras en el archivo: {total}")
    print(f"Coincidencias de '{buscada}': {coinc}")

if __name__ == "__main__":
    main()
