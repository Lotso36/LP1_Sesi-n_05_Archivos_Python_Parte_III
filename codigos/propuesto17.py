FIRMA = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

def es_png(ruta):
    with open(ruta, "rb") as f:
        return f.read(len(FIRMA)) == FIRMA

def main():
    ruta = input("Nombre del archivo: ").strip()
    try:
        print(f"'{ruta}' {'ES' if es_png(ruta) else 'NO es'} una imagen PNG.")
    except FileNotFoundError:
        print(f"El archivo '{ruta}' no existe.")
    except OSError as e:
        print("Error de lectura:", e.strerror)

if __name__ == "__main__":
    main()