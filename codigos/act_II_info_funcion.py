def crearArchivo(texto, ruta="prueba.txt"):
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("Lenguaje de Programación I\n")
        f.write(texto + "\n")

archi = open("archivo.txt", "w", encoding="utf-8")
print("Nombre:", archi.name)
print("Cerrado?:", archi.closed)
print("Modalidad de apertura:", archi.mode)
archi.close()
print("Cerrado tras close()?:", archi.closed)

crearArchivo(input("Ingrese un texto a agregar al archivo: "))
print(open("prueba.txt", encoding="utf-8").read())
