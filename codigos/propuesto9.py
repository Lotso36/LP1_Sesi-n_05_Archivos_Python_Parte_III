from collections import Counter

def histograma(ruta):
    with open(ruta, encoding="utf-8") as f:
        return Counter(c for linea in f for c in linea.lower() if c.isalpha())

def main():
    ruta = input("Nombre del archivo: ").strip()
    try:
        conteo = histograma(ruta)
    except FileNotFoundError:
        return print(f"El archivo '{ruta}' no existe.")
    except UnicodeDecodeError:
        return print("El archivo no es de texto UTF-8.")
    except OSError as e:
        return print("Error de lectura:", e.strerror)
    for letra in sorted(conteo):
        print(f"{letra}->{conteo[letra]}")

if __name__ == "__main__":
    main()
