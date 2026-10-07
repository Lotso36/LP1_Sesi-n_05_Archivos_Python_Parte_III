FIRMA = bytes([0xFF, 0xD8])

def es_jpg(ruta):
    with open(ruta, "rb") as f:
        return f.read(len(FIRMA)) == FIRMA

def main():
    ruta = input("Nombre del archivo: ").strip()
    try:
        print(f"'{ruta}' {'ES' if es_jpg(ruta) else 'NO es'} una imagen JPG.")
    except FileNotFoundError:
        print(f"El archivo '{ruta}' no existe.")
    except OSError as e:
        print("Error de lectura:", e.strerror)

if __name__ == "__main__":
    main()