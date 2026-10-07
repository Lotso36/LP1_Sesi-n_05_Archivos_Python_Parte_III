RUTA = "archivo.txt"

with open(RUTA, "w", encoding="utf-8") as f:
    f.write("La vida es bella!!!")

with open(RUTA, encoding="utf-8") as f:
    print("Contenido completo:", f.read())

with open(RUTA, encoding="utf-8") as f:
    for n, linea in enumerate(f, 1):
        print(f"Linea {n}: {linea.rstrip()}")

with open(RUTA, "a", encoding="utf-8") as f:
    f.write("\nLa actitud siempre debe ser positiva")

with open(RUTA, encoding="utf-8") as f:
    print("Después de agregar:\n" + f.read())
