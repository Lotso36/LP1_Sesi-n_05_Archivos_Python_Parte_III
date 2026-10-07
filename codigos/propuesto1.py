def pedir_entero(minimo=1, maximo=10):
    while True:
        try:
            n = int(input(f"Ingrese un entero entre {minimo} y {maximo}: "))
            if minimo <= n <= maximo:
                return n
            print(f"El valor debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Entrada invalida: ingrese un numero entero.")

def main():
    n = pedir_entero()
    try:
        with open("tabla_propuesto.txt", "w", encoding="utf-8") as f:
            f.writelines(f"{n} x {i} = {n * i}\n" for i in range(1, 11))
    except OSError as e:
        return print("No se pudo escribir el archivo:", e.strerror)
    print("Tabla guardada en tabla_propuesto.txt:")
    print(open("tabla_propuesto.txt", encoding="utf-8").read())

if __name__ == "__main__":
    main()
