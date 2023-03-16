#operaciones con string
proverbio='cuando el rio suena '
proverbio2='piedras trae'

#Combinar cadenas
print(proverbio+proverbio2)
#repetir cadenas
print(proverbio*4)

#obtener un caracter
print('imprimiendo la posicion por el elemento', proverbio[2])
print('imprimiendo la posicion por el elemento', proverbio[4])
print('imprimiendo la posicion por el elemento', proverbio[6])

#Dividiendo una cadena
print(proverbio[:])
print(proverbio[5:])
print(proverbio[:5])
print(proverbio[5:12])
print(proverbio[5:13:2])

#Logitud de una cadena
print('la longitud de la cadena es', len(proverbio))
