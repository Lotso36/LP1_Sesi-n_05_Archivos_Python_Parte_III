CAMPOS = ("id", "nombre", "apellido", "celular", "fecha de nacimiento")
DATOS = """1;Juan;Díaz;999999999;01/01/2000
2;Marcos;Torres;988888888;21/02/2002
3;Jesús;Lazo;977777777;10/03/2005
4;Delia;Barreda;966666666;30/04/2008
5;Alfredo;Ponce;955555555;17/11/2012
"""

def cargar_directorio(ruta="directorio.txt"):
    directorio = []
    with open(ruta, encoding="utf-8") as f:
        for n, linea in enumerate(f, 1):
            valores = linea.strip().split(";")
            if len(valores) != len(CAMPOS):
                print(f"Línea {n} ignorada: se esperaban {len(CAMPOS)} campos.")
                continue
            directorio.append(dict(zip(CAMPOS, valores)))
    return directorio

if __name__ == "__main__":
    try:
        directorio = cargar_directorio()
    except FileNotFoundError:                     
        with open("directorio.txt", "w", encoding="utf-8") as f:
            f.write(DATOS)
        directorio = cargar_directorio()
    except OSError as e:
        raise SystemExit(f"Error de lectura: {e.strerror}")
    for persona in directorio:
        print(persona)
