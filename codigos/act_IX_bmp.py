import os

class TipoImagen:
    @staticmethod
    def chequearImagenBMP(archivo):
        try:
            with open(archivo, "rb") as f:
                return f.read(2) == b"BM"
        except OSError:
            return False

if __name__ == "__main__":
    pruebas = {"imagen_bmp.bmp": b"BM" + bytes(20),
               "imagen_jpg.jpg": b"\xff\xd8\xff\xe0" + bytes(20),
               "imagen_png.png": b"\x89PNG\r\n\x1a\n" + bytes(20)}
    for nombre, contenido in pruebas.items():
        with open(nombre, "wb") as f:
            f.write(contenido)
    for i, nombre in enumerate(pruebas, 1):
        print(f"Prueba {i} ({nombre}):", TipoImagen.chequearImagenBMP(nombre))
    print("Archivo inexistente:", TipoImagen.chequearImagenBMP("no_existe.bmp"))
