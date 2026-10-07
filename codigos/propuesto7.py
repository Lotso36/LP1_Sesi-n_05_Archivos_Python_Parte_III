from collections import Counter

def frecuencia_letras(ruta):
    with open(ruta, encoding="utf-8") as f:
        return Counter(c for linea in f for c in linea.rstrip("\n").lower())

def main():
    ruta = input("Nombre del archivo de texto (con extensión): ").strip()
    try:
        print(dict(frecuencia_letras(ruta)))
    except FileNotFoundError:
        print(f"El archivo '{ruta}' no existe.")
    except UnicodeDecodeError:
        print("El archivo no es de texto UTF-8.")
    except OSError as e:
        print("Error de lectura:", e.strerror)

if __name__ == "__main__":
    main()
