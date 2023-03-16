#Operaciones con listas
#Insertando en una lista
lenguaje_progra=['python','Ruby','Java','C++','JavaScript']
print(lenguaje_progra)
lenguaje_progra.append('C#')
print(lenguaje_progra)

#Agrega valores a una lista con append()
rango_numeros=[]
for i in range(21):
    if i%2==0:
        rango_numeros.append(i)
print(rango_numeros)

#Añadir elementos en cualquier posicion
lenguaje_progra.insert(1,'VB')
print(lenguaje_progra)

#Repetir elementos
print(lenguaje_progra*2)