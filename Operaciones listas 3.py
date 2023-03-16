#Operaciones con lista
#Combinar listas
#Conservando la lista original
Compras=['Agua','Huevos','Aceites']
Compras_Frutas=['Naranja','Manzanas','Piñas']
print(Compras+Compras_Frutas)
print(Compras)
print(Compras_Frutas)

#Modificando la lista original
Compras.extend(Compras_Frutas)
print(Compras)
print(Compras_Frutas)

#Modificar
Compras[0]='Jugo'
print(Compras)

#Eliminar
del Compras[0]#Eliminar segun indice mediante la sentencia del
print(Compras)
Compras.remove('Aceites')#Eliminando con la funcion remove()
print(Compras)
print(Compras.pop(2))
print(Compras)

Compras_Frutas.clear()#Eliminar por completo
print(Compras_Frutas)