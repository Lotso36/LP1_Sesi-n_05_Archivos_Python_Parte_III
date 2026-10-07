import os
import pickle

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca, self.modelo = marca, modelo
        self.en_marcha = self.acelerando = self.frenando = False

    def arrancar(self): self.en_marcha = True
    def acelerar(self): self.acelerando = True
    def frenar(self):   self.frenando = True

    def estado(self):
        return (f"Marca: {self.marca}\nModelo: {self.modelo}\nEn marcha: {self.en_marcha}\n"
                f"Acelerando: {self.acelerando}\nFrenando: {self.frenando}\n" + "-" * 25)

class Docente:
    def __init__(self, nombre, edad, horas):
        self.nombre, self.edad, self.horas = nombre, edad, horas
        print(f"Creación de nuevo docente {nombre}")

    def __str__(self):
        return f"{self.nombre} | Edad: {self.edad} | Horas: {self.horas}"

class ListaDocentes:
    ARCHIVO = "actividad6.bin"

    def __init__(self):
        self.docentes = []
        try:
            with open(self.ARCHIVO, "rb") as f:
                self.docentes = pickle.load(f)
            print(f"Se cargaron {len(self.docentes)} docentes del archivo.")
        except (FileNotFoundError, EOFError):
            print("El archivo no existe o está vacío.")

    def agregarDocente(self, d):
        self.docentes.append(d)
        self.guardar()

    def guardar(self):
        with open(self.ARCHIVO, "wb") as f:
            pickle.dump(self.docentes, f)

    def mostrarDocentes(self):
        for d in self.docentes:
            print(d)

if __name__ == "__main__":
    autos = [Vehiculo("Honda", "CRV"), Vehiculo("Toyota", "Yaris"), Vehiculo("Nissan", "Sentra")]
    autos[0].arrancar(); autos[1].acelerar()
    with open("actividad5.pckl", "wb") as f:
        pickle.dump(autos, f)
    with open("actividad5.pckl", "rb") as f:
        for v in pickle.load(f):
            print(v.estado())

    if os.path.exists(ListaDocentes.ARCHIVO):  
        os.remove(ListaDocentes.ARCHIVO)
    lista = ListaDocentes()
    for datos in (("Dely", 43, 30), ("Miguel", 24, 24), ("Leandro", 30, 18)):
        lista.agregarDocente(Docente(*datos))
    print("Lectura del archivo .bin:")
    ListaDocentes().mostrarDocentes()
