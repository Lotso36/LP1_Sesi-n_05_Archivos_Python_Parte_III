with open("archivobase.txt", "w", encoding="utf-8") as f:
    f.write("Primera linea\nSegunda linea\nTercera linea\n")

with open("archivobase.txt", encoding="utf-8") as archi:   
    for ln in archi:
        print(ln, end="")
print("\nArchivo cerrado?:", archi.closed)
