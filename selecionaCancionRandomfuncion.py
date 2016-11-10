def seleccionaCancionRandom(libreria):
	libreria = {"pene": "polla", "chocho": "conejo"}

	import random
	tituloCancion = list(libreria.keys())
	return random.choice(tituloCancion)



assert isinstance(libreria, dict)

assert tituloCancion in libreria

