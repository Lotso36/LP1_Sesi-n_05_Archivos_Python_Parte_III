import pickle
from propuesto18 import ARCHIVO, Tarea

def main():
    try:
        with open(ARCHIVO, "rb") as f:
            tareas = pickle.load(f)
    except FileNotFoundError:
        return print(f"No existe {ARCHIVO}. Ejecute primero propuesto18.py.")
    except (pickle.UnpicklingError, EOFError, AttributeError):
        return print("El archivo esta dañado o vacio.")
    print(f"Tareas leidas de {ARCHIVO}:")
    for i, t in enumerate(tareas, 1):
        print(f"{i}. {t}")

if __name__ == "__main__":
    main()