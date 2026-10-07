datos = bytearray(range(10, 20))
try:
    with open("actividad1.bin", "wb") as f:
        f.write(datos)
    print("Archivo binario escrito:", len(datos), "bytes")
except OSError as e:
    print("Error al abrir el fichero:", e)

buffer = bytearray(10)
try:
    with open("actividad1.bin", "rb") as f:
        f.readinto(buffer)
    print(" ".join(hex(b) for b in buffer))
except OSError as e:
    print("Error al abrir el fichero:", e)
