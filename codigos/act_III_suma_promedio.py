def leer_numeros(nombre):
    suma = contador = 0
    try:
        with open(nombre, encoding="utf-8") as f:
            for n, linea in enumerate(f, 1):
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    suma += float(linea)
                    contador += 1
                except ValueError:
                    print(f"Linea {n}: '{linea}' no es un numero (se omite).")
    except FileNotFoundError:
        return print(f"No existe el archivo llamado {nombre}")
    except OSError as e:
        return print(f"No se pudo leer el archivo: {e.strerror}")
    if contador == 0:
        return print("El archivo no contiene numeros válidos.")
    print(f"Suma: {suma:g}\nPromedio: {suma / contador:.2f}")

leer_numeros(input("Digite nombre del archivo completo (ejemplo.txt): "))
