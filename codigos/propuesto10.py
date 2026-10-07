from collections import defaultdict

class ErrorPuntos(Exception):
    pass

class ArchivoError(ErrorPuntos):
    pass

class LineaError(ErrorPuntos):
    def __init__(self, numero, motivo):
        super().__init__(f"Linea {numero}: {motivo}")

class FormatoError(LineaError):
    pass

class PuntosError(LineaError):
    pass

def procesar_linea(numero, linea):
    partes = linea.split()
    if len(partes) != 3:
        raise FormatoError(numero, f"se esperaban 3 elementos y hay {len(partes)}")
    nombre, apellido, puntos = partes
    try:
        puntos = float(puntos)
    except ValueError:
        raise PuntosError(numero, f"'{partes[2]}' no es un numero") from None
    if puntos < 0:
        raise PuntosError(numero, "los puntos no pueden ser negativos")
    return f"{nombre} {apellido}", puntos

def leer_puntos(ruta):
    totales, errores = defaultdict(float), []
    try:
        with open(ruta, encoding="utf-8") as f:
            for n, linea in enumerate(f, 1):
                if not linea.strip():
                    continue
                try:
                    alumno, pts = procesar_linea(n, linea)
                    totales[alumno] += pts
                except LineaError as e:
                    errores.append(str(e))
    except FileNotFoundError:
        raise ArchivoError(f"El archivo '{ruta}' no existe.") from None
    except UnicodeDecodeError:
        raise ArchivoError("El archivo no es de texto UTF-8.") from None
    except OSError as e:
        raise ArchivoError(e.strerror) from None
    return totales, errores

def main():
    try:
        ruta = input("Ingrese la ruta del archivo: ")
        totales, errores = leer_puntos(ruta)
        for alumno in sorted(totales):
            print(f"{alumno}: {totales[alumno]}")
        if errores:
            print("\nErrores:")
            for e in errores:
                print(e)
    except ArchivoError as e:
        print(e)

if __name__ == "__main__":
    main()