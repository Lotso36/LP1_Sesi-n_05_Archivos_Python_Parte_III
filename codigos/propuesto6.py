import re
from collections import Counter

def frecuencia_palabras(ruta):
    with open(ruta, encoding="utf-8") as f:
        return Counter(p for linea in f for p in re.findall(r"\w+", linea.lower()))

def main():
    ruta = input("Nombre del archivo de texto (con extensión): ").strip()
    try:
        frecuencias = frecuencia_palabras(ruta)
    except FileNotFoundError:
        return print(f"El archivo '{ruta}' no existe.")
    except UnicodeDecodeError:
        return print("El archivo no es de texto UTF-8.")
    except OSError as e:
        return print("Error de lectura:", e.strerror)
    if not frecuencias:
        return print("El archivo no contiene palabras.")
    print(dict(frecuencias))                     
    for palabra, veces in frecuencias.items():
        print(f"{palabra}: {veces}")

if __name__ == "__main__":
    main()
