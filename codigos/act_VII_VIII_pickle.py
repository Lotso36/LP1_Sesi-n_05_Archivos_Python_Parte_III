import pickle

with open("actividad3.pckl", "wb") as f:
    pickle.dump([1, 2, 3, 4, 5], f)

with open("actividad3.pckl", "rb") as f:
    print("Lista recuperada:", pickle.load(f))
