
playlist = {}


libreria = {"California_Uber_Alles.mp3": 
                {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys", "location": "./biblioteca/California_Uber_Alles.mp3"},
            "Seattle_Party": 
                {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets", "location": "./biblioteca/Seattle_Party.flac"},
            "King_Kunta":
                {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly", "location": "./biblioteca/King_Kunta.mp3"}   
            }
import random


def seleccionaCancionRandom(libreria):


	
	listaCanciones = list(libreria.keys())
	tituloCancion = random.choice(listaCanciones)
	return tituloCancion

	assert tituloCancion in libreria, "mensaje error: no esta en libreria"

	assert isinstance(libreria, dict)



##CASOS TEST
##for i in range(1, 21):
##	print (seleccionaCancionRandom(libreria))



def iniciarPlayList(tituloCancion):
#pasar playlist
#agregar la cancionrandom

	print(seleccionaCancionRandom)

#assert while len(playlist) != libreria


 
##CASO TEST

#chequear numeroCancion == diccionario

#chequear que la cancion no esta dentro del diccionario

